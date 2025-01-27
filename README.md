# 🔔  SilverNotif  
SilverNotiff est un bot discord qui envoi une notification lorsqu'une vidéo est postée sur youtube.
*(en dev mais fonctionel)*

---

## 🔗  Prérequis 
- Python avec pip
- Une app discord crée sur [discord.com/developers](https://discord.com/developers/applications)

## 🛠️  Créez une app Discord
- Créez une app nomée SilverNorif sur [discord.com/developers](https://discord.com/developers/applications)
  - Dans la configuration de l'app, dans la catégorie "Bot"
    - Décochez "Public Bot"
    - Cochez les trois permissions : "Presence Intent", "Server Members Intent" et "Message Content Intent"

## 🕹️  Pour utiliser SilverNotif
- Téléchargez la derniere [releases](https://github.com/SilverCore-Git/SilverNotif/releases)
- Déplacez les fichiers du bot dans un dossier dédié
- Ouvrez un terminal dans le dossier dédié. Y accéder avec ``cd chemin vers le dossier``
- Exécutez la commande ``pip install discord.py json requests``
- Modifiez la configuration dans le fichier ``config.json``
- Exécutez le bot en ouvrant ``bot.py`` avec ``python`` ou <br>
  avec la commande ``python bot.py`` ou ``py bot.py``

## ⚙️  Pour configurer ``config.json``
*Ce fichier peut être ouvert avec block-note*

- 🎫 TOKEN :
  - Se rendre sur son app discord sur [discord.com/developers](https://discord.com/developers/applications)
  - Dans la catégorie "Bot" cliquez sur "Reset Token" pour l'obtenir.
    **ATTENTION : Le TOKEN permet de contrôler le bot, ne pas le divulguer facilement !**
  - Remplir le champs ``"Token": "your token"`` avec le token

- 🔑 APIKEY :
  Il sagit de la clé pour accéder à l'api "Youtube Data API V3"
  Il va faloire la demander à google !
  - Rendez vous sur [Google cloude console](https://console.cloud.google.com]
  - Connectez-vous avec un compte Google ou créez un compte si ce n'est pas encore fait.
  - Configurez un nouveau projet :
    - Cliquez sur le menu déroulant Sélectionner un projet ou Créer un projet.
    - Donnez un nom à votre projet et cliquez sur Créer.
  - Une fois le projet créé, allez dans le menu de navigation à gauche API & Services > Dashboard
  - Cliquez sur Activer les API et services.
  - Recherchez l'API ``Youtube Data API V3``, puis activez la.
  - Retournez sur le Dashboard des API & Services.
  - Cliquez sur Créer une clé API. Vous obtiendrez une clé générée automatiquement
    **Conservez cette clé en lieu sûr car elle sera affichée une seule fois après sa création**

 - 📋 ACTIVITY :
    - Deffinisez ce qui va s'afficher en dessous du bot (status)

 - 🏷️ ChanelID :
    - Il s'agit de l'identifiant de la chaîne youtube
    - Rendez vous sur votre [youtube studio](https://studio.youtube.com)
    - Dans le menu à gauche, cliquez sur Paramètres > Général.
    - L'ID de la chaîne se trouve sous Informations de base.

 - 💳 SalonID_YTB :
    - Il s'agit de l'id du salon dans lequel les notifications seront envoyés
    - Dans les paramètres utilisateur discord activez le "Mode développeur"
    - Paramètre > Avancés > Mode développeur
    - Faites click droit sur le salon voulu puis ``Copier l'identifiant du salon``
    - Collez l'ID à la place de ``123456789123456789``


---
by [SilverCore](https://github.com/SilverCore-Git) 👑 [Vous pouvez nous aider](https://tipeee.com/silverdium) 😎💸<br>
Merci de soutenir les projets SilverCore ❤️ !<br>
🔐 Vous n'êtes pas autorisés à vendre ce code sans l'autorisation explicite de l'auteur. 🛡️<br>
⭐  SilverCore ©️ Tous droits reservés  ⭐
