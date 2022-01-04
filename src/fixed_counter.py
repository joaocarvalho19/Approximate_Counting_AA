import random
import numpy as np

class FixedCounter:
    def __init__(self, file, prob, repeatitions):
        self.file = file
        self.number_chars = 0
        self.prob = prob
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
                char = char.upper()
                if char not in letters.keys():
                    letters[char] = 0
                    if self.choice():
                        letters[char] = 1
                else:
                    if self.choice():
                        letters[char] += 1
        
        return letters

    
    def choice(self):
        return random.choices([1,0], cum_weights=(self.prob, 1.00)) == [1]


    def printResults(self, letters):
        for c in letters:
            print("Char {} | Freq {}  --  {}%".format(c, letters[c], round(letters[c]/self.number_chars * 100, 4)))

    def simpleAnalisysCounter(self,sorted_chars, sorted_e_chars):
        print("|  {:<4}  --| {:<5} | {:<4} | {:<7} | {:<4} | {:<4} |".format("Char", "EC", "FC Est. Counter","FC" ,"Mean Est. FC" ,"Mean Acc"))
        for c in sorted_chars:
            exact_value = sorted_e_chars[c]
            counter_value = round(np.mean(np.array(sorted_chars[c])),1)
            f_expected__values = np.array(sorted_chars[c]) / self.prob
            est_counter = exact_value * self.prob

            mean_value = round(np.mean(f_expected__values))
            abs_devs = np.absolute(f_expected__values - mean_value)
            acc = round(mean_value / exact_value * 100,2)


            print("|  {:<4}  --| {:<5} | {:<15} | {:<7} | {:<12} | {:<8} |".format(c ,exact_value, est_counter ,counter_value,mean_value, acc))