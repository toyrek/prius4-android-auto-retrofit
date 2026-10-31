# 7. SmartDeviceLink Toyota

SDL permet à une application du téléphone d'utiliser une interface intégrée au poste : textes, menus, commandes, audio ou navigation selon l'application et les fonctions autorisées. Le constructeur intègre SDL Core et contrôle les capacités. Un SDK public ne signifie pas que l'on peut installer une APK arbitraire dans l'autoradio. [Architecture officielle](https://smartdevicelink.com/overview/).

## Ne pas confondre les marchés et les unités

- **Japon :** Toyota Connected annonce la fermeture du service SDL ordinaire fin août 2022, avec orientation vers Android Auto/CarPlay. L'annonce prévoit une exception pour **Toyota SmartDeviceLink for DH**, certaines Raize et Roomy. Elle ne prouve pas une fermeture identique sur le Panasonic européen. [Annonce du 25/08/2022](https://toyotaconnected.co.jp/movilink/info/20220825_01.html).
- **Application DH :** la [fiche publiée par Toyota](https://apps.apple.com/jp/app/toyota-smartdevicelink-for-dh/id1476035524) désigne les Raize/Roomy avec équipement concerné. Ce n'est pas une application universelle pour Prius.
- **Europe :** un manuel TAS500 documente Toyota Apps/SDL, mais sa [liste d'applications datée de 2018](https://mapupdatecontent.toyota-europe.com/Support/TAS500_ToyotaApps.pdf) n'en annonce alors aucune. TAS500 n'est pas notre Panasonic ; cette liste n'est pas un état global de 2026.

Les catalogues historiques japonais citent moviLink, CarNAVITIME, LINE MUSIC et d'autres applications, avec restrictions de téléphone et de transport. Ils ne constituent pas une liste actuelle pour une Prius européenne. Daihatsu annonce par exemple la fin de la liaison SDL CarNAVITIME en septembre 2025. [Catalogue Toyota de 2022](https://toyota.jp/pages/contents/dop/navi/displayaudio/pdf/da_sdl_app.pdf), [avis Daihatsu de 2025](https://www.daihatsu.co.jp/connect/info/kg79k700000000g6.htm).

## Sur le poste converti

Le propriétaire voit un bouton SDL après Audio 1075. La copie v10 de BE-00439T-TME annonce pourtant son retrait avec RC2002+. Aucun écran d'ouverture ni connexion SDL réussie n'est encore consigné. Interface résiduelle, variation de configuration ou service encore présent restent des hypothèses.

La fermeture commerciale d'un service ne démontre pas à elle seule que le protocole local ne peut plus fonctionner. À l'inverse, un bouton ne démontre pas l'acceptation des applications.

## Piste de développement

Un client Android minimal pourrait vérifier connexion, enregistrement d'application, version négociée, capacités et permissions. Le [SDK prévoit USB/Bluetooth pour un poste de série](https://smartdevicelink.com/en/guides/android/getting-started/connecting-to-an-infotainment-system/) via Multiplex ; les exemples TCP/port 12345 concernent notamment l'émulation et ne prouvent pas un port ouvert sur Toyota.

L'application doit lire les [capacités](https://smartdevicelink.com/en/guides/android/getting-started/checking-supported-features/) et les [permissions](https://smartdevicelink.com/en/guides/android/getting-started/understanding-permissions/) : certaines fonctions nécessitent l'approbation du constructeur. Aucune lecture de batterie hybride ou commande du véhicule n'est établie ici. Ce dépôt n'inclut pas de prototype SDL annoncé compatible ; Android Auto est la liaison actuellement validée par le propriétaire.
