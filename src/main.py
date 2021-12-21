from fixed_counter import FixedCounter
from exact_counter import ExactCounter
from decreasing_counter import DecreasingCounter
import sys


if __name__ == "__main__":
    fixed_prob = 1/4
    repeatitions = 1000
    file = None

    try:
        file = sys.argv[1]
    except Exception as err:
        print("Usage: python3 src/main.py texts/<file>")
        sys.exit(2)

    # Exact Counter
    ec = ExactCounter(file)
    e_chars = ec.run()
    #ec.printResults(chars)

    # Fixed Prob Counter
    fc = FixedCounter(file, fixed_prob, repeatitions)
    f_chars = fc.run()
    #fc.printResults(chars)

    # Fixed Prob Counter
    dc = DecreasingCounter(file, repeatitions)
    d_chars = dc.run()
    #dc.printResults(chars)

    # Results
    for c in e_chars:
        if c in f_chars:
            if c in d_chars:
                print("Char - {}\n     | Exact Freq: {}\n     | Fixed Freq: {}\n     | Decreasing Freq: {}".format(c, e_chars[c], int(round(f_chars[c][0]/f_chars[c][1])), int(round(d_chars[c][0]/d_chars[c][1]))))
            else:
                print("Char - {}\n     | Exact Freq: {}\n     | Fixed Freq: {}\n     | Decreasing Freq: {}".format(c, e_chars[c], int(round(f_chars[c][0]/f_chars[c][1])), None))

        else:
            print("Char - {}\n     | Exact Freq: {}\n     | Fixed Freq: {}\n     | Decreasing Freq: {}".format(c, e_chars[c], None, None))