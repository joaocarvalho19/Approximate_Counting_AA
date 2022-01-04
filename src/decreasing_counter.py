import math
import random
import numpy as np

class DecreasingCounter:
    def __init__(self, file, repeatitions):
        self.file = file
        self.number_chars = 0
        self.repeatitions = repeatitions    


    def run(self):

        result_list = {}           # char: [sum of counts, num of counts]
        for i in range(self.repeatitions):
            letters = self.counter(self.file)
            for char in letters:
                if char not in result_list:
                    result_list[char] = [letters[char]]
                else:
                    result_list[char].append(letters[char])

        return result_list


    def counter(self, file):
        letters = {}
        for char in file:
            if char.isalpha():
                #self.number_chars += 1
                char = char.upper()
                if char not in letters.keys():
                    letters[char] = 0
                    prob = 1 / (2**0)   # k = 0
                    if self.choice(prob):
                        letters[char] = 1
                else:
                    prob = 1 / (2**letters[char])   #k = letters[char]
                    if self.choice(prob):
                        letters[char] += 1
        
        return letters
        
        
    def choice(self, prob):
        return random.choices([1,0], cum_weights=(prob, 1.00)) == [1]

    def printResults(self, letters):
        for c in letters:
            print("Char {} | Freq {} ".format(c, letters[c]))

    def simpleAnalisysCounter(self,sorted_chars, sorted_e_chars):
        print("|  {:<4}  --| {:<5} | {:<4} | {:<5} | {:<4} | {:<4} |".format("Char", "EC", "DC Est. Counter","DC" ,"Mean Est. DC" ,"Mean Acc"))
        for c in sorted_chars:
            exact_value = sorted_e_chars[c]
            counter_value = round(np.mean(np.array(sorted_chars[c])),1)
            f_expected__values = (2**np.array(sorted_chars[c])) - 1
            est_counter = math.floor(math.log2(exact_value + 1))

            mean_value = round(np.mean(f_expected__values))
            abs_devs = np.absolute(f_expected__values - mean_value)
            acc = round(mean_value / exact_value * 100,2)


            print("|  {:<4}  --| {:<5} | {:<15} | {:<5} | {:<12} | {:<8} |".format(c ,exact_value, est_counter ,counter_value,mean_value, acc))