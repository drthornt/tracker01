#!/usr/bin/env python
import time
import Adafruit_ADS1x15
import sys
from datetime import datetime, date, time

adc = Adafruit_ADS1x15.ADS1015()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

#print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
#print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
#print('-' * 37)
# Main loop.
#while True:
    # Read all the ADC channel values in a list.
    #values = [0]*2
    #values[0] = adc.read_adc(0, gain=GAIN)
    #values[1] = adc.read_adc(1, gain=GAIN)
    #values[0] = adc.read_adc(2, gain=GAIN)
    #values[1] = adc.read_adc(3, gain=GAIN)
    #for i in range(4):
    #    values[i] = adc.read_adc(i, gain=GAIN)
    # Print the ADC values.
    #print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    #print('| {0:>6} | {1:>6} |'.format(*values))
    # Pause for half a second.
    #time.sleep(0.5)


def reading():
    dt = datetime.now()
    GAIN = 1
    epoch = int(datetime.now().strftime("%s"))
    values = [0]*2
    values[0] = adc.read_adc(2, gain=GAIN)
    values[1] = adc.read_adc(3, gain=GAIN)
    #print('| {0:>6} | {1:>6} |'.format(*values))
    sys.stdout.write("{} {} {}\n".format(epoch,values[0], values[1]))

if __name__ == "__main__":
    reading()
