from process.globals import *

def read(filename):
    f = open(filename)
    reader = pynmea2.NMEAStreamReader(f)

    while 1:
        for msg in reader.next():
            print(msg)


def read():
    reader = pynmea2.NMEAStreamReader()
    com = s.serGPS
    if com:
        while 1:
            data = com.read(16).decode('utf-8')
            for nmea in reader.next(data):
                msg = pynmea2.parse(str(nmea))
                print(type(msg))
                print(msg.fields)