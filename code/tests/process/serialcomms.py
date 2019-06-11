from process.globals import *

black   =  '\033[1;30m'
red     =  '\033[1;31m'
green   =  '\033[1;32m'
yellow  =  '\033[1;33m'
blue    =  '\033[1;34m'
magenta =  '\033[1;35m'
cyan    =  '\033[1;36m'
white   =  '\033[1;37m'

serAT = serial.Serial('COM106', 9600, timeout=1)
serTIM = serial.Serial('COM15', 115200, timeout=1)
serGPS = serial.Serial('COM83', 9600, timeout=3)

def sendTIM(cmd):
    print(yellow + cmd)
    serTIM.write(bytes(cmd + '\r', 'utf-8'))

def receiveTIM():
    c = 0
    a = []
    b = []
    g = 0
    now = time.time()
    while True and (time.time() - now < 600.0):
        d = serTIM.readline().decode('utf-8')
        if len(d):
            d = d.strip()
            a.append(d)
            b.append(int(d.split(',')[0]))
            print(white + d, blue + str(b))
            g = find.guess_seq_len(b)
            if g != 0:
                print(magenta + str(g))
                break
    
def sendAT(cmd, t=0, expect='OK'):
    print(yellow + cmd)
    serAT.write(bytes(cmd + '\r', 'utf-8'))
    return receiveAT(t, expect)

def receiveAT(t=0, expect='OK'):
    c = 0
    data = []
    while True:
        d = serAT.readline().decode('utf-8')
        if not len(d):
            c += 1
        d = d.strip()
        if len(d) > 0:
            print(cyan + d)
            out = p.converter(d)
            if out:
                print(magenta + out)
            data.append(d)
        if t > 0:
            if c == t:
                data.append('timeout')
                return data
        if expect in d or 'ERROR' in d:
            return data