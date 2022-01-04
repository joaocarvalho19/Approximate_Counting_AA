from fixed_counter import FixedCounter
from exact_counter import ExactCounter
from decreasing_counter import DecreasingCounter
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
import time


def barPlot():
    # set width of bars
    barWidth = 0.25

    # set heights of bars
    bars1 = list(sorted_e_chars.values())[:5]
    bars2 = [round(np.mean(np.array(sorted_f_chars[c]) / fixed_prob)) for c in sorted_f_chars][:5]
    bars3 = [round(np.mean((2**np.array(sorted_d_chars[c])) - 1)) for c in sorted_d_chars][:5]


    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    # Make the plot
    plt.bar(r1, bars1, color='red', width=barWidth, edgecolor='black', label='Exact')
    plt.bar(r2, bars2, color='blue', width=barWidth, edgecolor='black', label='Fixed')
    plt.bar(r3, bars3, color='green', width=barWidth, edgecolor='black', label='Decreasing')

    # Add xticks on the middle of the group bars
    plt.xlabel('group', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], list(sorted_e_chars.keys())[:5])

    # Create legend & Show graphic
    plt.legend()
    plt.show()




def bothTable():
    print("| {:<4} --| {:<5} | {:<5} | {:<5} | {:<5} | {:<5} |".format("Char", "EC", "FC", "Acc FC", "DC", "Acc DC"))
    for c in sorted_e_chars:
        exact_value = sorted_e_chars[c]
        if c in sorted_f_chars:
            f_expected__values = np.array(sorted_f_chars[c]) / fixed_prob
            f_mean_value = round(np.mean(f_expected__values))
            f_value = round(np.mean(np.array(sorted_f_chars[c])))
            f_acc = round(f_mean_value / exact_value * 100,2)
            if c in sorted_d_chars:
                d_expected__values = (2**np.array(sorted_d_chars[c])) - 1
                d_mean_value = round(np.mean(d_expected__values))
                d_value = round(np.mean(np.array(sorted_d_chars[c])))
                d_acc = round(d_mean_value / exact_value * 100,2)
                print("| {:<4} --| {:<5} | {:<5} | {:<6} | {:<5} | {:<6} |".format(c, exact_value, f_value, f_acc, d_value, d_acc))



def analisysCounter(sorted_chars, _type):
    print("|  {:<4}  --| {:<5} | {:<4} | {:<4} | {:<4} | {:<18} | {:<19} | {:<19} |".format("Char","EC" ,"Mean FC" ,"Mean Dev" ,"Mean Acc","Abs/Rel Max Error", "Abs/Rel Min Error", "Abs/Rel Mean Error"))
    for c in sorted_chars:
        exact_value = sorted_e_chars[c]
        if _type == "d":
            f_expected__values = (2**np.array(sorted_chars[c])) - 1
        elif _type == "f":
            f_expected__values = np.array(sorted_chars[c]) / fixed_prob
        else:
            print("ERROR!")
            return

        mean_value = round(np.mean(f_expected__values))
        abs_devs = np.absolute(f_expected__values - mean_value)
        mean_dev = round(np.mean(abs_devs),2)
        acc = round(mean_value / exact_value * 100,2)

        abs_errors = np.absolute(f_expected__values-exact_value)
        abs_max_err = round(np.max(abs_errors))
        abs_min_err = round(np.min(abs_errors))
        abs_mean_err = round(np.mean(abs_errors),1)

        rel_max_err = round(abs_max_err / exact_value*100,1)
        rel_min_err = round(abs_min_err / exact_value*100,1)
        rel_mean_err = round(abs_mean_err / exact_value*100,1)

        print("|  {:<4}  --| {:<5} | {:<7} | {:<8} | {:<8} | {:<8} / ~{:<6} | {:<10} / ~{:<5} | {:<10} / ~{:<5} |".format(c ,sorted_e_chars[c] ,mean_value ,mean_dev , acc,abs_max_err, rel_max_err, abs_min_err, rel_min_err, abs_mean_err, rel_mean_err))



if __name__ == "__main__":
    fixed_prob = 1/4
    repeatitions = 100
    file = None

    try:
        file = sys.argv[1]
        repeatitions = int(sys.argv[2])
    except Exception as err:
        print("Usage: python3 src/main.py texts/<file> <num repeatitions>")
        sys.exit(2)
    
    begin = time.time()
    file = open(file, "r")
    file = file.read()

    # Exact Counter
    ec = ExactCounter(file)
    e_chars = ec.run()
    #ec.printResults(chars)
    sorted_e_chars = dict(sorted(e_chars.items(), key=lambda item: item[1], reverse=True))
    print("Text length: {}".format(ec.getTextLen()))

    

    # Fixed Prob Counter
    fc = FixedCounter(file, fixed_prob, repeatitions)
    f_chars = fc.run()
    #fc.printResults(chars)
    sorted_f_chars = dict(sorted(f_chars.items(), key=lambda item: sum(item[1])/len(item[1]), reverse=True))

    # Decreasing Prob Counter
    dc = DecreasingCounter(file, repeatitions)
    d_chars = dc.run()  
    #dc.printResults(chars)
    sorted_d_chars = dict(sorted(d_chars.items(), key=lambda item: sum(item[1])/len(item[1]), reverse=True))
    
    # Results
    bothTable()
    
    # Comparisons
    #analisysCounter(sorted_d_chars, "d")
    #fc.simpleAnalisysCounter(sorted_f_chars, sorted_e_chars)
    #dc.simpleAnalisysCounter(sorted_d_chars, sorted_e_chars)
    
    barPlot()
    print("Time: {}".format(round(time.time()-begin, 2)))