# 4. Installation : parcours du cas testé

Ce tutoriel décrit le cas Panasonic **DA01 / FA00, JBL 86140-47490 + MEU 86840-06041** et les paquets dont les empreintes sont publiées. Lire [compatibilité](01-compatibilite.md), notamment la divergence de consignes sur les cartes 943. L'adaptation Prius n'est pas une procédure constructeur universelle. Consulter le bulletin correspondant aux fichiers ; les étapes ci-dessous servent de guide communautaire.

**Ordre : Audio préalable si nécessaire, puis 1 → 2 → 1 → 3 → 2.**

## Conditions pendant toute l'intervention

Prévoir deux à trois heures. Voiture **dehors**, en **P**, frein de stationnement serré. Pied sur le frein, appuyer sur POWER et vérifier **READY**. Le moteur thermique peut démarrer automatiquement : un écran allumé en ACC ne suffit pas. Débrancher le téléphone et utiliser le port USB de données, dans notre cas près de la prise AUX.

Pendant une écriture, **garder l'alimentation et la clé branchée**. Les arrêts décrits ci-dessous se font seulement aux messages de fin correspondants. Pour revenir en READY, pied sur le frein puis POWER. Les réglages et appairages peuvent être effacés. Les durées sont indicatives ; aucun temps écoulé ne remplace un message de fin.

## 0. Audio préalable : 1000 vers 1046 dans notre cas

Le bulletin v10 impose une mise à niveau avant le rétrofit si Audio est inférieur à 1011. Pour notre DA01 en 1000, le paquet Toyota contrôlé propose 1046.

1. Vérifier **17TDT2EU-DA01** dans Mise à jour du logiciel. Ne pas utiliser le fichier préalable DA01 sur un système déjà DA31.
2. Brancher uniquement la clé AUDIO1046, puis ouvrir la mise à jour. Vérifier qu'Audio **1046** est proposé avant de confirmer.
3. Laisser l'installation finir, environ dix minutes. Au message demandant le redémarrage, suivre l'écran, couper POWER, attendre une minute et revenir en READY. Garder la clé pendant l'écriture et le redémarrage sauf instruction explicite de l'écran.
4. Confirmer Audio **1046** après démarrage ; retirer cette clé après la fin complète. Elle ne sert plus dans la séquence suivante.

Si Audio est déjà au moins 1011, le bulletin ne rend pas 1046 universellement obligatoire. Notre essai n'est pas une justification pour rétrograder une version plus récente.

## A. Clé 1 : préparation

1. Depuis HOME, brancher la clé **1**. Le démarrage est automatique, généralement en quelques secondes.
2. Attendre **RESULT: SUCCESS!**. Garder la clé branchée.
3. Couper POWER puis redémarrer en READY comme prévu à cette fin d'étape. Laisser le système reprendre avec la clé 1 présente.
4. Attendre **STATUS: DONE!**. Dans notre séance, l'écran indiquait ensuite de retirer cette clé et de lancer la mise à jour KWI. Retirer alors la clé 1.

## B. Clé 2 : conversion du logiciel Navigation

1. Brancher la clé **2**. Ouvrir Menu → Configuration/SETUP → Général → Mise à jour du logiciel.
2. Vérifier la proposition, lire les conditions et confirmer l'installation. Notre cible Navigation est **1120**.
3. Attendre la fin, environ vingt minutes. Au message **NEW SOFTWARE IS READY FOR UPDATE** demandant le redémarrage, couper puis redémarrer en READY **avec la clé 2 branchée**.
4. Vérifier **MEU 17TMT2EU-FA10 / Navigation 1120**. Si les valeurs attendues ne sont pas obtenues, relever le message et résoudre ce point avant de continuer.

Le passage de 1512 à 1120 correspond ici au changement de branche logicielle. Ce n'est pas un remplacement des cartes par une édition numérotée 1120.

## C. Clé 1 : réplication

1. Revenir à HOME, retirer la clé 2 et remettre la clé **1**.
2. Le démarrage peut prendre jusqu'à cinquante secondes. Attendre le message **REPLICATE SYSTEM ... FINISHED** et la fin du traitement indiquée à l'écran.
3. Quand l'opération est terminée, **retirer la clé 1**, puis couper POWER et redémarrer en READY.

## D. Clé 3 Europe : conversion du DCU

1. Brancher la clé **3**, préparée avec la copie complète du profil 42581 sous 47490.
2. Laisser toutes les phases s'exécuter, environ trente-cinq minutes, parfois davantage. Des redémarrages automatiques sont possibles.
3. **Preparing new software** et **Installing new software** sont des phases en cours. Ne pas retirer la clé ni couper l'alimentation.
4. Attendre le message annonçant l'installation terminée et demandant de retirer le périphérique USB puis d'arrêter le moteur/contact. Exécuter alors dans cet ordre : **retirer la clé 3 → couper POWER → redémarrer en READY**.
5. Vérifier **DCU 17TDT2EU-DA31**. Notre poste a alors affiché **Audio 1023** : c'était un état intermédiaire avant la finalisation.

Si DA01 reste affiché, si un message d'échec apparaît ou si l'état est différent, ne pas déclarer la conversion terminée et ne pas répéter les clés à l'aveugle.

## E. Clé 2 : finalisation Audio 1075

1. Remettre la clé **2** et lancer la mise à jour finale depuis Mise à jour du logiciel. Avec nos fichiers et notre DA31, la cible Audio est **1075**.
2. Laisser finir, environ dix minutes, puis attendre la demande de redémarrage.
3. **Garder la clé 2 branchée**, couper POWER, attendre **une minute** et redémarrer en READY.
4. Attendre l'accueil, puis encore **deux minutes** sans manipuler l'écran. Retirer ensuite la clé 2.
5. Confirmer **DA31 / FA10 / Audio 1075 / Navigation 1120** et effectuer les contrôles de la page suivante.

## Message inattendu

Noter l'étape, la clé, le texte exact et prendre une photo sans identifiants personnels. Pendant une écriture en cours, conserver l'alimentation ; ne pas improviser une coupure, une autre clé ou une répétition. Un écran bleu seul n'est pas une fin d'installation. Une unité bloquée peut nécessiter un professionnel ; aucun moyen de récupération garanti n'est fourni ici.

Références : BE-00439T-TME v10, pages 9 et 33-36 pour le préalable, 14-23 pour le MEU, 23-28 pour le DCU, 28-31 pour la finalisation ; [journal du cas testé](../data/tested-configuration.json). Les messages utilisateur confirment les résultats décrits, sans validation indépendante de toutes les fonctions.

Suite : [contrôles après installation](05-apres-installation.md).
