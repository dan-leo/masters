from test_ import *

# @pytest.mark.skip()
def test_drxset():
    setEDRX(0, 0, 2, 1, 6, 1) # 2.56 continuous

def test_drxcap():
    # capture(12)
    capture(1000)