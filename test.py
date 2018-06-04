#!/usr/bin/env python

from ina219 import INA219
from ina219 import DeviceRangeError
import sys
from datetime import datetime, date, time

SHUNT_OHMS = 0.1

MAX_EXPECTED_AMPS = 0.2

def read():
    # ina = INA219(SHUNT_OHMS)
    ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS, address=0x41)
    # ina.configure()
    ina.configure(ina.RANGE_16V)

    dt = datetime.now()
    sys.stdout.write("%s " % dt )
    # print("Bus Voltage: %.3f V" % ina.voltage())
    sys.stdout.write("Bus Voltage: %.3f V " % ina.voltage())
    try:
        sys.stdout.write("Bus Current: %.3f mA " % ina.current())
        sys.stdout.write("Power: %.3f mW " % ina.power())
        sys.stdout.write("Shunt voltage: %.3f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resister
        print(e)
    sys.stdout.write("\n")

if __name__ == "__main__":
    read()
