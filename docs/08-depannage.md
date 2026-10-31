# 8. Questions fréquentes

## Toutes les Prius 4 sont compatibles ?

Non établi. Comparer **références matérielles, région, JBL, navigation et Model ID**. Le nom commercial Prius IV ne suffit pas. Le cas documenté est 86140-47490 / 86840-06041 / CV-CS38E2AJ.

## Faut-il acheter des cartes ?

Ce cas précis a réussi sans achat ni mise à jour séparée au départ de navdb 943. Les copies v4/v10 du bulletin diffèrent sur ce prérequis ; ne pas généraliser aux autres bases. Voir [compatibilité](01-compatibilite.md).

## Le moteur doit-il tourner ?

La Prius doit être **en READY**, dehors, en P avec frein de stationnement. Le moteur thermique peut s'arrêter et redémarrer automatiquement. Le mode accessoires seul n'est pas suffisant. Ne couper POWER qu'aux fins d'étapes prévues.

## « Preparing new software » dure longtemps

C'est une phase d'installation, pas un message de fin. Garder l'alimentation et la clé. Les durées du guide sont indicatives ; si un défaut est annoncé, consigner son texte exact et l'étape. Ne pas imposer une coupure après un délai arbitraire.

## Retirer la clé avant le redémarrage ?

Cela dépend de l'étape. Première préparation clé 1 : la garder jusqu'à la reprise et STATUS DONE. Mise à jour clé 2 : la garder lors du redémarrage. Fin de réplication clé 1 : la retirer avant redémarrage. Fin explicite de conversion clé 3 : la retirer avant de couper POWER. Finalisation clé 2 : attendre une minute hors tension, redémarrer, attendre l'accueil puis deux minutes, retirer. Toujours comparer avec le [tutoriel complet](04-installation.md) et le message de l'écran.

## Navigation 1512 devient 1120, ou Audio 1023 apparaît

1120 appartient à la branche cible FA10 du cas testé ; le nombre ne représente pas l'année des cartes. Audio 1023 a été rapporté après la clé 3, avant Audio 1075 lors de la dernière clé 2. Vérifier les Model ID et l'étape exacte.

## La clé n'est pas reconnue

Avant toute écriture, contrôler insertion complète, port de données, FAT32, fichiers extraits à la racine et empreintes. Le boîtier d'une clé trop épaisse a empêché son insertion dans notre cas. Ne pas confondre un ZIP copié tel quel avec les fichiers extraits. Pendant une intervention déjà active, ne pas manipuler les supports hors de la séquence prévue.

## 42571 ou 42581 ?

Notre JBL utilise une copie complète de **42581**. L'autre profil annonce une amplification intégrée. Conserver les 17 fichiers, y compris le marqueur vide et les signatures ; aucune réécriture interne. Le profil n'est pas validé pour toutes les Prius.

## Android Auto sans fil, CarPlay, YouTube ou applications internes ?

Android Auto filaire est confirmé. CarPlay n'a pas été essayé ici. Aucun sans-fil natif, navigateur universel, lecteur vidéo libre ni installateur d'APK dans le poste n'est démontré. La présence de SDL est traitée [séparément](07-smartdevicelink.md).

## Peut-on restaurer l'ancien système avec les journaux Diagnosis Recorder ?

Aucune méthode de restauration complète n'a été validée dans ce projet. Un export de journaux n'est pas une image de sauvegarde intégrale du firmware. Ne pas promettre de retour arrière automatique.

## Comment contribuer sans divulguer mes données ?

Utiliser le formulaire de retour et indiquer les références génériques et versions. Masquer VIN, série, immatriculation, coordonnées, appareils appairés et localisations ; supprimer les métadonnées des photos. Ne pas joindre un export brut de diagnostic.
