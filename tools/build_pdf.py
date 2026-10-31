"""Build the community guide (requires reportlab). No Toyota PDF is embedded."""
from pathlib import Path
import html
import re
import textwrap
from urllib.parse import urljoin
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, CondPageBreak, Table, TableStyle, Preformatted, KeepTogether, Image

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://github.com/toyrek/prius4-android-auto-retrofit/'
OUTPUT = ROOT / 'downloads/Tutoriel-Prius-IV-Android-Auto.pdf'
OUTPUT.parent.mkdir(exist_ok=True)

if Path('C:/Windows/Fonts/segoeui.ttf').exists():
    regular, bold, mono = 'C:/Windows/Fonts/segoeui.ttf', 'C:/Windows/Fonts/segoeuib.ttf', 'C:/Windows/Fonts/consola.ttf'
else:
    regular, bold, mono = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
for name,path in [('Guide',regular),('GuideBold',bold),('GuideMono',mono)]:
    pdfmetrics.registerFont(TTFont(name,path))
pdfmetrics.registerFontFamily('Guide',normal='Guide',bold='GuideBold',italic='Guide',boldItalic='GuideBold')
navy=colors.HexColor('#16324f'); teal=colors.HexColor('#087e83')
styles={
 'body':ParagraphStyle('body',fontName='Guide',fontSize=9.2,leading=12.8,spaceAfter=6,textColor=navy),
 'h1':ParagraphStyle('h1',fontName='GuideBold',fontSize=20,leading=25,spaceAfter=16,textColor=navy,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='GuideBold',fontSize=12,leading=16,spaceBefore=10,spaceAfter=6,textColor=teal,keepWithNext=True),
 'cell':ParagraphStyle('cell',fontName='Guide',fontSize=8,leading=11,spaceAfter=0,textColor=navy),
 'code':ParagraphStyle('code',fontName='GuideMono',fontSize=7,leading=10,spaceAfter=9,backColor=colors.HexColor('#f2f5f7'),borderPadding=6),
}

def clean(text):
    return text.replace('→',' > ').replace('–','-').replace('—','-').replace('\u2011','-').replace('\u00a0',' ')

def inline(text,source):
    text=clean(text)
    # Resolve local Markdown targets to the public repository for offline PDFs.
    def link(m):
        label,target=m.groups()
        if not target.startswith(('http://','https://')):
            rel=(source.parent / target).resolve().relative_to(ROOT).as_posix()
            target=URL+'blob/main/'+rel
        return f'<link href="{html.escape(target,quote=True)}" color="#087e83">{html.escape(label)}</link>'
    tokens=[]
    def stash(m):
        tokens.append(link(m)); return f'ZZLINK{len(tokens)-1}ZZ'
    text=re.sub(r'\[([^]]+)\]\(([^)]+)\)',stash,text)
    text=html.escape(text)
    text=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',text)
    text=re.sub(r'`([^`]+)`',r'<font name="GuideMono">\1</font>',text)
    for i,token in enumerate(tokens): text=text.replace(f'ZZLINK{i}ZZ',token)
    return text

def content(source):
    lines=source.read_text(encoding='utf-8').splitlines(); out=[]; i=0
    while i<len(lines):
        line=lines[i]
        if not line.strip(): i+=1; continue
        picture=re.fullmatch(r'!\[([^]]*)\]\(([^)]+)\)',line.strip())
        if picture:
            alt,target=picture.groups()
            path=(source.parent/target).resolve()
            if path.suffix=='.svg': path=path.with_suffix('.png')
            if not path.is_relative_to(ROOT) or not path.exists():
                raise ValueError(f'Missing local illustration: {target}')
            img=Image(str(path))
            ratio=174*mm/img.imageWidth
            img.drawWidth=174*mm; img.drawHeight=img.imageHeight*ratio
            out.extend([img,Spacer(1,9)])
            i+=1; continue
        if line.startswith('```'):
            code=[]; i+=1
            while i<len(lines) and not lines[i].startswith('```'):
                code.extend(textwrap.wrap(clean(lines[i]),width=100,replace_whitespace=False,drop_whitespace=False) or [''])
                i+=1
            out.append(KeepTogether([Preformatted('\n'.join(code),styles['code'])])); i+=1; continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                row=[x.strip() for x in lines[i].strip('|').split('|')]
                if not all(re.fullmatch('[: -]+',x) for x in row):
                    rows.append([Paragraph(inline(x,source),styles['cell']) for x in row])
                i+=1
            width=174*mm
            table=Table(rows,colWidths=[width/len(rows[0])]*len(rows[0]),repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dbecef')),('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#d4dde4')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
            out.extend([table,Spacer(1,8)]); continue
        if line.startswith('# '):
            out.append(Paragraph(inline(line[2:],source),styles['h1'])); i+=1; continue
        if line.startswith('## '):
            out.append(Paragraph(inline(line[3:],source),styles['h2'])); i+=1; continue
        if line.startswith('- ') or re.match(r'^\d+\. ',line):
            out.append(Paragraph(inline(line,source),styles['body'])); i+=1; continue
        paragraph=[line]; i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','```','- ')) and not re.match(r'^\d+\. ',lines[i]):
            paragraph.append(lines[i]); i+=1
        out.append(Paragraph(inline(' '.join(paragraph),source),styles['body']))
    return out

def footer(canvas,doc):
    canvas.setStrokeColor(colors.HexColor('#d4dde4')); canvas.line(18*mm,17*mm,192*mm,17*mm)
    canvas.setFont('Guide',7); canvas.setFillColor(navy)
    canvas.drawString(18*mm,12*mm,'toyrek / Prius IV Android Auto - v1.1.0 - 31 octobre 2026')
    canvas.drawRightString(192*mm,12*mm,str(doc.page))

story=[Spacer(1,15*mm),Paragraph('PRIUS IV',ParagraphStyle('cover',parent=styles['h1'],fontSize=34,leading=40)),
 Paragraph('Android Auto avec le poste Toyota d’origine',styles['h1']),Spacer(1,10*mm),
 Paragraph('Tutoriel communautaire et retour d’expérience',styles['h2']),
 Paragraph('Panasonic 86140-47490 / MEU 86840-06041 / JBL',styles['body']),
 Paragraph('Audio 1046 préalable, puis clés 1 > 2 > 1 > 3 > 2',styles['h2']),
 Spacer(1,10*mm),Paragraph('<b>Un cas réussi, pas une compatibilité universelle.</b> Le propriétaire a confirmé Android Auto filaire le 30 octobre 2026. L’adaptation Prius reste non officielle ; une interruption ou des fichiers inadaptés peuvent rendre le poste inutilisable.',styles['body']),
 Paragraph('Lire la compatibilité et toutes les étapes avant de brancher une clé. Les clés 1 et 3 peuvent démarrer automatiquement.',styles['body']),
 Spacer(1,6*mm),Image(str(ROOT/'assets/parcours.png'),width=174*mm,height=174*mm*355/1200),Spacer(1,8*mm),
 Paragraph('<link href="https://toyrek.github.io/prius4-android-auto-retrofit/" color="#087e83">Ouvrir le formulaire et le guide interactif</link>',styles['body']),
 Paragraph(f'<link href="{URL}" color="#087e83">github.com/toyrek/prius4-android-auto-retrofit</link>',styles['body']),
 Paragraph('Version 1.1.0 - 31 octobre 2026. Documents originaux CC BY 4.0. Projet indépendant de Toyota. Les liens du PDF sont cliquables.',styles['body'])]
for index,file in enumerate(sorted((ROOT/'docs').glob('*.md'))):
    story.append(PageBreak() if index == 0 or file.name.startswith('04-') else CondPageBreak(70*mm))
    if index > 0 and not file.name.startswith('04-'): story.append(Spacer(1,10*mm))
    story.extend(content(file))
doc=SimpleDocTemplate(str(OUTPUT),pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=19*mm,bottomMargin=23*mm,
    title='Prius IV - Android Auto - Tutoriel communautaire',author='toyrek',subject='Configuration Panasonic JBL documentée ; tutoriel non officiel',pageCompression=1)
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUTPUT)
