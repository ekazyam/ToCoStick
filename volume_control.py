#!/usr/bin/env python

import serial


class TocoAnalyzer:

    # stored data of serial device.
    def __init__(self, serial_inf):
        self.serial_inf = serial_inf

    # read serial data from 2525a.
    def read_serial(self):

        # analyze for serial data.
        def data_analyze(data):
            print(data[31:].strip())

        while True:
            line = self.serial_inf.readline()
            if len(line) > 0:
                data_analyze(line)


# Setting for ToCoStick Devide information.
TOCO_DEV = "/dev/ttyUSB0"
RATE = 115200
TIMEOUT = 10

serial_inf = serial.Serial(TOCO_DEV, RATE, timeout=TIMEOUT)
analyze = TocoAnalyzer(serial_inf)

while True:
    try:
        analyze.read_serial()
    except KeyboardInterrupt:
        break
    except:
        continue

serial_inf.close()
