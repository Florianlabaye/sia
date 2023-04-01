""" 
 Définition de la classe #utilisateur 

- Pseudo
- Date de création
- Wallet associé
- Transactions
- XP
- Niveau d'habilitation
- Collection de cartes

"""

from time import gmtime, strftime
from carte import Carte

class Utilisateur:
    def __init__(self, adresse_wallet) -> None:
        self.pseudo = ""
        self.date_creation = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        self.adresse_wallet = adresse_wallet
        self.transactions = []
        self.xp = 0
        self.niveau_habilitation = 0
        self.collection = []

    def set_pseudo(self, pseudo):
        self.pseudo = pseudo
    
    def set_wallet(self, wallet):
        self.adresse_wallet = wallet

    def creer_carte(self, titre, description, localisation):
        carte = Carte(titre, description, localisation, self)
        self.collection.append(carte)

    def decrire_collection(self):
        print(f"Collection de {self.pseudo} :")
        for carte in self.collection:
            print(carte)

    def vendre_carte(self, carte, utilisateur, prix):
        self.collection.remove(carte)
        utilisateur.collection.append(carte)
        self.transactions.append(f"Vente de {carte.titre} à {utilisateur.pseudo} pour {prix} tokens le {strftime('%a, %d %b %Y %H:%M:%S +0000', gmtime())}")

        
        