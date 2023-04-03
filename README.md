# Bienvenue sur NFTrip !

NFTrip est une application de tokenisation de carte représentant des lieux insolites. Elle vous permet de créer et d'échanger des cartes NFT (Non-Fungible Tokens) de lieux insolites, tels que des sites historiques, des monuments célèbres, des musées, des lieux de tournage de films, et bien plus encore.

Ce projet remporte le 3e prix du Hackathon H-W3B, co-organisé par Sia Partners, Tezos et Exaion. qui a eu lieu en avril 2023 à Paris.

Notre application est codée en Python, avec un backend géré en Django. Nous avons développé notre marketplace sur la blockchain Tezos, pour assurer la sécurité et la transparence des transactions.

## Comment utiliser NFTrip :

- Installez les dépendances nécessaires à l'aide de la commande "pip install -r requirements.txt"
- Lancez le serveur en exécutant "python manage.py runserver"
- Accédez à l'application en ouvrant votre navigateur et en naviguant vers "http://localhost:8000/" (vérifiez d'être dans le repertoire racine du git)

## Fonctionnalités de NFTrip :

- Recherche de lieux insolites : notre application vous permet de rechercher des lieux insolites en utilisant une carte interactive. Vous pouvez zoomer et faire glisser la carte pour trouver des lieux à tokeniser. (à venir)
- Tokenisation de cartes : vous pouvez créer et échanger des cartes NFT de lieux insolites. Chaque carte est unique et représente un lieu spécifique.
- Transactions sécurisées : notre marketplace est basé sur la blockchain Tezos, qui assure la sécurité et la transparence des transactions.
- Gestion des comptes : vous pouvez créer un compte pour suivre vos transactions et vos cartes NFT.
- Pour créer un NFT, il suffit de se créer un compte et de remplir le formulaire "New Card". Ce dernier se créera automatiquement dans votre wallet Tezos et s'ajoutera sur la web app dans "browse". 
- Dans le Dashboard, vous pouvez voir la liste des cartes que vous possédez ainsi que vos certificats et les badges que vous avez gagnés.
- Dans l'interface "browse", vous pouvez voir l'ensemble des cartes disponibles et appliquer des filtres de recherche. Cliquez sur une carte pour tenter de l'obtenir en contactant le propriétaire via la messagerie de l'application.

## En savoir plus

- Le repo contient une vidéo de démonstration de l'application NFTrip pour la tokenisation de cartes de lieux insolites (demo-app.mp4)
- Une autre version de cette vidéo est disponible sur youtube : https://youtu.be/JMRlD3NEC24
- Pour retrouver la presentation du pitch faite au Hackathon : https://pitch.com/public/efd9e1ba-074b-4a21-8d3a-733fdb957bab/b8b030ff-f04b-4496-b25b-805c2001c2c5

## Smart Contract NFTrip :

Le smart contract NFTrip a été développé avec SmartPy, une plateforme open source pour la programmation de contrats intelligents sur la blockchain Tezos. Nous avons choisi SmartPy pour sa simplicité d'utilisation, sa documentation complète et sa grande communauté de développeurs.

Le smart contract NFTrip hérite du smart contract FA2.Fa2Nft, un contrat standard pour la gestion des tokens non fongibles (NFT) sur la blockchain Tezos. L'utilisation de FA2 permet une intégration facile avec d'autres contrats FA2 et offre une compatibilité avec les wallets et les plateformes d'échange prenant en charge le standard FA2.

## Remerciements
Nous sommes heureux de vous présenter NFTrip et espérons que vous apprécierez l'expérience de la tokenisation de cartes de lieux insolites. Si vous avez des questions ou des commentaires, n'hésitez pas à nous contacter à l'adresse support@nftrip.com. (à venir)

NFTrip est le fruit de notre participation au hackathon H-W3B, co-organisé par Sia Partners, Tezos et Exaion.
Notre équipe a travaillé avec passion pour développer NFTrip et fournir expérience utilisateur qui inclus les néophytes vis à vis de la cryptosphère. Nous sommes fiers de présenter notre application et de contribuer à l'écosystème de la blockchain.

Nous tenons à remercier Sia Partners et Tezos pour l'organisation de ce hackathon ainsi que tous les coachs qui nous ont aidé pendant ces 3 jours, et l'opportunité de participer à un tel événement passionnant. Nous sommes impatients de participer à d'autres événements de ce type à l'avenir
