# 6. Ce que les recherches ont apporté

Avant le rétrofit, le projet a exploré le diagnostic USB, MirrorLink, Miracast, la création d'une application mobile, le lanceur/eStore et les formats de mise à jour. Le résultat concret obtenu à ce jour est le rétrofit documenté ; les essais précédents ne sont pas des solutions d'installation équivalentes.

## Informations provenant de l'autoradio

L'export **Diagnosis Recorder** obtenu sur une clé réellement insérée a permis de confirmer DCU **86140-47490**, MEU **86840-06041** et de rapprocher le poste de la configuration Panasonic **CV-CS38E2AJ / JBL**. Les photos du menu technique confirmaient les références et proposaient notamment Product Information, Service Information et MM Diag Recorder.

Un problème matériel simple expliquait initialement « USB non connectée » : le corps de la clé empêchait une insertion complète. Un support au boîtier suffisamment fin a permis la copie. Éviter de forcer ou d'abîmer le port ; l'USB près de l'AUX était le port utilisé dans ce cas. Un téléphone qui charge ne prouve pas à lui seul que la liaison de données fonctionne.

Les données version extraites de `TRC_VERSION.dat` comportaient 53 enregistrements et 28 combinaisons observées. Ces champs peuvent mélanger plusieurs états : ils ne remplacent pas les versions actuellement affichées dans le menu logiciel. Les enveloppes `.enc2` n'ont pas été déchiffrées avec succès. Les journaux n'ont pas fourni un SDK constructeur ni un accès administrateur démontré.

**Aucun journal brut n'est publié.** Ils peuvent contenir des appareils appairés, adresses réseau, trajets et identifiants. Les références matérielles, versions, empreintes de fichiers Toyota et conclusions utiles sont conservées sans les identifiants uniques du véhicule.

## Résultat des pistes explorées

| Piste | Observation de la séance | Conclusion limitée |
|---|---|---|
| USB PC vers voiture | Aucun échange exploitable détecté | Ce branchement ne démontre pas un accès au système du poste |
| Point d'accès / Wi-Fi Direct / MirrorLink | Recherches sans connexion fonctionnelle | Être sur le même réseau ne suffit pas à établir le protocole |
| Miracast depuis Windows | Écran du PC affiché sur la Toyota avant rétrofit | Réception Miracast alors observée ; téléphone Sony et état après rétrofit non validés |
| Prototype mobile Prius Link | La Toyota a affiché « device not supported » | Le prototype ne constitue pas une solution fonctionnelle publiée ici |
| Lanceur, eStore, SystemViewer | Recherches locales et SDK publics analysés | Aucun installateur personnel accepté par cette unité n'a été démontré |
| Rétrofit Panasonic adapté | DA31/FA10 et Android Auto filaire obtenus | Voie réussie sur le matériel précisément documenté |

Le succès du rétrofit corrige l'hypothèse initiale selon laquelle cette unité ne pourrait pas recevoir de projection par USB. Il ne transforme pas le poste en tablette Android et ne prouve pas qu'une APK s'installe dans son système.

## Projets utiles pour poursuivre, sans promesse de compatibilité

- [SDL Core](https://github.com/smartdevicelink/sdl_core) et [SDK Java/Android](https://github.com/smartdevicelink/sdl_java_suite) : architecture et client SDL, pas installateur Toyota.
- [Exemples SDL](https://github.com/SmartDeviceLink-Examples) : démonstrations à adapter et vérifier.
- [WirelessAndroidAutoDongle](https://github.com/nisargjhaveri/WirelessAndroidAutoDongle) : projet de pont matériel vers Android Auto filaire ; non testé sur cette Prius.
- [Android for Cars](https://developer.android.com/training/cars) : développement d'applications mobiles compatibles avec les catégories et interfaces prévues par Android Auto.

La recherche sur **BE-00493T-TME** et le diagnostic MEU n'a pas établi de méthode générale pour installer notre propre application depuis une clé USB. Ce dépôt ne présente aucun outil de diagnostic comme un installateur validé.
