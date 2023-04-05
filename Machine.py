import string

alphabet = list(string.ascii_lowercase)

class Machine:
    def __init__(self, rotor, reflecteur, tableau):
        self.rotor = rotor
        self.reflecteur = reflecteur
        self.tableau = tableau

    phrase_a_coder = input("Entrez la phrase à coder :")
    phrase_a_coder = phrase_a_coder.lower()
    print("La phrase à coder est : " + phrase_a_coder)

    caractres_phrase_a_coder = list(phrase_a_coder)
    print(caractres_phrase_a_coder)


class Rotor:
    def __init__(self, positionDepart, alphabet):
        self.positionDepart = positionDepart
        self.alphabet = alphabet


def decale_alphabet(alphabet):
    alphabet = alphabet[1:] + [alphabet[0]]
    return alphabet

def creationRotor(positionDepart):
    rotor = Rotor(positionDepart, alphabet)
    print(rotor.positionDepart, rotor.alphabet)
    return rotor.positionDepart, rotor.alphabet

def newRotor(positionDepart, alphabet):
    rotor = Rotor(positionDepart, decale_alphabet(alphabet))
    print(rotor.positionDepart, rotor.alphabet)
    return rotor.positionDepart, rotor.alphabet

# MAIN
rotor1 = creationRotor(1)
print(rotor1)
rotor1 = newRotor(rotor1[0], rotor1[1])
print(rotor1)
