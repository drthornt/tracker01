#!/usr/bin/env python

from ina219 import INA219
from ina219 import DeviceRangeError
import sys
from datetime import datetime, date, time
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()

GAIN = 1

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 0.2


# HTU21 stuff
Htu21dI2cAddress = 0x40
humidity = 0;
SampleHumidityHoldCommnand = 0xE5

def read_current():
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

def read_adc():
    values = [adc.read_adc(2, gain=GAIN),adc.read_adc(2, gain=GAIN)]
    print('{0:>6} {1:>6}'.format(*values))
    

if __name__ == "__main__":
    read_current()
    read_adc()
