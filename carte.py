""" Définition de la classe #carte 

- Titre
- Type (plage, grotte, restaurant, rue, monument)
- Descriptions
- Localisation (GPS, Pays, Ville)
- Date de création
- Dernier échange
- Prix de la dernière transaction
- Photo (lien)
- Propriétaire actuel
- Propriétaires précédents
- Wallet associé
- Transactions
- Commentaires
- Prix de vente
- Score
- Niveau d'habilitation

 """

from time import gmtime, strftime
from emission_nft import *

class Carte:
    def __init__(self, titre, description, localisation, proprietaire) -> None:
        self.titre = titre
        self.type = ""
        self.description = description
        self.localisation = localisation
        self.date_creation = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        self.dernier_echange = "Pas encore eu d'échange"
        self.prix_derniere_transaction = "Pas encore eu de transaction"
        self.photo = "Pas encore de photo"
        self.nb_de_transactions = 0
        self.proprietaire = proprietaire
        self.commentaires = []
        self.score = 0
        self.niveau_habilitation = 0

    def scorer(self):
        pass

    def set_photo(self, lien):
        self.photo = lien
    
    def tokeniser(self, sc_address):
        smart_contract_mint_request(self.proprietaire, sc_address, self.titre, self.description, self.photo, self.localisation )

    def __str__(self) -> str:
        return f"Carte: {self.titre}, {self.description}"
    
