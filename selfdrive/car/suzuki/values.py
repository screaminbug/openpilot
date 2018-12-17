from selfdrive.car import dbc_dict

class CAR:
  SWIFT = "SUZUKI SWIFT 2013"

FINGERPRINTS = {
  CAR.SWIFT: [{
    208: 8, 209: 8, 210: 8, 276: 8, 281: 8, 288: 6, 290: 5, 292: 7, 319: 4, 429: 8, 431: 8, 440: 8, 495: 8, 672: 8, 784: 8, 788: 8, 792: 8, 928: 8, 929: 4, 930: 4, 952: 8, 953: 6, 959: 3, 976: 8, 977: 8, 985: 5, 1000: 2, 1280: 8, 1281: 4, 1585: 5, 1590: 5, 1591: 5, 1593: 5, 1595: 5, 1598: 5, 1664: 5
  }]
}

STEER_THRESHOLD = 100

DBC = {
  CAR.SWIFT: dbc_dict('suzuki_swift_2013_pt_generated', 'suzuki_swift_2013_adas'),
}

NO_DSU_CAR = []
