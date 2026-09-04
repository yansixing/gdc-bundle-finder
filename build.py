#!/usr/bin/env python3
"""Build index.html and gdc_index.csv from zip_listings.json (zip central-directory listings)."""
import json,csv,re,os
D=os.path.dirname(os.path.abspath(__file__))
data=json.load(open(f'{D}/zip_listings.json',encoding='utf-8'))
YEARMAP={'2023':'2021-2023'}
URL={
 '2015':('https://downloads.sonniss.com/Sonniss.com%20-%20GDC%20-%20Game%20Audio%20Bundle%20','of5.zip'),
 '2016':('https://downloads.sonniss.com/Sonniss.com%20-%20GDC%202016-%20Game%20Audio%20Bundle%20Part%20','of6.zip'),
 '2017':('https://downloads.sonniss.com/Sonniss.com%20-%20GDC%202017%20-%20Game%20Audio%20Bundle%20Part%20','of9.zip'),
 '2018':('https://downloads.sonniss.com/Sonniss.com%20-%20GDC%202018%20-%20Game%20Audio%20Bundle%20Part%20','of8.zip'),
 '2019':('https://downloads.sonniss.com/Sonniss.com%20-%20GDC%202019%20-%20Game%20Audio%20Bundle%20Part%20','of8.zip'),
 '2020':('https://downloads.sonniss.com/Sonniss.com%20-%20GDC%202020%20-%20Game%20Audio%20Bundle%20Part','of14.zip'),
 '2021-2023':('https://downloads.sonniss.com/Sonniss.com-GDC2023-GameAudioBundle','of14.zip'),
 '2024':('https://downloads.sonniss.com/Sonniss.com-GDC2024-GameAudioBundle','of9.zip')}
order=['2015','2016','2017','2018','2019','2020','2021-2023','2024']
zips={y:{} for y in order};libs={};LIBS=[];FILES=[]
for k,v in data.items():
    y,p=k.split('/');y=YEARMAP.get(y,y);p=int(p)
    zips[y][p]=[v['gb'],URL[y][0]+str(p)+URL[y][1]]
    for nm,sz in v['files']:
        parts=nm.split('/')
        if parts and parts[0].startswith('Sonniss.com'): parts=parts[1:]
        if len(parts)<2 or '__MACOSX' in parts or parts[-1].startswith('._'): continue
        folder,fn=parts[0].strip(),'/'.join(parts[1:])
        if not re.search(r'\.(wav|flac|aif|aiff|mp3|ogg)$',fn,re.I): continue
        key=(y,p,folder)
        if key not in libs: libs[key]=len(LIBS);LIBS.append([y,p,folder])
        FILES.append([libs[key],fn,round(sz/2**20,1)])
idx=sorted(range(len(LIBS)),key=lambda i:(order.index(LIBS[i][0]),LIBS[i][1],LIBS[i][2].lower()))
remap={old:new for new,old in enumerate(idx)}
LIBS=[LIBS[i] for i in idx]
FILES=sorted(([remap[f[0]],f[1],f[2]] for f in FILES),key=lambda f:(f[0],f[1].lower()))
zips={y:{p:zips[y][p] for p in sorted(zips[y])} for y in order}
SAMPLES={}
for y in order:
    names=[l[2].split(' - ',1)[-1] for l in LIBS if l[0]==y]
    pick=[n for n in names if re.search(r'horror|creature|monster|cave|underground|creak|drone|wind|water|footstep|gore|ambien|forest|metal|door',n,re.I)]
    seen=set();out=[]
    for n in pick:
        if n.lower() in seen: continue
        seen.add(n.lower());out.append(n)
        if len(out)==5: break
    SAMPLES[y]=out
J=lambda o:json.dumps(o,ensure_ascii=False,separators=(',',':'))
blob=f'const ORDER={J(order)};\nconst ZIPS={J(zips)};\nconst LIBS={J(LIBS)};\nconst FILES={J(FILES)};\nconst SAMPLES={J(SAMPLES)};'
tpl=open(f'{D}/template.html',encoding='utf-8').read()
assert '/*__DATA__*/' in tpl
open(f'{D}/index.html','w',encoding='utf-8').write(tpl.replace('/*__DATA__*/',blob))
with open(f'{D}/gdc_index.csv','w',newline='',encoding='utf-8') as fh:
    w=csv.writer(fh);w.writerow(['YEAR','PART','ZIP_GB','SUPPLIER - LIBRARY','FILENAME','SIZE_MB','ZIP_URL'])
    for f in FILES:
        l=LIBS[f[0]];z=zips[l[0]][l[1]];w.writerow([l[0],l[1],z[0],l[2],f[1],f[2],z[1]])
print('index.html',round(os.path.getsize(f'{D}/index.html')/1024),'KB; libs',len(LIBS),'files',len(FILES))
