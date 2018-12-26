from selfdrive.car.hyundai.values import DBC
from selfdrive.can.parser import CANParser
from selfdrive.config import Conversions as CV
from common.kalman.simple_kalman import KF1D
from selfdrive.car.modules.UIBT_module import UIButtons,UIButton
from selfdrive.car.modules.UIEV_module import UIEvents
import numpy as np


def get_can_parser(CP):

  signals = [
    # sig_name, sig_address, default
    ("WHL_SPD_FL", "WHL_SPD11", 0),
    ("WHL_SPD_FR", "WHL_SPD11", 0),
    ("WHL_SPD_RL", "WHL_SPD11", 0),
    ("WHL_SPD_RR", "WHL_SPD11", 0),

    ("YAW_RATE", "ESP12", 0),

    ("CF_Gway_DrvSeatBeltSw", "CGW1", 0),
    ("CF_Gway_TSigLHSw", "CGW1", 0),
    ("CF_Gway_TurnSigLh", "CGW1", 0),
    ("CF_Gway_TSigRHSw", "CGW1", 0),
    ("CF_Gway_TurnSigRh", "CGW1", 0),
    ("CF_Gway_ParkBrakeSw", "CGW1", 0),

    ("BRAKE_ACT", "EMS12", 0),
    ("PV_AV_CAN", "EMS12", 0),
    ("TPS", "EMS12", 0),

    ("CYL_PRES", "ESP12", 0),

    ("CF_Clu_CruiseSwState", "CLU11", 0),
    ("CF_Clu_CruiseSwMain" , "CLU11", 0),
    ("CF_Clu_SldMainSW", "CLU11", 0),
    ("CF_Clu_ParityBit1", "CLU11", 0),
    ("CF_Clu_VanzDecimal" , "CLU11", 0),
    ("CF_Clu_Vanz", "CLU11", 0),
    ("CF_Clu_SPEED_UNIT", "CLU11", 0),
    ("CF_Clu_DetentOut", "CLU11", 0),
    ("CF_Clu_RheostatLevel", "CLU11", 0),
    ("CF_Clu_CluInfo", "CLU11", 0),
    ("CF_Clu_AmpInfo", "CLU11", 0),
    ("CF_Clu_AliveCnt1", "CLU11", 0),

    ("CF_Clu_InhibitD", "CLU15", 0),
    ("CF_Clu_InhibitP", "CLU15", 0),
    ("CF_Clu_InhibitN", "CLU15", 0),
    ("CF_Clu_InhibitR", "CLU15", 0),

    ("CF_Lvr_Gear","LVR12",0),

    ("ACCEnable", "TCS13", 0),
    ("ACC_REQ", "TCS13", 0),
    ("DriverBraking", "TCS13", 0),
    ("DriverOverride", "TCS13", 0),

    ("ESC_Off_Step", "TCS15", 0),

    ("CF_Lvr_GearInf", "LVR11", 0),        #Transmission Gear (0 = N or P, 1-8 = Fwd, 14 = Rev)

    ("CR_Mdps_StrColTq", "MDPS12", 0),
    ("CF_Mdps_Def", "MDPS12", 0),
    ("CF_Mdps_ToiActive", "MDPS12", 0),
    ("CF_Mdps_ToiUnavail", "MDPS12", 0),
    ("CF_Mdps_MsgCount2", "MDPS12", 0),
    ("CF_Mdps_Chksum2", "MDPS12", 0),
    ("CF_Mdps_ToiFlt", "MDPS12", 0),
    ("CF_Mdps_SErr", "MDPS12", 0),
    ("CR_Mdps_StrTq", "MDPS12", 0),
    ("CF_Mdps_FailStat", "MDPS12", 0),
    ("CR_Mdps_OutTq", "MDPS12", 0),

    ("VSetDis", "SCC11", 0),
    ("MainMode_ACC", "SCC11", 0),
    ("SCCInfoDisplay", "SCC11", 0),
    ("ACCMode", "SCC12", 1),

    ("SAS_Angle", "SAS11", 0),
    ("SAS_Speed", "SAS11", 0),

    ("CF_Lca_IndLeft", "LCA11", 0),
    ("CF_Lca_IndRight", "LCA11", 0),
  ]

  checks = [
    # address, frequency
    ("MDPS12", 50),
    ("TCS15", 10),
    ("TCS13", 50),
    ("CLU11", 50),
    ("ESP12", 100),
    ("EMS12", 100),
    ("CGW1", 10),
    ("WHL_SPD11", 50),
    ("SCC11", 50),
    ("SCC12", 50),
    ("SAS11", 100)
  ]

  return CANParser(DBC[CP.carFingerprint]['pt'], signals, checks, 0)

def get_camera_parser(CP):

  signals = [
    # sig_name, sig_address, default
    ("CF_Lkas_Icon", "LKAS11", 0),
    ("CF_Lkas_LdwsSysState", "LKAS11", 0),
    ("CF_Lkas_SysWarning", "LKAS11", 0),
    ("CF_Lkas_LdwsLHWarning", "LKAS11", 0),
    ("CF_Lkas_LdwsRHWarning", "LKAS11", 0),
    ("CF_Lkas_HbaLamp", "LKAS11", 0),
    ("CF_Lkas_FcwBasReq", "LKAS11", 0),
    ("CF_Lkas_ToiFlt", "LKAS11", 0),
    ("CF_Lkas_HbaSysState", "LKAS11", 0),
    ("CF_Lkas_FcwOpt", "LKAS11", 0),
    ("CF_Lkas_HbaOpt", "LKAS11", 0),
    ("CF_Lkas_FcwSysState", "LKAS11", 0),
    ("CF_Lkas_FcwCollisionWarning", "LKAS11", 0),
    ("CF_Lkas_FusionState", "LKAS11", 0),
    ("CF_Lkas_FcwOpt_USM", "LKAS11", 0),
    ("CF_Lkas_LdwsOpt_USM", "LKAS11", 0),
    ("CF_Lkas_Unknown1", "LKAS11", 0),
    ("CF_Lkas_Unknown2", "LKAS11", 0),
    ("CF_Lkas_ActToi", "LKAS11", 0),
    ("CR_Lkas_StrToqReq", "LKAS11", 0)
  ]

  checks = [("LKAS11", 100)]
  return (CANParser(DBC[CP.carFingerprint]['pt'], signals, checks, 2)), \
    (CANParser(DBC[CP.carFingerprint]['pt'], signals, checks, 1))

class CarState(object):
  def __init__(self, CP):
    #labels for buttons
    self.btns_init = [["","",["","",""]], \
                      ["","",[""]], \
                      ["","",[""]], \
                      ["cam","CAM",[""]], \
                      ["alwon", "MAD",[""]], \
                      ["sound", "SND", [""]]]

    # ALCA PARAMS
    # max REAL delta angle for correction vs actuator
    self.CL_MAX_ANGLE_DELTA_BP = [10., 44.]
    self.CL_MAX_ANGLE_DELTA = [2.4, .3]

    # adjustment factor for merging steer angle to actuator; should be over 4; the higher the smoother
    self.CL_ADJUST_FACTOR_BP = [10., 44.]
    self.CL_ADJUST_FACTOR = [16. , 8.]


    # reenrey angle when to let go
    self.CL_REENTRY_ANGLE_BP = [10., 44.]
    self.CL_REENTRY_ANGLE = [5. , 5.]

    # a jump in angle above the CL_LANE_DETECT_FACTOR means we crossed the line
    self.CL_LANE_DETECT_BP = [10., 44.]
    self.CL_LANE_DETECT_FACTOR = [1.7, .75]

    self.CL_LANE_PASS_BP = [10., 44.]
    self.CL_LANE_PASS_TIME = [60., 3.]

    # change lane delta angles and other params
    self.CL_MAXD_BP = [10., 32., 44.]
    self.CL_MAXD_A = [.358, 0.084, 0.042] #delta angle based on speed; needs fine tune, based on Tesla steer ratio of 16.75

    self.CL_MIN_V = 8.9 # do not turn if speed less than x m/2; 20 mph = 8.9 m/s

    # do not turn if actuator wants more than x deg for going straight; this should be interp based on speed
    self.CL_MAX_A_BP = [10., 44.]
    self.CL_MAX_A = [10., 10.]

    # define limits for angle change every 0.1 s
    # we need to force correction above 10 deg but less than 20
    # anything more means we are going to steep or not enough in a turn
    self.CL_MAX_ACTUATOR_DELTA = 2.
    self.CL_MIN_ACTUATOR_DELTA = 0.
    self.CL_CORRECTION_FACTOR = 1.

    #duration after we cross the line until we release is a factor of speed
    self.CL_TIMEA_BP = [10., 32., 44.]
    self.CL_TIMEA_T = [0.7 ,0.4, 0.20]

    self.CL_WAIT_BEFORE_START = 1
    #END OF ALCA PARAMS

    self.CP = CP

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
    self.left_blinker_on = 0
    self.left_blinker_flash = 0
    self.right_blinker_on = 0
    self.right_blinker_flash = 0

    # OSM
    #self.OSM = OSM(self)
    #self.OSM.getlocal()

    #BB UIEvents
    self.UE = UIEvents(self)

    #BB variable for custom buttons
    self.cstm_btns = UIButtons(self,"Hyundai","hyundai")

    #BB pid holder for ALCA
    self.pid = None

    #BB custom message counter
    self.custom_alert_counter = -1 #set to 100 for 1 second display; carcontroller will take down to zero

  def update(self, cp, cp_cam, cp_cam2):
    # copy can_valid
    self.can_valid = cp.can_valid

    # update prevs, update must run once per Loop
    self.prev_left_blinker_on = self.left_blinker_on
    self.prev_right_blinker_on = self.right_blinker_on

    self.door_all_closed = True
    self.seatbelt = cp.vl["CGW1"]['CF_Gway_DrvSeatBeltSw']

    self.brake_pressed = cp.vl["TCS13"]['DriverBraking'] if not self.cstm_btns.get_button_status("alwon") else 0 # I'm Bad
    self.esp_disabled = cp.vl["TCS15"]['ESC_Off_Step']

    self.park_brake = cp.vl["CGW1"]['CF_Gway_ParkBrakeSw']
    self.main_on = True
    self.acc_active = (cp.vl["SCC12"]['ACCMode'] != 0) if not self.cstm_btns.get_button_status("alwon") else \
      (cp.vl["SCC11"]["MainMode_ACC"] != 0)  # I'm Dangerous!
    self.acc_active_real = (cp.vl["SCC12"]['ACCMode'] !=0)
    self.pcm_acc_status = int(self.acc_active)

    # calc best v_ego estimate, by averaging two opposite corners
    self.v_wheel_fl = cp.vl["WHL_SPD11"]['WHL_SPD_FL'] * CV.KPH_TO_MS
    self.v_wheel_fr = cp.vl["WHL_SPD11"]['WHL_SPD_FR'] * CV.KPH_TO_MS
    self.v_wheel_rl = cp.vl["WHL_SPD11"]['WHL_SPD_RL'] * CV.KPH_TO_MS
    self.v_wheel_rr = cp.vl["WHL_SPD11"]['WHL_SPD_RR'] * CV.KPH_TO_MS
    self.v_wheel = 1.035 * (self.v_wheel_fl + self.v_wheel_fr + self.v_wheel_rl + self.v_wheel_rr) / 4.

    self.low_speed_lockout = self.v_wheel < 1.0

    # Kalman filter, even though Hyundai raw wheel speed is heaviliy filtered by default
    if abs(self.v_wheel - self.v_ego) > 2.0:  # Prevent large accelerations when car starts at non zero speed
      self.v_ego_x = np.matrix([[self.v_wheel], [0.0]])

    self.v_ego_raw = self.v_wheel
    v_ego_x = self.v_ego_kf.update(self.v_wheel)
    self.v_ego = float(v_ego_x[0])
    self.a_ego = float(v_ego_x[1])
    is_set_speed_in_mph = int(cp.vl["CLU11"]["CF_Clu_SPEED_UNIT"])
    speed_conv = CV.MPH_TO_MS if is_set_speed_in_mph else CV.KPH_TO_MS
    self.cruise_set_speed = cp.vl["SCC11"]['VSetDis'] * speed_conv
    self.standstill = not self.v_wheel > 0.1

    self.angle_steers = cp.vl["SAS11"]['SAS_Angle']
    self.angle_steers_rate = cp.vl["SAS11"]['SAS_Speed']
    self.yaw_rate = cp.vl["ESP12"]['YAW_RATE']
    self.main_on = True
    self.left_blinker_on = True if (cp.vl["CGW1"]['CF_Gway_TSigLHSw'] == True) or (cp.vl["CGW1"]['CF_Gway_TurnSigLh'] == True) else False
    self.left_blinker_flash = cp.vl["CGW1"]['CF_Gway_TurnSigLh']
    self.right_blinker_on = True if (cp.vl["CGW1"]['CF_Gway_TSigRHSw'] == True) or (cp.vl["CGW1"]['CF_Gway_TurnSigRh'] == True) else False
    self.right_blinker_flash = cp.vl["CGW1"]['CF_Gway_TurnSigRh']
    self.steer_override = abs(cp.vl["MDPS12"]['CR_Mdps_StrColTq']) > 1.0
    self.steer_state = cp.vl["MDPS12"]['CF_Mdps_ToiActive'] #0 NOT ACTIVE, 1 ACTIVE
    self.steer_error = cp.vl["MDPS12"]['CF_Mdps_ToiUnavail']
    self.brake_error = 0
    self.steer_torque_driver = cp.vl["MDPS12"]['CR_Mdps_StrColTq']
    self.steer_torque_motor = cp.vl["MDPS12"]['CR_Mdps_OutTq']
    self.stopped = cp.vl["SCC11"]['SCCInfoDisplay'] == 4.

    self.user_brake = 0

    self.brake_lights = bool(self.brake_pressed)
    if (cp.vl["TCS13"]["DriverOverride"] == 0 and cp.vl["TCS13"]['ACC_REQ'] == 1):
      self.pedal_gas = 0
    else:
      self.pedal_gas = cp.vl["EMS12"]['TPS']
    self.car_gas = cp.vl["EMS12"]['TPS']

    # Gear Selecton - This is not compatible with all Kia/Hyundai's, But is the best way for those it is compatible with
    gear = cp.vl["LVR12"]["CF_Lvr_Gear"]
    if gear == 5:
      self.gear_shifter = "drive"
    elif gear == 6:
      self.gear_shifter = "neutral"
    elif gear == 0:
      self.gear_shifter = "park"
    elif gear == 7:
      self.gear_shifter = "reverse"
    else:
      self.gear_shifter = "unknown"

    # Gear Selection via Cluster - For those Kia/Hyundai which are not fully discovered, we can use the Cluster Indicator for Gear Selection, as this seems to be standard over all cars, but is not the preferred method.
    if cp.vl["CLU15"]["CF_Clu_InhibitD"] == 1:
      self.gear_shifter_cluster = "drive"
    elif cp.vl["CLU15"]["CF_Clu_InhibitN"] == 1:
      self.gear_shifter_cluster = "neutral"
    elif cp.vl["CLU15"]["CF_Clu_InhibitP"] == 1:
      self.gear_shifter_cluster = "park"
    elif cp.vl["CLU15"]["CF_Clu_InhibitR"] == 1:
      self.gear_shifter_cluster = "reverse"
    else:
      self.gear_shifter_cluster = "unknown"

    # save the entire LKAS11, CLU11 and MDPS12
    #print cp_cam.can_valid, cp_cam2.can_valid
    if cp_cam.can_valid == True:
      self.lkas11 = cp_cam.vl["LKAS11"]
      self.camcan = 2
    else:
      self.lkas11 = cp_cam2.vl["LKAS11"]
      self.camcan = 1

    self.clu11 = cp.vl["CLU11"]
    self.mdps12 = cp.vl["MDPS12"]

    # Lane Change Assist Messages
    self.lca_left = cp.vl["LCA11"]["CF_Lca_IndLeft"]
    self.lca_right = cp.vl["LCA11"]["CF_Lca_IndRight"]
