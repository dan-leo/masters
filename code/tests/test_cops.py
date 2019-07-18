from test_ import *

descr = '100'

@pytest.mark.skip()
def test_copsset():
    # setEDRX(0, 0, 2, 1, 6, 1) # 2.56 continuous
    setEDRX(0, 9, 0, 0, 0, 0) # off

def test_cops_register():
    expect('AT+CFUN=1', 'OK', 3)
    if '+CSCON: 0' in expect('AT+COPS=0', ['+CEREG: 1', '+CSCON: 0'], 200):
        capture(1, 'cops/failed/' + descr)

@pytest.mark.skip()
def test_cops_delay():
    print('Delay initiated.')
    time.sleep(100)
    print('Delay ended.')

def test_cops_release():
    expect('at+nsocl=0', '')
    receiveAT(1)
    OK('AT+NSOCR="DGRAM",17,14000,1')
    receiveAT(1)
    expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,1,"FF"', '+CSCON: 0', 100)
    OK('at+nsocl=0')

def test_cops_capture():
    capture(1, 'cops/' + descr)

def test_cops_deregister():
    expect('AT+COPS=2', '+NPSMR:', 100)

def test_cops_capture2():
    expect('AT+CFUN=0', '', 1)
    capture(1, 'cops/deregister/' + descr)
