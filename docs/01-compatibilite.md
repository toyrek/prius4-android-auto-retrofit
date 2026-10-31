# 1. Vérifier si ce retour concerne votre poste

Ce dépôt documente une **Prius IV européenne MY2019**. Il ne couvre pas automatiquement toutes les Prius IV, les Prius Prime/PHV, les modèles importés, les postes Denso ou les systèmes sans navigation.

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
