# 10. Se faire accompagner par une IA

Une IA peut aider à lire les références, comparer les preuves, contrôler les fichiers et expliquer la prochaine étape. Elle ne voit pas le poste ni l'état électrique de la voiture si vous ne les lui décrivez pas, et ne peut pas garantir le résultat.

## Utilisation simple

1. Ouvrir [le formulaire](https://toyrek.github.io/prius4-android-auto-retrofit/) ou remplir [la fiche](../ai/fiche-vehicule.md).
2. Copier [le message d'accompagnement](../ai/PROMPT.md) dans son assistant.
3. Ajouter ses propres relevés. Une information inconnue doit rester inconnue.
4. L'assistant rend un bilan de compatibilité, les informations manquantes et **une seule prochaine action**.

Le formulaire peut créer un message incluant les valeurs saisies. Il fonctionne sans compte, sans serveur de traitement et sans télémétrie. Une copie vers un assistant n'a lieu que si vous la collez vous-même.

## Pour les agents qui lisent un dépôt

Le fichier [AGENTS.md](../AGENTS.md) donne les règles de travail. [ai/procedure.json](../ai/procedure.json) décrit les états et observations attendues pour le cas déjà documenté. [ai/vehicle.example.json](../ai/vehicle.example.json) est un exemple, pas les données d'un nouvel utilisateur. Les dossiers personnels `private/` et `raw/` restent exclus de Git.

Le module `guide/preflight.js` réalise une comparaison prudente des champs fournis. Il renvoie toujours `flash_authorized: false` : son rôle est le tri et l'explication, pas la validation matérielle. L'agent doit connaître les sources et les prérequis avant de guider une action.

```text
node tools/check-vehicle.cjs chemin-vers-ma-fiche.json
```

## Exemple d'échange utile

Propriétaire : « J'ai une Prius 2017, est-ce que je peux mettre la clé 1 ? »

Réponse attendue : « L'année seule ne suffit pas. Sans brancher de clé, ouvre Mise à jour du logiciel et recopie le Model ID DCU. »

Propriétaire : « Ça affiche Preparing new software. »

Réponse attendue : « L'installation est en cours. Garde READY et la clé branchée. Attends le message de fin prévu pour cette étape. » L'agent conserve aussi l'étape et le numéro de clé connus ; il ne redemande pas de repartir au début.

## Ce que l'agent doit expliquer

- La différence entre **même configuration qu'un retour** et **compatibilité garantie**.
- La différence entre logiciel Navigation et cartes navdb.
- Pourquoi DA31/FA10 ou une conversion partielle changent le parcours.
- Pourquoi un profil JBL ne s'utilise pas par défaut sur un autre équipement.
- Quelle preuve permet de passer à l'étape suivante, avec le texte exact de l'écran.

L'IA ne remplace pas le bulletin applicable. Si le message ou la référence diffère, elle doit reconstituer les faits et chercher la bonne procédure, plutôt que proposer de nouvelles clés au hasard.
