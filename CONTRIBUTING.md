# Contribuer

Ouvrir un retour avec le formulaire GitHub : modèle/année/marché, référence DCU et MEU, présence JBL/navigation, versions avant/après, hashes ou paquets utilisés, étapes et messages exacts, fonctions réellement testées. Les résultats partiels et les échecs ont leur place.

Préciser aussi le fabricant, l'écran, DAB/CD, le montage d'origine ou un remplacement et toute tentative antérieure. Utiliser [la fiche](ai/fiche-vehicule.md) pour organiser les informations ; laisser une valeur inconnue au lieu de reprendre celles de l'exemple.

Ne pas publier VIN, numéros de série, immatriculation, adresse, téléphone, e-mail personnel, identifiants réseau, contacts Bluetooth ou journaux bruts. Vérifier les métadonnées des photos. Une transcription précise suffit lorsque l'image expose des identifiants.

Une nouvelle ligne de compatibilité doit garder son niveau de preuve : déclaré par un propriétaire, documenté par photos expurgées, ou vérifié indépendamment. Ne pas transformer un succès sur une unité en affirmation pour une génération complète.

Pour une correction du tutoriel, citer la page/révision du bulletin ou le résultat observé. Ne pas ajouter un firmware binaire, une archive Toyota, un code d'activation personnel ou un outil de contournement à une pull request.

Les contributions originales aux documents sont sous CC BY 4.0 ; les contributions aux outils sous MIT. Conserver l'attribution des sources et préciser les limites des essais.

## Vérifier une contribution

```text
python -m unittest discover -s tests -v
node --test tests/test_preflight.cjs
python tools/validate_repository.py
```

Python 3.12+ et Node.js 18+ pour ces contrôles. La page statique ne nécessite aucune installation. Après un changement d'interface, vérifier un écran étroit et un écran de bureau, le clavier et les champs inconnus. Après un changement de logique, ajouter un cas significatif plutôt qu'un test qui recopie le code.

Pour reconstruire les schémas : `python tools/build_illustrations.py`. Pour leurs PNG, installer le paquet de développement optionnel `sharp` puis lancer `node tools/render_illustrations.cjs`. Pour le PDF : installer `reportlab`, puis `python tools/build_pdf.py` et inspecter visuellement le rendu. Les PNG déjà fournis permettent de reconstruire le PDF sans installer Sharp.
