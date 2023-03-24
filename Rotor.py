import string

alphabet = list(string.ascii_lowercase)

class Rotor:
    def __init__(self, positionDepart, alphabet):
        self.positionDepart = positionDepart
        self.alphabet = alphabet


test = Rotor(1, alphabet)
print(test.positionDepart, test.alphabet)