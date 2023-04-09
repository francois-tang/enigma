# Enigma - Université Paris Cité - Cryptographie

## Auteur
* **TANG François** - M2 MIAGE FA - 2022-2023

## Responsable
* **M. Kreshnik MUSARAJ** - Professeur module "Cryptographie & Blockchain"

## Version de Python
Python 3.10.9

## Documentation
### Lancer le projet
:arrow_forward: Il lancer un terminal de commande, puis se mettre à l'emplacement où on veut récupérer le projet en tapant :
```
cd [l'emplacement du projet]
```

:arrow_forward: Puis taper :
```
git clone https://github.com/francois-tang/enigma.git
```

:arrow_forward: Et pour lancer le projet :
```
python Machine.py
```

### Les inputs demandés
1. **"Entrez la phrase à coder :"**
    * Cela peut être tous les caractères de l'alphabet sans les accents ainsi que les caractères spéciaux comme " !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~".
    * Par exemple **"azerty azerty"**.
1. **"Entrez 10 caractères uniques qui seront couplés avec les 10 suivants :"**
    * Il faut rentrer les 10 premiers caractères qui seront couplés avec les suivants.
    * Par exemple : **"abcdefghij"**.
1. **"Entrez 10 caractères uniques qui seront couplés avec les 10 précédents :"**
    * Il faut rentrer les 10 caractères qui seront couplés avec les précédents.
    * Par exemple : **"klmnopqrst"**.
    * Ainsi a est couplé avec k et inversement, etc.
1. **"Entrez la position du rotor 1 :"**
    * Il faut entrer la position de départ du rotor 1. a étant la position 1.
    * Par exemple : **"4"**.
1. **"Entrez la position du rotor 2 :"**
    * Il faut entrer la position de départ du rotor 2. a étant la position 1.
    * Par exemple : **"10"**.
1. **"Entrez la position du rotor 3 :"**
    * Il faut entrer la position de départ du rotor 2. a étant la position 1.
    * Par exemple : **"6"**.
1. **"Entrez le déclencheur du rotor 2 :"**
    * Il faut entrer le déclencheur du rotor 2, c'est-à-dire à quelle lettre du rotor précédent il va tourner d'un cran = c'est le trigger.
    * Par exemple : **"f"**.
1. **"Entrez le déclencheur du rotor 3 :"**
    * Il faut entrer le déclencheur du rotor 3, c'est-à-dire à quelle lettre du rotor précédent il va tourner d'un cran = c'est le trigger.
    * Par exemple : **"d"**.

### Résultats
:arrow_forward: L'intégralité du programme tourne avec les étapes détaillées pour chaque rotor, s'il tourne ou non, que se passe-t-il dans le réflecteur et dans le couplage.
:arrow_forward: Le logiciel retourne le mot initial à coder et le résultat du codage.