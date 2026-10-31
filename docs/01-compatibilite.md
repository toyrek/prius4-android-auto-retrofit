# 1. Vérifier si ce retour concerne votre poste

**Non, ces fichiers ne conviennent pas à tous les autoradios, ni automatiquement à toutes les Prius IV.** Ce dépôt documente une Prius IV européenne MY2019 précise. Les recherches ci-dessous séparent les faits constructeur, notre retour et les variantes encore inconnues. Mise à jour : 31 octobre 2026.

## Trouver sa famille de poste

| Votre situation | Ce qui est établi | Suite adaptée |
|---|---|---|
| Panasonic CV-CS38E2AJ, 86140-47490 + 86840-06041, JBL, DAB, CD, navigation, Europe | Notre cas a obtenu Android Auto filaire | Comparer aussi toutes les versions et les prérequis ci-dessous |
| Même matériel déjà DA31/FA10, Android Auto fonctionnel | Le changement de branche est déjà effectué | Utiliser Android Auto ; ne pas reprendre les clés |
| Même matériel, conversion commencée ou DA01/FA10, DA31/FA00 | État intermédiaire différent d'un départ intact | Reconstituer l'étape atteinte et les messages avant toute action |
| Autre Panasonic, autre référence Prius, sans JBL ou sans navigation | Aucun essai correspondant documenté ici | Recherche spécifique ; ne pas copier le profil 42581 par analogie |
| Ancien Touch / Touch 2, dont certaines Prius IV plus anciennes | Le nom commercial et l'année n'identifient pas la plateforme | Relever fabricant, pièces et Model ID ; pas de validation par la seule façade |
| Denso / Denso Ten | Architecture distinguée de Panasonic dans le bulletin étudié | Notre adaptation Panasonic ne s'applique pas ; rechercher la procédure propre au poste |
| Prius importée USA/Japon, Entune ou grand écran vertical 11,6 pouces | D'autres équipements et branches existent selon le marché | Ne pas utiliser nos paquets Europe ; identifier la variante locale |
| Prius/Prime US avec Android Auto déjà prévu d'usine | Certaines finitions le possèdent ; d'autres non | Vérifier la notice et l'usage avant d'envisager un rétrofit |
| Autoradio Android ou boîtier ajouté, hors équipement Toyota d'origine | Système distinct | Utiliser les mises à jour et instructions de son fabricant |
| Corolla/RAV4 concernés par une offre Toyota | Rétrofit constructeur documenté selon région/équipement | Suivre leur bulletin propre, sans ajouter notre copie de profil Prius |

« Non documenté » signifie que nous n'avons pas établi la compatibilité. Cela ne signifie pas qu'aucune solution alternative n'existe.

## Ce que confirment les sources Toyota

- **France :** la FAQ décrit historiquement une offre pour Corolla/Corolla Touring Sports produites à partir de janvier 2019 et RAV4 **Lounge Collection** à partir de janvier 2019. Elle n'annonce pas un déblocage universel de Touch 2. [Toyota France](https://www.toyota.fr/informations/faq/multimedia-ma-toyota).
- **Royaume-Uni :** Toyota cite Corolla MY19 toutes carrosseries/finitions et RAV4 MY19/MY20 sauf **Icon**, puis demande de confirmer l'éligibilité auprès du réseau. Les périmètres commerciaux varient selon le pays. [Toyota UK](https://mag.toyota.co.uk/toyota-apple-carplay-and-android-auto-upgrade/).
- **États-Unis :** Toyota annonce Android Auto sur les Prius 2021 **sauf Limited**. Pour Prius Prime 2021, l'ajout est annoncé sur **LE**. La mention « Prius 2021 » ou un écran plus grand ne suffit donc pas. Ces annonces d'équipement d'origine ne prouvent aucun rétrofit avec nos fichiers européens. [Prius US 2021](https://pressroom.toyota.com/the-car-that-changed-an-industry-toyota-marks-20th-anniversary-of-prius-with-special-anniversary-edition/), [Prius Prime US 2021](https://pressroom.toyota.com/the-2021-toyota-prius-prime-adds-safety-and-tech-while-continuing-to-combine-the-best-of-both-worlds/).
- **Bulletin BE-00439T-TME v10 :** le titre vise RAV4 avec navigation et Corolla avec/sans navigation (Panasonic/Harman). Les pages 4 et 9 distinguent variantes avec/sans MEU et Panasonic/Denso Ten. La mention de zone « tous marchés » du document ne démontre pas une compatibilité avec toute unité Toyota mondiale. Les fichiers publiés dans ce dépôt concernent le paquet **EU** examiné. [Provenance et pages du bulletin](09-sources.md).

Les pages Toyota USA ont été retrouvées dans l'index de recherche officiel ; l'ouverture directe a renvoyé HTTP 403 lors de ce contrôle. Les extraits constructeur accessibles soutiennent les distinctions de finition ci-dessus. Nous n'avons pas établi une liste exhaustive de toutes les références mondiales.

## Relever les identifiants exacts

Sans clé de rétrofit branchée, ouvrir **Menu → Configuration/SETUP → Général → Mise à jour du logiciel**. Relever DCU, MEU, Audio, Navigation et navdb_version. Les références de pièces et l'équipement JBL doivent également être identifiés ; la version Audio seule ne suffit pas.

| Champ | Cas testé |
|---|---|
| Panasonic | CV-CS38E2AJ |
| Référence DCU | 86140-47490 |
| Référence MEU | 86840-06041 |
| DCU avant conversion | 17TDT2EU-DA01 |
| MEU avant conversion | 17TMT2EU-FA00 |
| Équipement | JBL, DAB, navigation, CD |
| Audio initial | 1000, mis à niveau vers 1046 |
| Navigation initiale | 1512 |
| navdb initiale | 943 |

**Référence différente : compatibilité non établie ici.** Déjà DA31/FA10 avec Android Auto fonctionnel : ne pas recommencer ce parcours. Une unité partiellement convertie nécessite une analyse de son état, pas une reprise automatique à la clé 1.

## Cartographie : conserver la contradiction

La copie v4 du bulletin (2020) accepte explicitement 2018 v1/943 ; la v10 (2021) classe 943 parmi les bases à mettre à jour avant l'opération. Le cas documenté a démarré avec 943 et a obtenu Android Auto **sans achat ni mise à jour séparée des cartes**. Le numéro navdb final n'a pas été relevé.

Ce succès ne démontre pas que toutes les bases anciennes conviennent, ni que la consigne v10 peut être ignorée sur un autre poste. Pour A36, A4D, B00, B7E, autres versions ou données inconnues : aucune validation dans ce dépôt. Le logiciel « Navigation 1120 » et la base cartographique sont deux éléments distincts. Les références des documents sont dans [les sources](09-sources.md).

## Matrice de retours

| Cas | Matériel | Versions finales | Android Auto | Autres fonctions |
|---|---|---|---|---|
| Session du 30/10/2026 | 47490 + 06041, JBL, CV-CS38E2AJ | DA31 / FA10, Audio 1075, Navigation 1120 | Confirmé par le propriétaire | Vérification détaillée non consignée |

Le retour de Rinsley sur HybridLife a aidé à choisir le profil donneur ; il reste une source communautaire externe, pas un second essai réalisé par ce projet. Un résultat incomplet y est également signalé. Voir [sources](09-sources.md).

Une égalité de référence réduit l'incertitude sans garantir le résultat : état du matériel, historique logiciel, cartographie, alimentation et fichiers comptent aussi. Les inventaires SHA-256 vérifient des fichiers, pas la compatibilité automobile.

## Prérequis à examiner ensemble

| Vérification | Ce qu'il faut relever ou faire |
|---|---|
| Région et montage d'origine | Pays d'origine du véhicule, constructeur du poste ; signaler tout remplacement |
| Matériel | Pièces DCU/MEU et configuration ; une référence seule ne suffit pas |
| État actuel | Versions et éventuelle tentative déjà engagée ; ne pas repartir à zéro sur une conversion partielle |
| Audio | Dans le bulletin étudié, moins de 1011 exige un préalable ; notre DA01 en 1000 a reçu 1046. Ne pas rétrograder une version plus récente |
| Cartes | Relever navdb séparément de Navigation ; garder la divergence v4/v10 pour 943, ne pas inventer une règle pour une base inconnue |
| Supports | Supports distincts, sauvegardés, FAT32, extractions complètes et hashes contrôlés |
| Alimentation | Prius dehors, en P, frein serré, READY ; interrompre la préparation en cas d'état d'alimentation douteux avant le lancement |
| Temps et messages | Prévoir la durée complète ; changement de clé au message prévu, jamais au seul chronomètre |
| Sauvegarde | Conserver les réglages utiles ; un export de journaux n'est pas une image de restauration |
| Résultat | Contrôler les versions, puis les fonctions une par une ; une icône Android Auto ne certifie pas caméra/JBL/HUD |

Le [formulaire interactif](https://toyrek.github.io/prius4-android-auto-retrofit/) et le [guide IA](10-guide-agent-ia.md) organisent ces informations. Aucun ne certifie la compatibilité physique à distance.
