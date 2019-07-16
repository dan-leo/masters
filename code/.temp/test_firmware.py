from test_ import *

def test_fota():
    # 0x08002000
    # 0x0800d644
    with open('firmware/sim7020E_bootloader.bin', 'r') as bl:
        pass
    # 0x08012000
    # 0x0827b750
    addr = 0x08012000
    with open('firmware/sim7020E.bin', 'rb') as fw:
        while True:
            l = fw.read(512)
            if not len(l):
                break
            print(len(l))
            expect('AT+CFLW=1,' + str(addr) + ',' + str(len(l)), '>')
            addr += len(l)
            break