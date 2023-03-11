import string
print(string.ascii_uppercase)


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    def __init__ (self):
        super().__init__('En', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self._letters_num = len(self.letters)

    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num (self):
        return self._letters_num

    @staticmethod
    def primer():
        return "In the last task, I was inspired by Quake 3"

