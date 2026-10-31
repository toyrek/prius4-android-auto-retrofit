# 2. Télécharger les archives utilisées

**Contrôle du 31 octobre 2026 :** les quatre adresses Toyota ci-dessous ont répondu en HTTP 206 ; les 16 premiers octets et la taille annoncée correspondaient à nos relevés. Cela ne remplace pas un téléchargement complet suivi d'un calcul SHA-256. Les archives utilisées le 30 octobre avaient passé le test d'intégrité complet 7-Zip.

| Usage | Lien sur le serveur Toyota | Taille du ZIP | Taille décompressée indicative |
|---|---|---:|---:|
| Clé 1 | [Full_upgrade_package_Toyota_USB1.zip](https://streamtechdoc.toyota-europe.com/techdoc3/retrofit/Full_upgrade_package_Toyota_USB1.zip) | 225 642 octets | Moins de 1 Mo |
| Clé 2 | [Full_upgrade_package_Toyota_USB2.zip](https://streamtechdoc.toyota-europe.com/techdoc3/retrofit/Full_upgrade_package_Toyota_USB2.zip) | 9 833 317 852 octets | 11,38 Go |
| Clé 3 **Europe** | [Full_upgrade_package_Toyota_USB3_EU.zip](https://streamtechdoc.toyota-europe.com/techdoc3/retrofit/Full_upgrade_package_Toyota_USB3_EU.zip) | 13 659 575 090 octets | 23,48 Go |
| Audio préalable **DA01** | [17TDT2EU-DA01_Latest.zip](https://streamtechdoc.toyota-europe.com/techdoc3/audio_navigation/17TDT2EU-DA01_Latest.zip) | 275 863 523 octets | KWI de 366 885 311 octets |

Le suffixe **Latest** peut désigner un contenu différent à l'avenir. Notre exemplaire contient `17TDT2EU-DA01_0020.kwi`, version Audio **1046**. Le nombre 0020 dans le nom ne signifie pas Audio 0020. Une empreinte différente exige une nouvelle vérification : ne pas forcer l'installation.

## Extraire avec 7-Zip

Utiliser [7-Zip officiel](https://www.7-zip.org/). Les mots de passe ci-dessous sont ceux des paquets dans la copie publique BE-00439T-TME v10, page 3, utilisés pour le contrôle complet. Ce ne sont pas des identifiants d'un compte Toyota.

| Archive | Mot de passe, à copier exactement |
|---|---|
| USB1 | `rtsHKUasDD259444AZR` |
| USB2 | `5PkE4O0dJeMd439c58d` |
| USB3 Europe | `M2mpLqbo1MsDqWQNkUe` |

Ne pas utiliser le paquet Russie/Kazakhstan pour ce parcours européen. Les liens et secrets d'archives ne constituent pas une autorisation constructeur pour la Prius. Le bulletin officiel se recherche sur [Toyota-Tech Europe](https://www.toyota-tech.eu/) sous **BE-00439T-TME** ; l'accès au document peut demander un abonnement. Notre copie publique et son origine sont décrites dans [Sources](09-sources.md).

Prévoir environ **65 Go libres** si l'on conserve simultanément les quatre ZIP et leurs contenus extraits sur le PC. Les gros ZIP ne tiennent pas comme fichiers uniques sur FAT32 : on télécharge sur le PC, puis on copie les **fichiers extraits** sur les clés.

## Contrôler l'intégrité

Les [SHA-256 des quatre archives](../data/SHA256SUMS.txt) sont des empreintes **mesurées par ce projet**, pas des signatures publiées par Toyota. Sous PowerShell, par exemple :

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath 'C:\TelechargementsToyota\Full_upgrade_package_Toyota_USB3_EU.zip'
```

Avec Python 3, depuis le dossier du dépôt, vérifier les quatre archives en une fois :

```powershell
py -3 tools/verify.py archives 'C:\TelechargementsToyota'
```

Dans 7-Zip, lancer également **Tester** sur chaque archive avec son mot de passe avant extraction. Une erreur CRC, une archive incomplète ou un hash différent doit être résolu avant de préparer une clé.

## Si le téléchargement s'interrompt

Les serveurs ont accepté les requêtes par plages lors de nos contrôles. Un exemple de reprise, pour USB3 seulement, avec `curl.exe` disponible sur le PC :

```powershell
curl.exe --fail --location --retry 5 --continue-at - --output 'Full_upgrade_package_Toyota_USB3_EU.zip' 'https://streamtechdoc.toyota-europe.com/techdoc3/retrofit/Full_upgrade_package_Toyota_USB3_EU.zip'
```

Utiliser le même fichier partiel, vérifier l'espace libre et contrôler le SHA-256 après la fin. Si le serveur refuse la reprise ou change de contenu, conserver le fichier partiel à part et réexaminer la source. Ne pas recopier un ZIP partiel sur la clé.
