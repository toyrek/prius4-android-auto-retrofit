# 3. Préparer les supports

Lire d'abord [compatibilité](01-compatibilite.md) et [téléchargements](02-telechargements.md). Le formatage efface la clé : sauvegarder son contenu et identifier le support par sa capacité et son nom, jamais uniquement par sa lettre Windows.

| Étiquette | Minimum décrit par le bulletin | Support utilisé dans notre cas | Format |
|---|---:|---:|---|
| 1 | 8 Go | 8 Go | FAT32 |
| 2 | 16 Go | 32 Go | FAT32 |
| 3 | 32 Go | 64 Go avec partition FAT32 d'environ 33,27 Go | FAT32 |
| AUDIO1046, séparée | 2 Go | 32 Go | FAT32 |

Le support Audio est nécessaire ici pour le départ en 1000. Une capacité de 64 Go n'impose pas de remplir toute la clé. Si Windows ne propose pas FAT32, utiliser un outil de formatage adapté en vérifiant soigneusement le disque sélectionné. Aucun script du dépôt ne formate, supprime ni prépare automatiquement une clé.

## Placer les fichiers au bon niveau

Extraire les ZIP sur le PC. Copier **le contenu du dossier du paquet** à la racine de chaque clé. Ne pas conserver un niveau supplémentaire nommé `Full_upgrade_package_...` sur la clé.

```text
Clé 1 / intervention / ...                     13 fichiers
Clé 2 / fichiers .kwi + deux README            21 fichiers distincts
Clé 3 / fichiers .kwi, .dat, .xml,
        dossiers d'origine dont VehicleParameter
        + adaptation décrite ci-dessous       517 fichiers après adaptation
Audio / 17TDT2EU-DA01_0020.kwi                  1 fichier
```

Les archives USB2 et USB3 contiennent deux README en double. Le comptage d'entrées du ZIP est donc différent du nombre de fichiers distincts après extraction : **23 → 21** et **502 → 500**, puis 17 fichiers ajoutés pour la Prius. Les rapports du dépôt dédupliquent les entrées identiques. Ne supprimer aucun fichier différent pour atteindre artificiellement ces nombres.

## Adaptation de la clé 3 pour le matériel JBL testé

Le paquet utilisé ne contient pas de dossier `86140-47490`. Dans `VehicleParameter/DCU`, copier **tout le dossier `86140-42581`**, puis nommer sa copie **`86140-47490`**. Conserver l'original.

```text
VehicleParameter/DCU/
  86140-42581/                   original conservé
    FactoryDataWrite            fichier vide conservé
    DCU/FactoryID/              16 fichiers
  86140-47490/                   copie complète
    FactoryDataWrite
    DCU/FactoryID/              les mêmes 16 fichiers
```

**Aucun contenu interne n'est réécrit** : conserver signatures `.txtsi`, `.binsi`, `.jsonsi`, fichiers binaires et marqueur vide `FactoryDataWrite`. Si un dossier 47490 existe déjà dans un paquet différent, ne pas l'écraser : réévaluer ce paquet.

Le profil 42581 contient `VP_PANA_AMP_type=ext_AMP_STEP1`, alors que 42571 contient `built_in_AMP`. Notre choix 42581 repose sur le matériel JBL, les profils et un retour de propriétaire identique. Ce seul champ ne prouve pas une compatibilité générale. **Ne pas substituer 42571 par intuition, ni appliquer 42581 à une Prius sans JBL.** [Origine du choix](09-sources.md).

## Vérifier avant d'éjecter

Avec Python 3, depuis le dépôt, remplacer `X:\` par la racine réelle de la clé correspondante :

```powershell
py -3 tools/verify.py usb1 'X:\'
py -3 tools/verify.py usb2 'X:\'
py -3 tools/verify.py usb3 'X:\'
py -3 tools/verify.py audio1046 'X:\'
```

Ces quatre commandes se lancent chacune sur **son propre support**. Elles relisent tous les fichiers et calculent leurs empreintes ; USB3 peut prendre plusieurs minutes. Les seuls dossiers Windows ignorés à la racine sont `System Volume Information` et `$RECYCLE.BIN`. Tout autre élément supplémentaire est signalé. Un contrôle réussi ne vérifie pas le format FAT32 ni la compatibilité du véhicule : vérifier également le système de fichiers dans les propriétés de la clé.

Ne pas mettre les téléchargements temporaires, journaux de diagnostic, ZIP ou dossiers d'autres clés à la racine. Éjecter chaque support proprement et écrire son numéro dessus. Les clés **1 et 3 ne doivent pas être branchées dans la voiture pour un simple essai de détection** : elles peuvent lancer une intervention.
