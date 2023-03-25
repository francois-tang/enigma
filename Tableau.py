import string

alphabet = list(string.ascii_lowercase)

class Tableau:
    def __init__(self, couple_entree, couple_sortie):
        self.couple_entree = couple_entree
        self.couple_sortie = couple_sortie

def test():      
    test = Tableau(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'])
    couple1 = test.couple_entree
    couple2 = test.couple_sortie
    print(couple1)
    print(couple2)

test()