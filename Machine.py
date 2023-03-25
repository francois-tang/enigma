import Rotor
import Tableau

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



    #r = Rotor.test()
    #print(r)