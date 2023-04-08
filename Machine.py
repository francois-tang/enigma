import string

# REFLECTEUR

alphabet_initial = list(string.ascii_lowercase)
alphabet_initial_inverse = alphabet_initial[::-1] #inverse les caractères a devient z, etc.


# CLASS MACHINE

class Machine:
    def __init__(self, rotor, reflecteur, tableau):
        self.rotor = rotor
        self.reflecteur = reflecteur
        self.tableau = tableau


# INPUT PHRASE A CODER

## VERIFICATION DE L'INPUT
def est_valide(chaine):
    for caractere in chaine:
        if caractere not in string.ascii_lowercase:
            return False
    return True

phrase_a_coder = input("Entrez la phrase à coder :")
phrase_a_coder = phrase_a_coder.lower()

if est_valide(phrase_a_coder):
    print("La phrase à coder est :", phrase_a_coder)
else:
    while not est_valide(phrase_a_coder):
        phrase_a_coder = input("Entrez à nouveau la phrase à coder qui doit être composée uniquement que de lettres :")
        phrase_a_coder = phrase_a_coder.lower()
    print("La phrase à coder est :", phrase_a_coder)

## LES CARACTERES DE LA PHRASE A CODER
caractres_phrase_a_coder = list(phrase_a_coder)
print(caractres_phrase_a_coder)


# COUPLAGE

def est_longueur_dix(chaine):
    return len(chaine) == 10

def caracteres_uniques(chaine): #Si le caractère est déjà dans la liste d'occurence, alors retourne False donc pas unique, sinon elle l'ajoute dans la liste d'occurences
    occurrences = {}
    for caractere in chaine:
        if caractere in occurrences:
            return False
        else:
            occurrences[caractere] = 1
    return True


while True:
    # PREMIER COUPLAGE
    premier_couple = input("Entrez 10 caractères uniques qui seront couplés avec les 10 suivants :")
    premier_couple = premier_couple.lower()

    if est_valide(premier_couple) and est_longueur_dix(premier_couple):
        premier_couple = list(str(premier_couple))
    else:
        continue

    # DEUXIEME COUPLAGE
    deuxieme_couple = input("Entrez 10 caractères uniques qui seront couplés avec les 10 précédents :")
    deuxieme_couple = deuxieme_couple.lower()

    if est_valide(deuxieme_couple) and est_longueur_dix(deuxieme_couple):
        deuxieme_couple = list(str(deuxieme_couple))
    else:
        continue
    
     # VERIFICATION DES COUPLES
    couple_initial = premier_couple + deuxieme_couple
    couple_initial_inverse = deuxieme_couple + premier_couple

    if caracteres_uniques(couple_initial) and caracteres_uniques(couple_initial_inverse):
        break
    print("Les caractères ne sont pas uniques.")

print("Les 10 premiers caractères sont :", premier_couple)
print("Les 10 caractères suivants sont :", deuxieme_couple)
print(couple_initial)
print(couple_initial_inverse)


# CLASS ROTOR

class Rotor:
    def __init__(self, position_depart, alphabet):
        self.position_depart = position_depart
        self.alphabet = alphabet


def decale_alphabet(alphabet):
    alphabet = alphabet[1:] + [alphabet[0]]
    return alphabet

def creation_rotor(position_depart):
    rotor = Rotor(position_depart, alphabet_initial[position_depart-1:] + alphabet_initial[:position_depart+1]) #car a = 0, etc. donc on décale
    return rotor.position_depart, rotor.alphabet

def rotor_tourne(position_depart, alphabet):
    rotor = Rotor(position_depart, decale_alphabet(alphabet))
    print("Le rotor tourne")
    return rotor.position_depart, rotor.alphabet

def transforme_caractere(caractere, alphabet_initial, rotor_alphabet):
    index = alphabet_initial.index(caractere)
    return rotor_alphabet[index]


# DEMANDE UTILISATEUR POSITION ROTOR 1 à 3

position_rotor1 = input("Entrez la position du rotor 1 :")
if position_rotor1.isnumeric() == True:
    print("La position du rotor 1 est : " + position_rotor1)
else:
    while position_rotor1.isnumeric() == False:
        position_rotor1 = input("Ce n'est pas un nombre. Entrez à nouveau la position du rotor 1 entre 1 et 26 :")
        print("La position du rotor 1 est : " + position_rotor1)


position_rotor2 = input("Entrez la position du rotor 2 :")
if position_rotor2.isnumeric() == True:
    print("La position du rotor 2 est : " + position_rotor2)
else:
    while position_rotor2.isnumeric() == False:
        position_rotor2 = input("Ce n'est pas un nombre. Entrez à nouveau la position du rotor 2 entre 1 et 26 :")
        print("La position du rotor 2 est : " + position_rotor2)


position_rotor3 = input("Entrez la position du rotor 3 :")
if position_rotor3.isnumeric() == True:
    print("La position du rotor 3 est : " + position_rotor3)
else:
    while position_rotor3.isnumeric() == False:
        position_rotor3 = input("Ce n'est pas un nombre. Entrez à nouveau la position du rotor 3 entre 1 et 26 :")
        print("La position du rotor 3 est : " + position_rotor3)


# DEMANDE UTILISATEUR DECLENCHEUR TOURNER ROTOR 1 à 3
"""
position_rotor1 = input("Entrez la position du rotor 1 :")
if position_rotor1.isnumeric() == True:
    print("La position du rotor 1 est : " + position_rotor1)
else:
    while position_rotor1.isnumeric() == False:
        position_rotor1 = input("Ce n'est pas un nombre. Entrez à nouveau la position du rotor 1 entre 1 et 26 :")
        print("La position du rotor 1 est : " + position_rotor1)


position_rotor2 = input("Entrez la position du rotor 2 :")
if position_rotor2.isnumeric() == True:
    print("La position du rotor 2 est : " + position_rotor2)
else:
    while position_rotor2.isnumeric() == False:
        position_rotor2 = input("Ce n'est pas un nombre. Entrez à nouveau la position du rotor 2 entre 1 et 26 :")
        print("La position du rotor 2 est : " + position_rotor2)


position_rotor3 = input("Entrez la position du rotor 3 :")
if position_rotor3.isnumeric() == True:
    print("La position du rotor 3 est : " + position_rotor3)
else:
    while position_rotor3.isnumeric() == False:
        position_rotor3 = input("Ce n'est pas un nombre. Entrez à nouveau la position du rotor 3 entre 1 et 26 :")
        print("La position du rotor 3 est : " + position_rotor3)
"""

# MAIN

## CREATION ROTOR 1
rotor1 = creation_rotor(int(position_rotor1))
print("Le rotor 1 est créé comme suit : ", rotor1[1])

## CREATION ROTOR 2
rotor2 = creation_rotor(int(position_rotor2))
print("Le rotor 2 est créé comme suit : ", rotor2[1])

## CREATION ROTOR 3
rotor3 = creation_rotor(int(position_rotor3))
print("Le rotor 3 est créé comme suit : ", rotor3[1])

## PASSAGE LETTRE DANS ROTOR 1
rotor1_alphabet = rotor1[1]
premier_caractere = caractres_phrase_a_coder[0]
caractere_transforme = transforme_caractere(premier_caractere, alphabet_initial, rotor1_alphabet)
print("Le caractère transformé au rotor 1 est :", caractere_transforme)

rotor1 = rotor_tourne(rotor1[0], rotor1[1])
rotor1_alphabet = rotor1[1]
print(rotor1_alphabet)

## PASSAGE LETTRE DANS ROTOR 2
rotor2_alphabet = rotor2[1]
caractere_transforme = transforme_caractere(caractere_transforme, alphabet_initial, rotor2_alphabet)
print("Le caractère transformé au rotor 2 est :", caractere_transforme)

## PASSAGE LETTRE DANS ROTOR 3
rotor3_alphabet = rotor3[1]
caractere_transforme = transforme_caractere(caractere_transforme, alphabet_initial, rotor3_alphabet)
print("Le caractère transformé au rotor 3 est :", caractere_transforme)


# REFLECTEUR
caractere_transforme = transforme_caractere(caractere_transforme, alphabet_initial, alphabet_initial_inverse)
print("Le caractère sorti du réflecteur est :", caractere_transforme)


## ROTOR 3 RETOUR
print("La position du rotor 3 est :", rotor3_alphabet)
caractere_transforme = transforme_caractere(caractere_transforme, alphabet_initial, rotor3_alphabet)
print("Le caractère transformé au rotor 3 retour est :", caractere_transforme)

## ROTOR 2 RETOUR
print("La position du rotor 2 est :", rotor2_alphabet)
caractere_transforme = transforme_caractere(caractere_transforme, alphabet_initial, rotor2_alphabet)
print("Le caractère transformé au rotor 2 retour est :", caractere_transforme)

## ROTOR 1 RETOUR
print("La position du rotor 1 est :", rotor1_alphabet)
caractere_transforme = transforme_caractere(caractere_transforme, alphabet_initial, rotor1_alphabet)
print("Le caractère transformé au rotor 1 retour est :", caractere_transforme)