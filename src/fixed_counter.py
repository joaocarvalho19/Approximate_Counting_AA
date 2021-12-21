import random

class FixedCounter:
    def __init__(self, file, prob, repeatitions):
        self.file = file
        self.number_chars = 0
        self.prob = prob
        self.repeatitions = repeatitions


    def run(self):
        file = open(self.file, "r")
        file = file.read()

        result_list = {}           # char: [sum of counts, num of counts]
        for i in range(self.repeatitions):
            letters = self.counter(file)
            for char in letters:
                if char not in result_list:
                    result_list[char] = [letters[char], 1]
                else:
                    current_sum = result_list[char][0]
                    current_num = result_list[char][1]
                    result_list[char] = [current_sum + letters[char], current_num + 1]
        

        return dict(sorted(result_list.items()))


    def counter(self, file):
        letters = {}
        for char in file:
            if char.isascii():
                #self.number_chars += 1
                if char not in letters.keys():
                    if self.choice():
                        letters[char] = 1
                else:
                    if self.choice():
                        letters[char] += 1
        
        return letters

    
    def choice(self):
        if random.choices([1,0], cum_weights=(self.prob, 1.00)) == [1]:
            return True
        else:
            return False


        """mean = 0
        for r in result:
            mean += r*result[r]
            print("Value: {} Freq: {}%".format(r, round(result[r]/repeatitions*100, 2)))

        print("Mean counter value: {}".format(mean/repeatitions))"""

    def printResults(self, letters):
        for c in letters:
            print("Char {} | Freq {}  --  {}%".format(c, letters[c], round(letters[c]/self.number_chars * 100, 4)))