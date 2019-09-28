from __future__ import print_function
from process.globals import *   

# def pytest_configure():

def setup_module(module):
    pytest.vendor = 'vendor_undef'
    serialOpen()
    print()

    pytest.manufacturer = 'huawei'
    # pytest.manufacturer = 'ericsson'
    # pytest.manufacturer = 'nokia'
    # pytest.manufacturer = 'zte'

    # pytest.loc = 'vodacom/cticc/'
    # pytest.loc = 'vodacom/centurycity/'
    # pytest.loc = 'vodacom/quellerina/'
    # pytest.loc = 'vodacom/quellerina_behavior/'
    # pytest.loc = 'mtn/mil_lab/'
    # pytest.loc = 'mtn/rf_shield/'
    # pytest.loc = 'mtn/testplant_14th/'
    pytest.loc = 'vodacom/testplant_14th/'
    # pytest.loc = 'mtn/testplant_14th_behavior/'

    # pytest.descr = '0'
    # pytest.descr = '5'
    pytest.descr = '10'
    # pytest.descr = '20'
    # pytest.descr = '30'
    # pytest.descr = '40'
    # pytest.descr = '50'
    # pytest.descr = '60'
    # pytest.descr = '70'
    # pytest.descr = '80'
    # pytest.descr = '90'
    # pytest.descr = '100'
    # pytest.descr = '110'

    pytest.test = 'dump/'
    pytest.subtest = ''

    # pytest.lock = threading.Lock()
 
def teardown_module(module):
    serialClose()