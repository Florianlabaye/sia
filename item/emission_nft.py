"""

import smartpy as sp

FA2 = sp.io.import_script_from_url(
    "https://smartpy.io/templates/fa2_lib.py"
)

def make_metadata(title, description, photo_link, localisation):
    #Helper function to build metadata JSON bytes values.
    return sp.big_map(l={"titre": sp.utils.bytes_of_string(title),"description": sp.utils.bytes_of_string(description),"photo_link": sp.utils.bytes_of_string(photo_link),"localisation": sp.utils.bytes_of_string(localisation),})

class NFT(FA2.Fa2Nft):
    @sp.entry_point
    def mint(self, owner, token_info):
        token_id = self.data.last_token_id
        self.data.ledger[token_id] = owner
        self.data.token_metadata[token_id] = sp.record(token_id = token_id, token_info = token_info)
        self.data.last_token_id += 1
 
@sp.add_test(name = "Test NFT Emission ")
def test():
    sc = sp.test_scenario()
    nft = NFT(metadata = make_metadata("Titre", "Desc", "Link", "Localisation"))
    sc += nft

    bob = sp.address("tz1WXtiDgVUn7MVuccvjhE1guH61S9kqLmbe")
    alice = sp.address("tz1PZY3agTGshV48bcYVbuz88G3mfL8wgm1p")

    sc.show(sp.record(alice=alice, bob=bob))

    sc.h2("Mint")

    # Alice mint un NFT
    nft.mint(owner=alice, token_info=sp.map(l={"titre": sp.utils.bytes_of_string("plage"),"description": sp.utils.bytes_of_string("crique romaine"),"photo_link": sp.utils.bytes_of_string("https://www.envol-espace.fr/photos/barcelone_et_catalogne/la_catalogne_romaine/5762/cirque_romain_tarragone.jpg"),"localisation": sp.utils.bytes_of_string("tarragone"),}) )
    sc.verify(nft.data.ledger[0] == alice)

    sc.h2("Transfer")
    nft.transfer(
        [
            sp.record( from_=alice, txs=[sp.record(to_=bob, amount=1, token_id=0)])
        ]
    ).run(sender=alice)

    sc.verify(nft.data.ledger[0] == bob)

"""

""""Adresse du smart contract sur GhostNet -> KT1MArMCMVWohqsuksyAtCCi2TGshDpp4G5F"""
"""Adresse du wallet d'alice -> tz1PZY3agTGshV48bcYVbuz88G3mfL8wgm1p"""
"""Adresse du wallet de bob -> tz1WXtiDgVUn7MVuccvjhE1guH61S9kqLmbe"""

import os

def string_to_hexa(string):
    hexa = "0x"
    for i in range(len(string)):
        hexa += hex(ord(string[i]))[2:]
    return hexa

def hexa_to_string(hexa):
    string = ""
    for i in range(2, len(hexa), 2):
        string += chr(int(hexa[i:i+2], 16))
    return string


def smart_contract_mint_request(owner : str, sc_adresse : str,  titre : str, description : str, photo_link : str, localisation : str):
    
    titre = string_to_hexa(titre)
    description = string_to_hexa(description)
    photo_link = string_to_hexa(photo_link)
    localisation = string_to_hexa(localisation)

    request =  "octez-client -l --endpoint https://ghostnet.smartpy.io transfer 0 \
    from " + owner + " to " + sc_adresse + " \
    --entrypoint mint --arg '(Pair \"" + owner + "\" {Elt \"description\" " + description + " ; Elt \"localisation\" "+ localisation +"; Elt \"photo_link\" "+ localisation +" ; Elt \"titre\" " + titre +" })' \
    --fee 0.001433 \
    --gas-limit 10000 \
    --storage-limit 800"


    os.system(request) # executer la commande pour interagir avec le smart contract

    return request

a = smart_contract_mint_request("tz1PZY3agTGshV48bcYVbuz88G3mfL8wgm1p", "KT1MArMCMVWohqsuksyAtCCi2TGshDpp4G5F", "plage", "crique romaine", "https://www.envol-espace.fr/photos/barcelone_et_catalogne/la_catalogne_romaine/5762/cirque_romain_tarragone.jpg", "tarragone")


'''
    "octez-client -l --endpoint https://ghostnet.smartpy.io transfer 0 \
    from " + owner + " to " + sc_adresse +"\
    --entrypoint mint --arg '(Pair \""+owner+"\" {Elt \"bob\" 0x33})' \
    --fee 0.001329 \
    --gas-limit 10000 \
    --storage-limit 496"
'''