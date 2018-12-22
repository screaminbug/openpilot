from selfdrive.can.parser import CANParser
from selfdrive.config import Conversions as CV
from selfdrive.car.ford.values import DBC
from common.kalman.simple_kalman import KF1D
import numpy as np

WHEEL_RADIUS = 0.33

def get_can_parser(CP):

  signals = [
    # sig_name, sig_address, default
    ("WHEEL_REAR_RIGHT", "WHEEL_SPEEDS", 0.),
    ("WHEEL_REAR_LEFT", "WHEEL_SPEEDS", 0.),
    ("WHEEL_FRONT_RIGHT", "WHEEL_SPEEDS", 0.),
    ("WHEEL_FRONT_LEFT", "WHEEL_SPEEDS", 0.),
    ("STEER_SMOOTH_1", "STEER_INPUT", 0.),
   # ("Cruise_State", "Cruise_Status", 0.),
   # ("Set_Speed", "Cruise_Status", 0.),
   # ("LaActAvail_D_Actl", "Lane_Keep_Assist_Status", 0),
   # ("LaHandsOff_B_Actl", "Lane_Keep_Assist_Status", 0),
   # ("LaActDeny_B_Actl", "Lane_Keep_Assist_Status", 0),
    ("GAS_1", "ENGINE_CONTROL", 0.),
   # ("Dist_Incr", "Steering_Buttons", 0.),
   # ("Brake_Drv_Appl", "Cruise_Status", 0.),
   # ("Brake_Lights", "BCM_to_HS_Body", 0.),
  ]

  checks = [
  ]

  return CANParser(DBC[CP.carFingerprint]['pt'], signals, checks, 0)


class CarState(object):
  def __init__(self, CP):

    self.CP = CP
    self.left_blinker_on = 0
    self.right_blinker_on = 0

    # initialize can parser
    self.car_fingerprint = CP.carFingerprint

    # vEgo kalman filter
    dt = 0.01
    # Q = np.matrix([[10.0, 0.0], [0.0, 100.0]])
    # R = 1e3
    self.v_ego_kf = KF1D(x0=np.matrix([[0.0], [0.0]]),
                         A=np.matrix([[1.0, dt], [0.0, 1.0]]),
                         C=np.matrix([1.0, 0.0]),
                         K=np.matrix([[0.12287673], [0.29666309]]))
    self.v_ego = 0.0

  def update(self, cp):
    # copy can_valid
    self.can_valid = cp.can_valid

    # update prevs, update must run once per loop
    self.prev_left_blinker_on = self.left_blinker_on
    self.prev_right_blinker_on = self.right_blinker_on

    # calc best v_ego estimate, by averaging two opposite corners
    self.v_wheel_fl = cp.vl["WHEEL_SPEEDS"]['WHEEL_SPEED_REAR_RIGHT'] * WHEEL_RADIUS
    self.v_wheel_fr = cp.vl["WHEEL_SPEEDS"]['WHEEL_SPEED_REAR_LEFT'] * WHEEL_RADIUS
    self.v_wheel_rl = cp.vl["WHEEL_SPEEDS"]['WHEEL_SPEED_FRONT_RIGHT'] * WHEEL_RADIUS
    self.v_wheel_rr = cp.vl["WHEEL_SPEEDS"]['WHEEL_SPEED_FRONT_LEFT'] * WHEEL_RADIUS
    self.v_wheel = float(np.mean([self.v_wheel_fl, self.v_wheel_fr, self.v_wheel_rl, self.v_wheel_rr]))

    # Kalman filter
    if abs(self.v_wheel - self.v_ego) > 2.0:  # Prevent large accelerations when car starts at non zero speed
      self.v_ego_x = np.matrix([[self.v_wheel], [0.0]])

    self.v_ego_raw = self.v_wheel
    v_ego_x = self.v_ego_kf.update(self.v_wheel)
    self.v_ego = float(v_ego_x[0])
    self.a_ego = float(v_ego_x[1])
    self.standstill = not self.v_wheel > 0.001

    self.angle_steers = cp.vl["STEER_INPUT"]['STEER_SMOOTH_1']
    self.v_cruise_pcm = 0 #cp.vl["Cruise_Status"]['Set_Speed'] * CV.MPH_TO_MS
    self.pcm_acc_status = 0 #cp.vl["Cruise_Status"]['Cruise_State']
    self.main_on = 0 #cp.vl["Cruise_Status"]['Cruise_State'] != 0
    self.lkas_state = 0 # cp.vl["Lane_Keep_Assist_Status"]['LaActAvail_D_Actl']
    self.steer_override = 0 #not cp.vl["Lane_Keep_Assist_Status"]['LaHandsOff_B_Actl']
    self.steer_error = 0 # cp.vl["Lane_Keep_Assist_Status"]['LaActDeny_B_Actl']
    self.user_gas = cp.vl["ENGINE_CONTROL"]['GAS_1']
    self.brake_pressed = 0 #bool(cp.vl["Cruise_Status"]["Brake_Drv_Appl"])
    self.brake_lights = 0 #bool(cp.vl["BCM_to_HS_Body"]["Brake_Lights"])
    self.generic_toggle = 0 #bool(cp.vl["Steering_Buttons"]["Dist_Incr"])
