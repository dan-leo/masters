from test_ import *

descr = '50'

# @pytest.mark.skip()
def test_ptauset():
    setEDRX(4, 1, 0, 0, 3, 2) # 5.5 sec ptau

def test_ptau():
    capture(1000, 'ptau/' + descr)