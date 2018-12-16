from selfdrive.car import dbc_dict

class CAR:
  SWIFT = "SUZUKI SWIFT 2013"

class ECU:
  CAM = 0 # camera
  DSU = 1 # driving support unit
  APGS = 2 # advanced parking guidance system


# addr: (ecu, cars, bus, 1/freq*100, vl)
STATIC_MSGS = [
  (0x130, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 1, 100, '\x00\x00\x00\x00\x00\x00\x38'),
  (0x240, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
  (0x241, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
  (0x244, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
  (0x245, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 1,   5, '\x00\x10\x01\x00\x10\x01\x00'),
  (0x248, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 1,   5, '\x00\x00\x00\x00\x00\x00\x01'),
  (0x367, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 0,  40, '\x06\x00'),
  (0x414, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 0, 100, '\x00\x00\x00\x00\x00\x00\x17\x00'),
  (0x466, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.HIGHLANDER, CAR.HIGHLANDERH), 1, 100, '\x20\x20\xAD'),
  (0x466, ECU.CAM, (CAR.COROLLA), 1, 100, '\x24\x20\xB1'),
  (0x489, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 0, 100, '\x00\x00\x00\x00\x00\x00\x00'),
  (0x48a, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 0, 100, '\x00\x00\x00\x00\x00\x00\x00'),
  (0x48b, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 0, 100, '\x66\x06\x08\x0a\x02\x00\x00\x00'),
  (0x4d3, ECU.CAM, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 0, 100, '\x1C\x00\x00\x01\x00\x00\x00\x00'),

  (0x128, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1,   3, '\xf4\x01\x90\x83\x00\x37'),
  (0x128, ECU.DSU, (CAR.HIGHLANDER, CAR.HIGHLANDERH), 1,   3, '\x03\x00\x20\x00\x00\x52'),
  (0x141, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 1,   2, '\x00\x00\x00\x46'),
  (0x160, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 1,   7, '\x00\x00\x08\x12\x01\x31\x9c\x51'),
  (0x161, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA), 1,   7, '\x00\x1e\x00\x00\x00\x80\x07'),
  (0X161, ECU.DSU, (CAR.HIGHLANDERH, CAR.HIGHLANDER), 1,  7, '\x00\x1e\x00\xd4\x00\x00\x5b'),
  (0x283, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 0,   3, '\x00\x00\x00\x00\x00\x00\x8c'),
  (0x2E6, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 0,   3, '\xff\xf8\x00\x08\x7f\xe0\x00\x4e'),
  (0x2E7, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 0,   3, '\xa8\x9c\x31\x9c\x00\x00\x00\x02'),
  (0x33E, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 0,  20, '\x0f\xff\x26\x40\x00\x1f\x00'),
  (0x344, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH), 0,   5, '\x00\x00\x01\x00\x00\x00\x00\x50'),
  (0x365, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.HIGHLANDERH), 0,  20, '\x00\x00\x00\x80\x03\x00\x08'),
  (0x365, ECU.DSU, (CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER), 0,  20, '\x00\x00\x00\x80\xfc\x00\x08'),
  (0x366, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.HIGHLANDERH), 0,  20, '\x00\x00\x4d\x82\x40\x02\x00'),
  (0x366, ECU.DSU, (CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER), 0,  20, '\x00\x72\x07\xff\x09\xfe\x00'),
  (0x470, ECU.DSU, (CAR.PRIUS, CAR.LEXUS_RXH), 1, 100, '\x00\x00\x02\x7a'),
  (0x470, ECU.DSU, (CAR.HIGHLANDER, CAR.HIGHLANDERH, CAR.RAV4H), 1,  100, '\x00\x00\x01\x79'),
  (0x4CB, ECU.DSU, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDERH, CAR.HIGHLANDER), 0, 100, '\x0c\x00\x00\x00\x00\x00\x00\x00'),

  (0x292, ECU.APGS, (CAR.PRIUS), 0,   3, '\x00\x00\x00\x00\x00\x00\x00\x9e'),
  (0x32E, ECU.APGS, (CAR.PRIUS), 0,  20, '\x00\x00\x00\x00\x00\x00\x00\x00'),
  (0x396, ECU.APGS, (CAR.PRIUS), 0, 100, '\xBD\x00\x00\x00\x60\x0F\x02\x00'),
  (0x43A, ECU.APGS, (CAR.PRIUS), 0, 100, '\x84\x00\x00\x00\x00\x00\x00\x00'),
  (0x43B, ECU.APGS, (CAR.PRIUS), 0, 100, '\x00\x00\x00\x00\x00\x00\x00\x00'),
  (0x497, ECU.APGS, (CAR.PRIUS), 0, 100, '\x00\x00\x00\x00\x00\x00\x00\x00'),
  (0x4CC, ECU.APGS, (CAR.PRIUS), 0, 100, '\x0D\x00\x00\x00\x00\x00\x00\x00'),
]

ECU_FINGERPRINT = {
  ECU.CAM: 0x2e4,   # steer torque cmd
  ECU.DSU: 0x343,   # accel cmd
  ECU.APGS: 0x835,  # angle cmd
}


def check_ecu_msgs(fingerprint, ecu):
  # return True if fingerprint contains messages normally sent by a given ecu
  return ECU_FINGERPRINT[ecu] in fingerprint


FINGERPRINTS = {
  CAR.SWIFT: [{
    8, 209: 8, 210: 8, 276: 8, 281: 8, 288: 6, 290: 5, 292: 7, 319: 4, 429: 8, 431: 8, 440: 8, 495: 8, 672: 8, 784: 8, 788: 8, 792: 8, 928: 8, 929: 4, 930: 4, 952: 8, 953: 6, 959: 3, 976: 8, 977: 8, 985: 5, 1000: 2, 1280: 8, 1281: 4, 1585: 5, 1590: 5, 1591: 5, 1593: 5, 1595: 5, 1598: 5, 1664: 5
  }]
}

STEER_THRESHOLD = 100

DBC = {
  CAR.SWIFT: dbc_dict('suzuki_swift_2013_pt_generated', 'suzuki_swift_2013_adas'),
  CAR.RAV4: dbc_dict('toyota_rav4_2017_pt_generated', 'toyota_prius_2017_adas'),
  CAR.PRIUS: dbc_dict('toyota_prius_2017_pt_generated', 'toyota_prius_2017_adas'),
  CAR.COROLLA: dbc_dict('toyota_corolla_2017_pt_generated', 'toyota_prius_2017_adas'),
  CAR.LEXUS_RXH: dbc_dict('lexus_rx_hybrid_2017_pt_generated', 'toyota_prius_2017_adas'),
  CAR.CHR: dbc_dict('toyota_chr_2018_pt_generated', 'toyota_prius_2017_adas'),
  CAR.CHRH: dbc_dict('toyota_chr_hybrid_2018_pt_generated', 'toyota_prius_2017_adas'),
  CAR.CAMRY: dbc_dict('toyota_chr_2018_pt_generated', 'toyota_prius_2017_adas'),
  CAR.CAMRYH: dbc_dict('toyota_camry_hybrid_2018_pt_generated', 'toyota_prius_2017_adas'),
  CAR.HIGHLANDER: dbc_dict('toyota_highlander_2017_pt_generated', 'toyota_prius_2017_adas'),
  CAR.HIGHLANDERH: dbc_dict('toyota_highlander_hybrid_2018_pt_generated', 'toyota_prius_2017_adas'),
}

NO_DSU_CAR = []
