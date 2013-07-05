import threading
import signal
import sys,os,time
from frames import frames
from colorsmap import getColors

def nyan(f, kind=1):
    state = []
    def showAnimation(quit_plz):
        colors, output, always_escape = getColors(kind)

        cachedframes = []
        for f in frames:
            fr = []
            for y,row in enumerate(f):
                if always_escape:
                    fr.append("".join(colors[cell] for cell in row))
                else:
                    fr.append("".join(colors[cell]+output for cell in row))
            cachedframes.append(fr)

        def frameGen():
            while True:
                for f in cachedframes:
                    yield f

        last_frame = False
        lastcode = None
        for f in frameGen():
            ns = len(state)
            print "\033[?25h\033[0m\033[H\033[2J"
            for y,row in enumerate(f):
                if y <= 22 and 22-y < len(state):
                    n = 22-y
                    if not always_escape:
                        print "\033[1;37m",
                    print ("%s%s" % (" "*30, state[n])),
                    if not always_escape:
                        print "\033[J\033[0m"
                    else:
                        print
                    continue
                print row

            if last_frame: break
            quit = quit_plz.wait(0.07)
            if quit: last_frame = True 

        print "\033[0m"

    quit_plz = threading.Event()
    t = threading.Thread(target=showAnimation, args=(quit_plz,))
    t.start()

    def endAnimation():
        quit_plz.set()
        t.join()

    def catchint(sig,fra):
        endAnimation()
        sys.exit(0)
    signal.signal(signal.SIGINT, catchint)

    try:
        f(state)
    except Exception as e:
        print e

    endAnimation()
