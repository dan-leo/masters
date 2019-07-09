from __future__ import print_function
from process.globals import *

def setup_module(module):
    print()
    serialOpen()
 
def teardown_module(module):
    serialClose()