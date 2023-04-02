from core.utilisateur import Utilisateur
from carte import Carte

# Create a new user

Alice = Utilisateur("0xkjsbdvkqdfbvlkjqdbv")
Alice.set_pseudo("Alice")
Alice.creer_carte("Plage", "Une carte de la plage de la baule", "La Baule")
Alice.creer_carte("Grotte", "Une carte de la grotte de la baule", "La Baule")

Bob = Utilisateur("0xwj54qdf5d8s9rbv")
Bob.set_pseudo("Bob")
Bob.creer_carte("Cave à vins", "Une carte de la cave à vins du domaine de Chardon", "Chardon en champagne")
Bob.creer_carte("Restaurant", "Une carte du restaurant du domaine de Chardon", "Chardon en champagne")

# Alice wants to sell her "Plage" card to Bob

Alice.vendre_carte(Alice.collection[0], Bob, 10)

# Bob wants to sell his "Cave à vins" card to Alice

Bob.vendre_carte(Bob.collection[0], Alice, 15)

# Alice wants to sell her "Grotte" card to Bob

Alice.vendre_carte(Alice.collection[0], Bob, 20)

# Bob wants to sell his "Restaurant" card to Alice

Bob.vendre_carte(Bob.collection[0], Alice, 25)

# Alice describes her collection

Alice.decrire_collection()

# Bob describes his collection

Bob.decrire_collection()


