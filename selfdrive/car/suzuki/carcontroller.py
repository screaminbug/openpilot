from selfdrive.boardd.boardd import can_list_to_can_capnp
from selfdrive.car.suzuki import suzukican
from opendbc.can.packer import CANPacker
from selfdrive.car.suzuki.values import CAR, DBC

class CarControllerParams:
  def __init__(self, car_fingerprint):
    if car_fingerprint == CAR.SWIFT:
      self.STEER_MAX = 1100
      self.STEER_STEP = 1              # how often we update the steer cmd
      self.STEER_DELTA_UP = 7          # ~0.75s time to peak torque (255/50hz/0.75s)
      self.STEER_DELTA_DOWN = 17       # ~0.3s from peak torque to zero

      self.STEER_DRIVER_ALLOWANCE = 50   # allowed driver torque before start limiting
      self.STEER_DRIVER_MULTIPLIER = 4   # weight driver torque heavily
      self.STEER_DRIVER_FACTOR = 100     # from dbc
      self.NEAR_STOP_BRAKE_PHASE = 0.5 # m/s, more aggressive braking near full stop


class CarController(object):
  def __init__(self, car_fingerprint, canbus):
    self.apply_steer_last = 0
    # Setup detection helper. Routes commands to
    # an appropriate CAN bus number.
    self.canbus = canbus
    self.params = CarControllerParams(car_fingerprint)

    self.packer_pt = CANPacker(DBC[car_fingerprint]['pt'])

  def update(self, sendcan, enabled, CS, frame, actuators):

    """ Controls thread """

    # **** process the car messages ****

    # *** compute control surfaces ***

    P = self.params

    # Send CAN commands.
    can_sends = []

    apply_steer = 0

    if (frame % P.STEER_STEP) == 0:
      if enabled and not CS.steer_not_allowed:
        apply_steer = actuators.steer * P.STEER_MAX + (P.STEER_MAX / 2)

      self.apply_steer_last = apply_steer
      idx = (frame / P.STEER_STEP) % 4

      can_sends.append(suzukican.create_steering_control(self.packer_pt,
        self.canbus, apply_steer, idx))

    sendcan.send(can_list_to_can_capnp(can_sends, msgtype='sendcan').to_bytes())

    self.apply_steer_last = apply_steer
