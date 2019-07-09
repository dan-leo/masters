from __future__ import print_function
from process.globals import *

def setup_module(module):
    print()
    serialOpen()
 
def teardown_module(module):
    serialClose()

@pytest.mark.skip()
def test_echoset():
    setEDRX(1, 0, 0, 15, 3, 15) # 2.56 cont, 30 sec ptau

# AT+NSOCR="DGRAM",17,14000
def test_echo():
    # expect('at+cops=2', '+NPSMR: 1', 10)
    # expect('at+cops=0', '+CEREG: 1', 10)
    expect('at+nsocl=0', '')
    receiveAT(1)
    OK('AT+NSOCR="DGRAM",17,14000')
#     expect('AT+NSOST=0,"195.34.89.241",7,5,"48656c6c6F"', '+CSCON: 1', 10)
    expect('AT+NSOSTF=0,"195.34.89.241",7,0x400,1,"FF"', '+CSCON: 0', 10)
    # receiveAT(4)
    OK('AT+NSORF=0,5', 3)
    OK('at+nsocl=0')