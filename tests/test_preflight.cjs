const assert=require('node:assert/strict');
const test=require('node:test');
const {assess,prompt}=require('../guide/preflight.js');
const sample=require('../ai/vehicle.example.json');
const cases=[
  ['cas documenté',{},'MATCHED_CASE'],
  ['préalable déjà fait',{audio:1046},'MATCHED_CASE'],
  ['carte inconnue',{navdb:null},'MISSING'],
  ['carte autre',{navdb:'A36'},'HARDWARE_MATCH_REVIEW'],
  ['audio plus récent',{audio:1100},'HARDWARE_MATCH_REVIEW'],
  ['autre année',{year:2017},'HARDWARE_MATCH_REVIEW'],
  ['référence absente',{dcu_part:''},'MISSING'],
  ['référence autre',{dcu_part:'86140-12345'},'OTHER_CONFIGURATION'],
  ['sans JBL',{jbl:false},'OTHER_CONFIGURATION'],
  ['sans navigation',{navigation:false},'OTHER_CONFIGURATION'],
  ['poste remplacé',{original_unit:false},'OTHER_CONFIGURATION'],
  ['USA',{market:'usa'},'OUTSIDE_GUIDE'],
  ['Japon',{market:'japan'},'OUTSIDE_GUIDE'],
  ['grand écran',{screen:'vertical11'},'OUTSIDE_GUIDE'],
  ['Denso',{manufacturer:'denso'},'OUTSIDE_GUIDE'],
  ['Prime',{vehicle:'prime'},'OUTSIDE_GUIDE'],
  ['Corolla',{vehicle:'corolla'},'OEM_ROUTE'],
  ['RAV4',{vehicle:'rav4'},'OEM_ROUTE'],
  ['déjà fonctionnel',{android_auto_works:true},'ALREADY_WORKING'],
  ['déjà converti',{dcu_id:'17TDT2EU-DA31',meu_id:'17TMT2EU-FA10'},'CONVERTED_REVIEW'],
  ['MEU converti seulement',{meu_id:'17TMT2EU-FA10'},'PARTIAL_REVIEW'],
  ['DCU converti seulement',{dcu_id:'17TDT2EU-DA31'},'PARTIAL_REVIEW'],
  ['rétrofit commencé',{conversion_started:true},'PARTIAL_REVIEW'],
  ['écriture prioritaire',{update_in_progress:true,android_auto_works:true,market:'usa'},'IN_PROGRESS'],
  ['état inconnu',{update_in_progress:null},'MISSING'],
  ['booléen texte refusé',{jbl:'false'},'INVALID_INPUT'],
  ['version texte refusée',{audio:'1046'},'INVALID_INPUT'],
  ['version négative refusée',{audio:-1},'INVALID_INPUT'],
  ['choix invalide',{market:'moon'},'INVALID_INPUT']
];
for(const [name,changes,code] of cases) test(name,()=>{
  const input={...sample,...changes}; const before=JSON.stringify(input); const r=assess(input);
  assert.equal(r.code,code); assert.equal(r.flash_authorized,false); assert.equal(JSON.stringify(input),before);
});
test('aucune donnée ne devient une compatibilité',()=>assert.equal(assess({}).code,'MISSING'));
test('entrée vide/null tolérée sans autorisation',()=>assert.equal(assess(null).flash_authorized,false));
test('message IA conserve les inconnues et résultat',()=>{
  const input={dcu_part:null}; const text=prompt(input,assess(input));
  assert.match(text,/"dcu_part": null/); assert.match(text,/"flash_authorized": false/); assert.match(text,/AGENTS.md/);
});
