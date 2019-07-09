from __future__ import print_function
from process.globals import *

def setup_module(module):
    print()
    serialOpen()
 
def teardown_module(module):
    serialClose()

@pytest.mark.skip()
def test_copsset():
    # setEDRX(0, 0, 2, 1, 6, 1) # 2.56 continuous
    setEDRX(0, 9, 0, 0, 0, 0) # off

def test_cops_register():
    expect('AT+COPS=0', '+CEREG: 1', 10)

@pytest.mark.skip()
def test_cops_delay():
    print('Delay initiated.')
    time.sleep(10)
    print('Delay ended.')

def test_cops_release():
    expect('at+nsocl=0', '')
    receiveAT(1)
    OK('AT+NSOCR="DGRAM",17,14000,1')
    expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,1,"FF"', '+CSCON: 0', 10)
    OK('at+nsocl=0')

def test_cops_capture():
    capture(1)

def test_cops_deregister():
    expect('AT+COPS=2', '+NPSMR:', 10)
