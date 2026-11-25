#!/usr/bin/env python3
"""Sincroniza este repo con PORTAL-B2B-EPM-LUIS y genera DOS juegos de portales:
  - FREELANCE (vendedor 'Freelance')  -> *_f.html, portal_b2b_FREELANCE.html, ...
  - MANUEL    (vendedor 'Manuel')     -> *_MANUEL.html
Ambos viven en este repo (PORTAL-B2B-EPM-FREELANCE) y comparten la carpeta images/.
Solo cambia: titulos sin "(Luis)", vendedor, links al repo y nombres de archivo.
NUNCA borra archivos (los portales de Manuel y los atajos no deben perderse).
Uso: python3 tools/sync_from_luis.py <clon_luis> <este_repo>"""
import os, re, shutil, sys, glob
src, dst = sys.argv[1], sys.argv[2]
REPO = 'PORTAL-B2B-EPM-FREELANCE'
SETS = {
  'Freelance': {'portal_b2b_LUIS.html':'portal_b2b_FREELANCE.html','portal_b2b_ofertas_l.html':'portal_b2b_ofertas_f.html',
                'capilar_l.html':'capilar_f.html','fragancias_l.html':'fragancias_f.html','mascotas_l.html':'mascotas_f.html',
                'portal_frag_luis.html':'portal_frag_freelance.html','portal_fragancias_luis.html':'portal_fragancias_freelance.html'},
  'Manuel':    {'portal_b2b_LUIS.html':'portal_b2b_MANUEL.html','portal_b2b_ofertas_l.html':'portal_b2b_ofertas_MANUEL.html',
                'capilar_l.html':'capilar_MANUEL.html','fragancias_l.html':'fragancias_MANUEL.html','mascotas_l.html':'mascotas_MANUEL.html'},
}
ALLREN = {}
for s in SETS.values(): ALLREN.update(s)
def conv(c, vendedor, ren):
    c = c.replace(' (Luis)', '').replace("vendedor:'Luis'", "vendedor:'%s'" % vendedor)
    c = c.replace('PORTAL-B2B-EPM-LUIS', REPO)
    c = re.sub(r'/'+REPO+r'/[0-9a-f]{40}/', '/'+REPO+'/main/', c)
    c = c.replace('/camilaparra92/'+REPO+'/', '/CamilaParra92/'+REPO+'/')
    for a, b in ren.items(): c = c.replace(a, b)
    return c
si, di = os.path.join(src,'images'), os.path.join(dst,'images'); os.makedirs(di, exist_ok=True)
for f in os.listdir(si): shutil.copy2(os.path.join(si,f), os.path.join(di,f))
for vend, ren in SETS.items():
    for a, b in ren.items():
        p = os.path.join(src, a)
        if not os.path.exists(p): print('AVISO: no existe en Luis', a); continue
        with open(os.path.join(dst, b), 'w', encoding='utf-8', newline='') as fh:
            fh.write(conv(open(p, encoding='utf-8').read(), vend, ren))
bad = [os.path.basename(p) for p in glob.glob(os.path.join(dst,'*.html')) if 'luis' in open(p,encoding='utf-8').read().lower()]
if bad: print('AVISO: quedan referencias a luis en', bad)
