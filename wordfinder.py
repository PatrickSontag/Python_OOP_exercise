"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    ...

    def __init__(self, path):
        self.path = path
        self.file = open(self.path)
        self.count = sum(1 for line in self.file)
        print(self.count, "words read")

    def random(self):
        "finds random word"
        f = open(self.path)
        word_list = list(f)
        return choice(word_list).rstrip('\n')
        # print(choice(word_list))

    # def random(self):
    #     "finds random word"
    #     f = open("words.txt")
    #     word_list = list(f)
    #     print(choice(word_list))

# class SpeicalWordFinder(WordFinder):

