class RabinKarp:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.text_length = len(text)
        self.pattern_length = len(pattern)
        self.prime = 101  # Prime number for hashing
        self.base = 256   # Number of characters in the input alphabet
        self.text_hash = 0
        self.pattern_hash = 0
        self.h = 1

    def create_hash(self, string, length):
        hash_value = 0
        for i in range(length):
            hash_value = (hash_value * self.base + ord(string[i])) % self.prime
        return hash_value

    def check_similarity(self):
        overlap = 0
        for i in range(self.pattern_length - 1):
            self.h = (self.h * self.base) % self.prime

        self.pattern_hash = self.create_hash(self.pattern, self.pattern_length)
        self.text_hash = self.create_hash(self.text, self.pattern_length)

        for i in range(self.text_length - self.pattern_length + 1):
            if self.pattern_hash == self.text_hash:
                if self.text[i:i + self.pattern_length] == self.pattern:
                    overlap += self.pattern_length
            if i < self.text_length - self.pattern_length:
                self.text_hash = (self.base * (self.text_hash - ord(self.text[i]) * self.h) + ord(
                    self.text[i + self.pattern_length])) % self.prime
                if self.text_hash < 0:
                    self.text_hash += self.prime

        plagiarism_rate = (overlap / self.text_length) * 100
        return plagiarism_rate

def detect_plagiarism(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()
    
    plagiarism_detector = RabinKarp(text1, text2)
    plagiarism_rate = plagiarism_detector.check_similarity()
    if plagiarism_rate > 0:
        print("Plagiarism detected!")
        print("Plagiarism rate: {:.2f}%".format(plagiarism_rate))
    else:
        print("No plagiarism detected.")

# Example usage:
file1 = "file1.txt"
file2 = "file2.txt"
detect_plagiarism(file1, file2)
