# Outils du dépôt

`verify.py` : Python 3.9 ou plus récent, bibliothèque standard uniquement. Compare les archives ou fichiers extraits aux inventaires publiés. Ne télécharge rien, ne formate rien, ne modifie aucun fichier et n'envoie aucune donnée. Les contrôles complets USB3 peuvent être longs. Les dossiers Windows explicitement ignorés ne sont pas inspectés. Les erreurs d'accès interrompent le contrôle.

```text
python tools/verify.py archives CHEMIN_DOSSIER_ZIP
python tools/verify.py usb1 RACINE_CLE_1
python tools/verify.py usb2 RACINE_CLE_2
python tools/verify.py usb3 RACINE_CLE_3
python tools/verify.py audio1046 RACINE_CLE_AUDIO
```

Codes de sortie : 0 = identité des fichiers attendus ; 1 = écarts ; 2 = erreur empêchant le contrôle. Une identité de fichiers ne garantit pas la compatibilité du véhicule et ne vérifie pas le format du support.

`validate_repository.py` : liens locaux, cohérence des inventaires, copie exacte du profil et quelques motifs de données privées. C'est un contrôle automatisé borné, pas une garantie générale d'anonymisation.

`build_pdf.py` : génération du tutoriel depuis `docs/*.md`, avec ReportLab. Nécessite Python, `reportlab`, et les polices Segoe UI/Consolas sous Windows ou DejaVu sous Linux. Il écrit uniquement le PDF dans `downloads/`.

```text
python -m unittest discover -s tests -v
python tools/validate_repository.py
python tools/build_pdf.py
```

Les outils ne flashent jamais l'autoradio. Aucun script constructeur n'est exécuté par eux.
