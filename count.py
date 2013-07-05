import nyan
import time
import sys

def countTo100(state):
    state.append("")
    for i in range(101):
        state[0] = "Counting to 100...  %d" % i
        time.sleep(.1)

try:
    kind = int(sys.argv[1])
except IndexError:
    kind = 1
nyan.nyan(countTo100, kind)
