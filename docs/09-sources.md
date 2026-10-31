# 9. Sources, traçabilité et crédits

Édition du 31 octobre 2026. Les constats dans la voiture sont ceux du propriétaire, pendant la séance du 30 octobre. Le dépôt ne transforme pas ces retours en certification Toyota. Les contrôles de fichiers sont des observations techniques locales distinctes.

## Documentation Toyota

- **BE-00439T-TME v10**, daté du 21 juin 2021, copie polonaise de 37 pages. Portée officielle Corolla/RAV4, préparation USB et séquence de conversion. La date d'impression visible 16/03/2025 n'est pas la date de révision. [Miroir fourni lors de la recherche](https://pub-28b50ea23bc849d8bdc62bda00d48d4f.r2.dev/BE-00439T-TME.pdf) : accès non fiable, nouvel accès par l'outil web impossible le 31/10/2026. Copie obtenue auparavant et relue localement ; non authentifiée par comparaison à une session Toyota-Tech. Empreinte du PDF étudié : `26061c48dd37e8e619bc32b7d1a4479647c2cb869245a5a5b1c80cff3f8ca32e`.
- **BE-00439T-TME v4**, daté du 18 septembre 2020, copie anglaise de 34 pages. Pages 4-5 et 9 pour 943/2018 v1. [Miroir historique Google Drive](https://drive.google.com/uc?export=download&id=1tP9C-T2Tzz8iffhAyeIqCY1d577VBjzC), disponibilité non revalidée dans cette publication. Empreinte : `d27f7fea3812ab6bda843230a220955706ab66f5439fb37a739b4820b7336b0a`. La v4 plus ancienne ne remplace pas automatiquement la v10.
- [Toyota-Tech Europe](https://www.toyota-tech.eu/) : source constructeur à consulter pour obtenir le bulletin applicable et ses éventuelles révisions.
- [BE-00344T-TME v8, copie hébergée par GVG](https://gvg.cz/wp-content/uploads/Toyota_Touch_2_%28MM19%29_Panasonic_1170.pdf) : historique de corrections Panasonic, dont Audio 1075. Ce document de 2022 ne prouve pas la version la plus récente en 2026.
- Archives officielles : liens, tailles et empreintes dans [Téléchargements](02-telechargements.md), données structurées dans [downloads.json](../data/downloads.json), contrôle HTTP daté dans [link-checks.json](../data/link-checks.json).

Ces PDF Toyota et firmwares ne sont pas inclus dans le dépôt. Le tutoriel PDF téléchargeable est notre propre synthèse, pas une copie du bulletin constructeur.

## Contributions communautaires

- **Rinsley, HybridLife** : [retour sur le matériel identique et profil 42581](https://hybridlife.org/threads/tutoriel-de-mise-%C3%A0-jour-de-toyota-touch-go-2.3945/page-73#post-199403). Ce témoignage a guidé l'adaptation de la clé 3 ; le projet ne revendique pas son invention.
- [HybridLife, page 79](https://hybridlife.org/threads/tutoriel-de-mise-%C3%A0-jour-de-toyota-touch-go-2.3945/page-79) : résultat incomplet signalé, à conserver dans l'évaluation des risques.
- [Toyota Owners Club, page 18](https://www.toyotaownersclub.com/forums/topic/195353-retro-fit-apple-carplay-android-auto/page/18/) : témoignage RAV4 au départ de 943. Ce n'est pas un essai Prius réalisé par nous.

Les liens communautaires sont des références de témoignages directs ; ils ne remplacent ni les versions exactes du véhicule ni les contrôles. Aucun message de forum ni photo d'un tiers n'est reproduit intégralement.

## Recherches techniques complémentaires

La [page SDL](07-smartdevicelink.md) cite Toyota Connected, Daihatsu et le projet SDL. La [page diagnostic](06-recherches-et-diagnostic.md) distingue observations locales, recherches infructueuses et projets ouverts. Le code des projets tiers reste sous leur propre licence.

## Périmètre des fichiers publiés

Les inventaires publiés contiennent uniquement chemins relatifs de fichiers de paquets, tailles et empreintes. Les numéros de série USB, lettres de lecteurs personnels, chemins utilisateurs, fichiers de sauvegarde personnels, VIN et journaux de communications ont été exclus. Le [cas testé](../data/tested-configuration.json) garde les références génériques et le niveau de preuve.

Les quatre archives reçues ont passé un test complet 7-Zip le 30/10/2026. Les clés préparées ont été relues pour comparaison des fichiers. La dernière structure de la clé 3 comportait **517 fichiers et 23 477 795 418 octets**. Un hash conforme atteste l'identité avec notre exemplaire, pas une signature indépendante de Toyota ni une validation de compatibilité.
