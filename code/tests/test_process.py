from process.globals import *


def test_gps():
    g.read()


def test_findRepetition():
    f = open("../logs/pulses0x1331NWeDRX81.92PTW5.21.log", "r")
    lines = f.readlines()
    a = []
    for l in lines:
        a.append(int(l.split(',')[0]))
    assert guess_seq_len(a) == 3
    assert guess_seq_len([16632, 20214, 20213, 20214, 20213, ]) == 2
    assert guess_seq_len([1039, 7335, 20215, 20215, 20214, 20213, ]) == 2
    assert guess_seq_len([1039, 7335, 3333, 20215, 20215, 20214, 20213]) == 2