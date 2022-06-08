"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """find a random word from given file"""

    def __init__(self, path):
        self.path = path
        file = open(self.path)
        self.count = sum(1 for line in file)
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

class SpecialWordFinder(WordFinder):
    """finds random word from file, ignoring blank lines and lines starting with "#"."""

    def random(self):
        f = open(self.path)
        word_list = list(f)
        for atmp in range(100):
            option = choice(word_list)
            if not option == "\n" and not option.startswith("#"):
                return option.rstrip('\n')
