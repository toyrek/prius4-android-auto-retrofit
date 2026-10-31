/* Read-only triage, shared by browser and CLI. This never authorizes flashing. */
(function(root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.PriusPreflight = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function() {
  'use strict';
  const fields = {
    update_in_progress: 'Écriture en cours', android_auto_works: 'Android Auto fonctionne déjà',
    conversion_started: 'Rétrofit déjà commencé', vehicle: 'Modèle de véhicule', year: 'Année modèle',
    market: 'Marché d’origine', original_unit: 'Poste d’origine', manufacturer: 'Fabricant',
    screen: 'Type d’écran', head_unit_model: 'Modèle du poste', dcu_part: 'Pièce DCU', meu_part: 'Pièce MEU',
    dcu_id: 'Model ID DCU', meu_id: 'Model ID MEU', audio: 'Audio', navigation_version: 'Navigation', navdb: 'navdb_version',
    jbl: 'JBL', navigation: 'Navigation Toyota', dab: 'DAB', cd: 'Lecteur CD'
  };
  const booleanFields = ['update_in_progress','android_auto_works','conversion_started','original_unit','jbl','navigation','dab','cd'];
  const choices = {vehicle:['prius4','prime','corolla','rav4','other'],market:['europe','usa','japan','other'],manufacturer:['panasonic','denso','aftermarket','other'],screen:['horizontal','vertical11','other']};
  const known = value => value !== null && value !== undefined && String(value).trim() !== '' && !['inconnu','unknown','?'].includes(String(value).trim().toLowerCase());
  const norm = value => typeof value === 'string' ? value.trim().toUpperCase() : '';
  function assess(input) {
    const p = input && typeof input === 'object' && !Array.isArray(input) ? input : {};
    const result = (code,title,summary,next,missing=[],notes=[]) => ({schema_version:1,code,title,summary,next_action:next,missing,notes,flash_authorized:false});
    if (p.update_in_progress === true) return result('IN_PROGRESS','Une écriture est en cours','La priorité est de conserver l’alimentation et le support en place.','Garder READY et la clé branchée ; relever le message exact et l’étape connue. Ne pas interrompre une écriture pour remplir ce formulaire.');
    const invalid=[];
    for (const k of booleanFields) if (known(p[k]) && typeof p[k] !== 'boolean') invalid.push(k);
    for (const k of ['year','audio','navigation_version']) if (known(p[k]) && (!Number.isInteger(p[k]) || p[k]<=0)) invalid.push(k);
    for (const [k,values] of Object.entries(choices)) if (known(p[k]) && !values.includes(p[k])) invalid.push(k);
    if (invalid.length) return result('INVALID_INPUT','Des valeurs sont à corriger','Aucune comparaison fiable avec ces champs.','Corriger : '+invalid.map(k=>fields[k]).join(', ')+'.',invalid);
    if (p.update_in_progress !== false) return result('MISSING','Commencer par l’état actuel','On ne sait pas si une installation est active.','Indiquer si une écriture est actuellement en cours.',['update_in_progress']);
    if (p.android_auto_works === true) return result('ALREADY_WORKING','Android Auto fonctionne déjà','Ce parcours de conversion n’est pas à recommencer.','Consulter le guide d’utilisation et les contrôles après installation.');
    if (p.conversion_started === true) return result('PARTIAL_REVIEW','Reconstituer la conversion commencée','Un parcours entamé ne doit pas être repris à zéro automatiquement.','Noter la dernière clé, le dernier message et les versions actuelles, sans brancher une autre clé.');
    if (known(p.market) && p.market !== 'europe') return result('OUTSIDE_GUIDE','Autre marché : autre étude','Les fichiers Europe de ce guide ne sont pas validés pour cette unité.','Rechercher la notice et les références propres au marché du véhicule.');
    if (p.vehicle === 'corolla' || p.vehicle === 'rav4') return result('OEM_ROUTE','Consulter la voie constructeur','Des variantes Corolla/RAV4 disposent d’un rétrofit Toyota ; notre adaptation de profil Prius ne leur est pas destinée.','Faire identifier la variante et son bulletin constructeur applicable.');
    if ((known(p.vehicle) && p.vehicle !== 'prius4') || (known(p.manufacturer) && p.manufacturer !== 'panasonic') || p.screen === 'vertical11') return result('OUTSIDE_GUIDE','Cette famille n’est pas couverte ici','Le cas Panasonic européen documenté ne permet pas de valider ce poste.','Identifier la procédure propre au fabricant et à la référence ; ne pas employer nos clés par analogie.');
    const d=norm(p.dcu_id), m=norm(p.meu_id);
    if (d==='17TDT2EU-DA31' && m==='17TMT2EU-FA10') return result('CONVERTED_REVIEW','Branche cible déjà affichée','DA31/FA10 indique un état différent du départ DA01/FA00.','Vérifier Audio et le lancement Android Auto ; ne pas refaire la conversion.');
    if (d==='17TDT2EU-DA31' || m==='17TMT2EU-FA10') return result('PARTIAL_REVIEW','Versions intermédiaires à examiner','Cette combinaison peut correspondre à une conversion partielle.','Reconstituer les étapes réalisées et les messages avant tout changement de clé.');
    const expected={head_unit_model:'CV-CS38E2AJ',dcu_part:'86140-47490',meu_part:'86840-06041',dcu_id:'17TDT2EU-DA01',meu_id:'17TMT2EU-FA00'};
    const differences=Object.keys(expected).filter(k=>known(p[k]) && norm(p[k])!==expected[k]);
    for(const k of ['jbl','navigation','dab','cd','original_unit']) if(p[k]===false) differences.push(k);
    if(differences.length) return result('OTHER_CONFIGURATION','Configuration différente du retour','Différences : '+differences.map(k=>fields[k]).join(', ')+'. Cela signifie non validé ici, pas impossible dans l’absolu.','Chercher un retour documenté ou un bulletin correspondant exactement à cette configuration.');
    const missing=Object.keys(fields).filter(k=>!known(p[k]));
    if(missing.length) return result('MISSING','Il manque des informations','Ne pas remplacer les inconnues par les valeurs du tutoriel.','Relever en priorité : '+missing.slice(0,3).map(k=>fields[k]).join(', ')+'.',missing);
    const notes=['Une correspondance de saisie ne certifie ni le matériel réel, ni la compatibilité, ni les clés.'];
    if(p.audio<1011) notes.push('Audio inférieur à 1011 : le bulletin demande un préalable. Notre DA01 en 1000 a reçu 1046.');
    else notes.push('Audio au moins 1011 : le seuil du bulletin est atteint. Ne pas rétrograder une version plus récente.');
    if(norm(p.navdb)==='943') notes.push('Cartes 943 : réussite rapportée sans achat, mais consignes v4/v10 contradictoires ; conserver cette incertitude.');
    else notes.push('Base cartographique différente du cas de départ 943 : vérifier le prérequis dans le bulletin applicable.');
    if(p.year!==2019 || ![1000,1046].includes(p.audio) || p.navigation_version!==1512 || norm(p.navdb)!=='943' || p.screen!=='horizontal') return result('HARDWARE_MATCH_REVIEW','Matériel correspondant, départ différent','Les références correspondent, mais l’année, les versions ou l’écran diffèrent du cas suivi.','Comparer précisément ces différences avec les sources avant toute préparation.',[],notes);
    return result('MATCHED_CASE','Correspond au cas documenté','Les informations saisies correspondent au départ du retour communautaire. Ce n’est pas une garantie ni un feu vert pour installer.','Lire la checklist des prérequis avec le guide ou un accompagnant ; garder les clés hors du véhicule pour cette préparation.',[],notes);
  }
  function prompt(profile,assessment) {
    return 'Aide-moi avec le guide https://github.com/toyrek/prius4-android-auto-retrofit . Lis AGENTS.md, docs/00-demarrer.md, docs/01-compatibilite.md et ai/PROMPT.md. Si tu ne peux pas les lire, demande leur contenu. Mes valeurs ci-dessous sont des saisies déclaratives, pas une certification. Ne complète pas les inconnues. Donne une seule action à la fois. Une écriture active exige de conserver l’alimentation et la clé, sans changement improvisé.\n\nMa fiche :\n'+JSON.stringify(profile,null,2)+'\n\nComparaison automatique (sans autorisation de flash) :\n'+JSON.stringify(assessment,null,2);
  }
  return {assess,prompt,fields};
});
