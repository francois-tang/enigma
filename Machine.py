import string

alphabet_initial = list(string.ascii_lowercase)

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
    def __init__(self, position_depart, alphabet):
        self.position_depart = position_depart
        self.alphabet = alphabet


def decale_alphabet(alphabet):
    alphabet = alphabet[1:] + [alphabet[0]]
    return alphabet

def creation_rotor(position_depart):
    rotor = Rotor(position_depart, alphabet_initial[position_depart-1:] + alphabet_initial[:position_depart+1]) #car a = 0, etc. donc on décale
    print(rotor.position_depart, rotor.alphabet)
    return rotor.position_depart, rotor.alphabet

def rotor_tourne(position_depart, alphabet):
    rotor = Rotor(position_depart, decale_alphabet(alphabet))
    print(rotor.position_depart, rotor.alphabet)
    return rotor.position_depart, rotor.alphabet

# MAIN
rotor1 = creation_rotor(6)
print(rotor1)
rotor1 = rotor_tourne(rotor1[0], rotor1[1])
print(rotor1)