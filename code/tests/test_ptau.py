from __future__ import print_function
from process.globals import *

colorama.init()

def setup_module(module):
    print()
    serialOpen()
 
def teardown_module(module):
    serialClose()

# @pytest.mark.skip()
def test_pset():
    setEDRX(0, 0, 0, 0, 3, 2) # 5.5 sec ptau

def test_ptau():
    capture(1000)