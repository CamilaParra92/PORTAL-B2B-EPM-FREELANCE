#!/usr/bin/env python3
"""Sincroniza este repo (FREELANCE) con PORTAL-B2B-EPM-LUIS.
Copia todos los HTML y la carpeta images/ desde Luis, aplicando solo estas diferencias:
  - quita el nombre "(Luis)" de los titulos
  - vendedor 'Luis' -> 'Freelance'
  - links al repo PORTAL-B2B-EPM-LUIS -> PORTAL-B2B-EPM-FREELANCE
  - renombra archivos (ver REN)
Uso: python3 tools/sync_from_luis.py <ruta_clon_luis> <ruta_este_repo>
"""
import os, re, shutil, sys, glob
src, dst = sys.argv[1], sys.argv[2]
REN = {'portal_b2b_LUIS.html':'portal_b2b_FREELANCE.html','portal_b2b_ofertas_l.html':'portal_b2b_ofertas_f.html',
       'capilar_l.html':'capilar_f.html','fragancias_l.html':'fragancias_f.html','mascotas_l.html':'mascotas_f.html',
       'portal_frag_luis.html':'portal_frag_freelance.html','portal_fragancias_luis.html':'portal_fragancias_freelance.html'}
def conv(c):
    c = c.replace(' (Luis)', '').replace("vendedor:'Luis'", "vendedor:'Freelance'")
    c = c.replace('PORTAL-B2B-EPM-LUIS', 'PORTAL-B2B-EPM-FREELANCE')
    c = re.sub(r'/PORTAL-B2B-EPM-FREELANCE/[0-9a-f]{40}/', '/PORTAL-B2B-EPM-FREELANCE/main/', c)
    c = c.replace('/camilaparra92/PORTAL-B2B-EPM-FREELANCE/', '/CamilaParra92/PORTAL-B2B-EPM-FREELANCE/')
    for a, b in REN.items(): c = c.replace(a, b)
    return c
# imagenes
si, di = os.path.join(src, 'images'), os.path.join(dst, 'images')
os.makedirs(di, exist_ok=True)
for f in os.listdir(si):
    shutil.copy2(os.path.join(si, f), os.path.join(di, f))
# html
seen = set()
for p in glob.glob(os.path.join(src, '*.html')):
    name = os.path.basename(p); out = REN.get(name, name); seen.add(out)
    c = conv(open(p, encoding='utf-8').read())
    with open(os.path.join(dst, out), 'w', encoding='utf-8', newline='') as fh: fh.write(c)
for p in glob.glob(os.path.join(dst, '*.html')):
    if os.path.basename(p) not in seen: os.remove(p)
leftover = [os.path.basename(p) for p in glob.glob(os.path.join(dst, '*.html')) if 'luis' in open(p, encoding='utf-8').read().lower()]
if leftover: print('AVISO: quedan referencias a luis en', leftover)
