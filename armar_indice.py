import json,glob,os
fs=sorted([os.path.basename(f)[:-5] for f in glob.glob('datos/ediciones/*.json')],reverse=True)
json.dump({"ediciones":fs},open('datos/indice.json','w'),ensure_ascii=False)
# Índice de búsqueda con todas las notas de todas las ediciones
todas=[]
for f in fs:
    ed=json.load(open(f'datos/ediciones/{f}.json'))
    for sec,items in (ed.get('secciones') or {}).items():
        for n in items:
            todas.append({"ed":f,"sec":sec,**{k:n.get(k,"") for k in ("titulo","resumen","fuente","url","fecha","tema")}})
json.dump(todas,open('datos/busqueda.json','w'),ensure_ascii=False,separators=(',',':'))
print(len(fs),'ediciones,',len(todas),'notas en el buscador')
