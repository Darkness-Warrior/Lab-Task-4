import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        return self.letters

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)
        self._letters_num = len(self.letters)

    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num(self):
        return self._letters_num

    @staticmethod
    def primer():
        return "In the last task, I was inspired by Quake 3"


eng_alphabet = EngAlphabet()
print(eng_alphabet.print())
print(eng_alphabet.letters_num())
print(eng_alphabet.is_en_letter('F'))
print(eng_alphabet.is_en_letter('Щ'))
print(EngAlphabet.primer())

