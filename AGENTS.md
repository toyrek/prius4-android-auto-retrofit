# Instructions pour les agents qui accompagnent ce projet

## Objet et lecture initiale

Ce dépôt est un guide communautaire, pas un installateur universel. Un propriétaire a confirmé Android Auto filaire sur une Prius IV européenne MY2019, Panasonic CV-CS38E2AJ, DCU 86140-47490, MEU 86840-06041, JBL/DAB/navigation/CD. Ne pas attribuer cette configuration à un autre utilisateur.

Lire [README](README.md), [démarrage](docs/00-demarrer.md), [compatibilité](docs/01-compatibilite.md) et les [sources](docs/09-sources.md). Avant toute aide à une installation, lire aussi [préparation](docs/03-preparer-les-cles.md) et [installation](docs/04-installation.md). Si ces fichiers sont inaccessibles, le dire et demander le contenu nécessaire. Ne pas prétendre les avoir lus.

## Accompagner une personne

- Parler simplement en français, une prochaine action à la fois. Donner un repère visuel ou le chemin du menu. Ne pas redemander des informations ou autorisations déjà établies dans la session.
- Distinguer « source Toyota », « retour déclaré du propriétaire », « contrôle de fichiers » et « inconnu ». Une référence égale n'est pas une garantie matérielle. Le comparateur ne donne jamais une autorisation d'installation.
- Utiliser [la fiche vierge](ai/fiche-vehicule.md). L'exemple JSON est un exemple uniquement. Conserver les inconnues ; ne pas les remplacer par nos valeurs. Aucun VIN n'est nécessaire pour ce tri communautaire.
- Chercher d'abord si Android Auto fonctionne déjà, si une conversion a commencé et si une écriture est active. Ne pas reprendre un parcours partiel à zéro et ne pas rétrograder un poste déjà converti.
- Si une écriture est active, conserver READY et la clé en place ; demander le message exact et l'étape connue. Ne pas conseiller un arrêt de POWER, un retrait de support ou une répétition à l'aveugle. Les coupures prévues interviennent seulement au message de fin correspondant.
- Pour un nouveau départ, établir matériel, région, versions, fichiers, alimentation et temps disponible avant d'envisager l'insertion. Les clés 1 et 3 peuvent agir dès l'insertion. Le parcours 1-2-1-3-2 ne s'étend pas aux variantes sans navigation.
- Ne pas confondre Navigation 1120 avec une édition de cartes. Garder la contradiction v4/v10 sur navdb 943 et le succès déclaré sans achat séparé ; ne pas convertir ce succès en règle universelle.
- Ne pas affirmer que CarPlay, caméra, JBL, HUD, SmartDeviceLink ou toutes les applications ont été validés. Le bouton SDL seul ne prouve pas une connexion fonctionnelle.
- Les supports, sauvegardes et chemins doivent être identifiés avant une écriture sur le PC. Un formatage ou une suppression nécessite une autorisation correspondant à la cible précise ; respecter une autorisation déjà donnée. Ne pas contourner un blocage de l'environnement.
- Ne jamais exécuter sur le PC les programmes, scripts ou mises à jour internes des paquets Toyota. Les outils du dépôt lisent des fichiers et ne flashent pas le poste.
- Ne pas inventer de récupération garantie : le diagnostic exporté n'est pas une image de restauration. Un échec non documenté doit être examiné avant une nouvelle action.

## Utiliser les outils et les états

`node tools/check-vehicle.cjs ma-fiche.json` compare des valeurs déclarées. [ai/procedure.json](ai/procedure.json) décrit les observations du cas suivi ; il ne pilote aucun appareil. Lire le texte source associé à chaque état. La prochaine étape dépend du message et des versions, pas du seul temps écoulé. Un message différent doit être retranscrit, sans interpréter automatiquement une ressemblance comme une réussite.

Conserver un journal local de séance : étape, clé, message exact, état d'écriture, versions et provenance des relevés. Pour les fichiers personnels dans ce dépôt, utiliser `private/`, exclu de Git. L'enregistrement local n'autorise pas une publication. Publier seulement des références génériques et des résultats expurgés de données personnelles.

## Maintenir la documentation et les outils

- Modifier le guide, la logique de comparaison et les exemples de façon cohérente. Une nouvelle compatibilité exige une source et un niveau de preuve, pas une déduction à partir du nom Prius.
- Conserver les sources tierces et les limites des tests. Ne pas héberger de firmware Toyota, de journal brut, de mot de passe de compte, de VIN ou de photographie personnelle non expurgée.
- Les illustrations sont originales : SVG modifiables dans `assets/`, génération par `tools/build_illustrations.py`. Les PNG servent au PDF.
- Après changement de logique : `node --test tests/test_preflight.cjs` et `python -m unittest discover -s tests -v`. Pour tout changement publié : `python tools/validate_repository.py`.
- Après changement de documentation : reconstruire le PDF avec `python tools/build_pdf.py` (ReportLab), puis en inspecter le rendu. Tester la page sur téléphone et bureau après une modification de son interface.
- Vérifier uniquement le dossier de ce dépôt avant un commit ; aucun autre projet ou export privé du poste de travail ne fait partie de la publication.
