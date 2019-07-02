from __future__ import print_function
from process.globals import *

def setup_module(module):
    serialOpen()
 
def teardown_module(module):
    serialClose()

# @pytest.mark.setup
# def test_connect():
#     assert serAT.is_open == True

@pytest.mark.setup
def test_AT():
    OK('AT')

@pytest.mark.setup
def test_NCONFIG():
    OK('AT+NCONFIG="AUTOCONNECT","FALSE"')
    OK('AT+NCONFIG="CR_0859_SI_AVOID","TRUE"')
    OK('AT+NCONFIG="CR_0354_0338_SCRAMBLING","TRUE"')

@pytest.mark.setup
def test_URC():
    OK('AT+CMEE=1')
    OK('AT+CSCON=1')
    OK('AT+CEREG=5')
    OK('AT+NPSMR=1')

@pytest.mark.setup
def test_CFUN():
    OK('AT+CFUN=0', 3)
    expect('at+cfun?', '+CFUN: 0', 1)
    expect('AT+CFUN=1', '+CEREG: 0', 2)
    receiveAT()

@pytest.mark.setup
def test_COPS():
    expect('AT+COPS=0', '+CEREG: 1', 10)

@pytest.mark.setup
def test_CEREG():
    expect('AT+CEREG?', '+CEREG: 5,1')

@pytest.mark.setup
def test_ping():
    expect('at+nping="8.8.8.8"', '+NPING: "8.8.8.8"', 10)

@pytest.mark.release
def test_release():
    # expect('at+cops=2', '+NPSMR: 1', 10)
    # expect('at+cops=0', '+CEREG: 1', 10)
    OK('AT+NSOCR="DGRAM",17,14000,1')
    expect('AT+NSOSTF=0,"1.1.1.1",7,0x200,1,"FF"', '+CSCON: 0', 10)
    OK('at+nsocl=0')