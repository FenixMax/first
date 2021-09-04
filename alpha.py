import string
class Alphabet:
    def __init__(self,lang="En",letters=string.ascii_uppercase):
        self.lang=lang
        self.letters=letters
    def print(self):
        print(self.letters)
    def letters_num(self):
        num=len(self.letters)
        print(num)
class EngAlphabet(Alphabet):
    def __init__(self,lang="En",letters=string.ascii_uppercase):
        super().__init__()
        self.__letters_num=len(letters)

    def is_en_letter(self, bukv):
        if bukv in self.letters:
            print(f'буква {bukv} относится к алфавиту')
        else:
            print(f'буква {bukv} не относится к алфавиту')
    def letters_num(self):
        return self.__letters_num
    @staticmethod
    def example(text):
        return text
if __name__=="__main__":
    a=EngAlphabet()
    a.print()
    print(a.letters_num())
    a.is_en_letter("F")
    a.is_en_letter("Щ")
    print(a.example('Have a nice day!!!'))