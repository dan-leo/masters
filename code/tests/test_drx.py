from __future__ import print_function
from process.globals import *

def setup_module(module):
    print()
    serialOpen()
 
def teardown_module(module):
    serialClose()

@pytest.mark.skip()
def test_drxset():
    setEDRX(0, 0, 2, 1, 6, 1) # 2.56 continuous

def test_drx():
    capture(12)