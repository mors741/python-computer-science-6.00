class Person(object):
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_name_letter(self):
        for letter in self.name:
            yield chr(ord(letter) +1)

p1 = Person("Zhenya")
