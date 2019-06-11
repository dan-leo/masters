from process.globals import *

def guess_seq_len(seq):
    # find number of sequences in similar arrays
    # limited to a maximum difference
    # seq = [18158, 12118, 8360, 20478, 20478, ...]
    maxDiff = 100
    guess = 0
    
    for s in range(len(seq)):
        for x in range(2, int((len(seq) - s) / 2) + 1):
            # print(s, x, seq[s:s+x], "==", seq[s+x:s+2*x])
            a = abs(np.array(seq[s:s+x]) - np.array(seq[s+x:s+2*x]))
            if len(a) and not False in (a < np.array([maxDiff] * len(a))):
                print(s, x, a, seq[s:s+x], "==", seq[s+x:s+2*x])
                return x

    return guess