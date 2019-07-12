from test_ import *

# @pytest.mark.skip()
def test_pset():
    setEDRX(0, 0, 0, 0, 3, 2) # 5.5 sec ptau

def test_ptau():
    capture(1000)