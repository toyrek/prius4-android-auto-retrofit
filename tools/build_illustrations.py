"""Original schematic illustrations, deterministic SVG, no photos or vehicle IDs."""
from pathlib import Path
from html import escape

OUT=Path(__file__).resolve().parents[1]/'assets'; OUT.mkdir(exist_ok=True)
NAVY='#17334b'; TEAL='#087e83'; LIGHT='#edf6f5'; ORANGE='#ab5914'

def text(x,y,value,size=22,fill=NAVY,weight=400):
    return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(value)}</text>'
def rect(x,y,w,h,fill='#fff',stroke='none',r=18):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>'
def save(name,h,title,description,body):
    content=f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>'+rect(0,0,1200,h,'#f4f8fa',r=24)+''.join(body)+'</svg>'
    (OUT/f'{name}.svg').write_text(content,encoding='utf-8')

body=[text(40,56,'Android Auto sur Prius IV : commencer par le bon poste',30,weight=700),text(40,91,'Un guide communautaire. Une configuration réussie, pas tous les autoradios.',20)]
cards=[('1','IDENTIFIER','Relever DCU, MEU, versions','Sans clé de mise à jour.'),('2','COMPARER','Vérifier matériel et prérequis','Une inconnue reste inconnue.'),('3','PRÉPARER','Contrôler les fichiers et les clés','Suivre ensuite le tutoriel.')]
for i,(n,title,a,b) in enumerate(cards):
    x=40+i*382
    body += [rect(x,125,354,200),rect(x+20,145,50,50,TEAL,r=25),text(x+37,179,n,26,'white',700),text(x+20,225,title,24,weight=700),text(x+20,263,a,20),text(x+20,297,b,18,TEAL)]
save('parcours',355,'Identifier, comparer, préparer','Trois étapes avant toute installation : identifier le poste sans clé, comparer la configuration, puis préparer les supports.',body)

body=[text(40,56,'Que faut-il relever dans la voiture ?',30,weight=700),text(40,91,'Menu > Configuration / SETUP > Général > Mise à jour du logiciel',20),rect(40,126,695,366,NAVY),rect(60,145,655,328,'#fff',r=12),text(82,180,'EXEMPLE PÉDAGOGIQUE - pas une capture réelle',18,TEAL,700)]
rows=[('Model ID DCU','17TDT2EU-DA01'),('Model ID MEU','17TMT2EU-FA00'),('Audio','1000'),('Navigation','1512'),('navdb_version','943')]
for i,(k,v) in enumerate(rows):
    y=219+i*48
    body +=[text(84,y,k,22,weight=700),text(380,y,v,23),f'<path d="M82 {y+14} H690" stroke="#dbe6eb"/>']
body += [text(770,162,'DCU : unité principale',23,weight=700),text(770,197,'MEU : module de navigation',22),text(770,250,'Audio / Navigation',23,weight=700),text(770,285,'= versions des logiciels',21),text(770,338,'navdb_version',23,weight=700),text(770,373,'= version des cartes',21),text(770,431,'Recopier VOS valeurs.',23,TEAL,700),text(770,465,'Sinon : « inconnu ».',21),text(40,540,'À relever aussi : références de pièces, fabricant, région, JBL, navigation, DAB et CD.',22),text(40,580,'Masquer VIN et numéros de série. L’apparence de l’écran ne prouve pas la compatibilité.',20,ORANGE)]
save('identifier',620,'Lire les identifiants de son autoradio','Exemple fictif reprenant les valeurs avant conversion du cas documenté. Relever ses propres valeurs et masquer les identifiants uniques.',body)

body=[text(40,54,'Le parcours du cas Panasonic / JBL documenté',30,weight=700),text(40,92,'Seulement après identification, prérequis examinés et fichiers vérifiés.',21),rect(40,121,1120,60,'#fff4e5'),text(62,160,'Avant : Audio 1000 vers 1046, avec un support séparé dans notre cas.',23,ORANGE,700)]
steps=[('1','Préparation','Attendre DONE',TEAL),('2','Navigation','FA10 / 1120',NAVY),('1','Réplication','Attendre FINISHED',TEAL),('3','Conversion DCU','Vérifier DA31','#9a6424'),('2','Finalisation','Audio 1075',NAVY)]
for i,(num,label,sub,color) in enumerate(steps):
    x=40+i*228
    body += [rect(x,209,208,230),rect(x+64,229,80,94,color),rect(x+79,219,50,20,'#b8c9d3',r=3),text(x+91,292,num,42,'#fff',700),text(x+16,366,label,20,weight=700),text(x+16,403,sub,18)]
    if i<4: body += [text(x+211,291,'›',30,TEAL,700)]
body += [text(40,491,'READY • dehors • P • frein serré',24,TEAL,700),text(40,529,'Garder la clé et l’alimentation pendant l’écriture.',22),text(40,565,'Retraits et redémarrages : suivre le message prévu à chaque étape du tutoriel.',20)]
save('cles',600,'Ordre des clés 1, 2, 1, 3, 2','Cas documenté uniquement. Audio préalable si nécessaire puis cinq passages avec trois clés. Les messages de fin déterminent les actions.',body)
print('3 illustrations SVG générées')
