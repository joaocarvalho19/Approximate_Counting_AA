from fixed_counter import FixedCounter
from exact_counter import ExactCounter
from decreasing_counter import DecreasingCounter
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
import time


def testFixed():
    repeatitions = {2: "red", 10: "green", 100: "blue", 1000: "black"}
    x = []
    for r in repeatitions:
        print("Run for {} repeatitions...".format(r))
        fc = FixedCounter(file, fixed_prob, r)
        f_chars = fc.run()
        
        sorted_f_chars = dict(sorted(f_chars.items(), key=lambda item: sum(item[1])/len(item[1]), reverse=True))

        top_f_chars = {}
        for char in list(sorted_f_chars.keys())[:10]:
            top_f_chars[char] = sorted_f_chars[char]        
        if r == 2:
            x = list(top_f_chars.keys())

        fc_y = [ np.mean(np.array(top_f_chars[c])/fixed_prob) / sorted_e_chars[c]*100 for c in top_f_chars]

        plt.plot(x, fc_y, color=repeatitions[r], label="rep="+str(r))

    plt.legend()
    plt.show() 

def testDecreasing():
    repeatitions = {2: "red", 10: "green", 100: "blue", 1000: "black"}
    x = []
    for r in repeatitions:
        print("Run for {} repeatitions...".format(r))
        dc = DecreasingCounter(file, r)
        d_chars = dc.run()
        
        sorted_d_chars = dict(sorted(d_chars.items(), key=lambda item: sum(item[1])/len(item[1]), reverse=True))

        top_d_chars = {}
        for char in list(sorted_d_chars.keys())[:10]:
            top_d_chars[char] = sorted_d_chars[char]        
        if r == 2:
            x = list(top_d_chars.keys())

        fc_y = [ (np.mean((2**np.array(top_d_chars[c])) - 1)) / sorted_e_chars[c]*100 for c in top_d_chars]

        plt.plot(x, fc_y, color=repeatitions[r], label="rep="+str(r))

    plt.legend()
    plt.show() 

if __name__ == "__main__":
    fixed_prob = 1/4
    file = None
    _type = None

    try:
        file = sys.argv[1]
        _type = sys.argv[2]
    except Exception as err:
        print("Usage: python3 src/test_repeatitions.py texts/<file> <type of counter(fixed or decreasing)>")
        sys.exit(2)
    
    begin = time.time()
    file = open(file, "r")
    file = file.read()
    # Exact Counter
    ec = ExactCounter(file)
    e_chars = ec.run()
    #ec.printResults(chars)
    sorted_e_chars = dict(sorted(e_chars.items(), key=lambda item: item[1], reverse=True))

    #Test
    if _type == "fixed":
        testFixed()
    elif _type == "decreasing":
        testDecreasing()
    else:
        print("Usage: python3 src/test_repeatitions.py texts/<file> <type of counter(fixed or decreasing)>")

    print("Time: {}".format(round(time.time()-begin, 2)))