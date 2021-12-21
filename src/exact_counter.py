class ExactCounter:
    def __init__(self, file):
        self.file = file
        self.number_chars = 0

    def run(self):
        file = open(self.file, "r")
        file = file.read()

        letters = {}
        for char in file:
            if char.isascii():
                self.number_chars += 1
                if char not in letters.keys():
                    letters[char] = 1
                else:
                    letters[char] += 1
        
        result = dict(sorted(letters.items()))
        return result
    
    def printResults(self, letters):
        for c in letters:
            print("Char {} | Freq {}  --  {}%".format(c, letters[c], round(letters[c]/self.number_chars * 100, 4)))