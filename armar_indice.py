import json,glob,os
fs=sorted([os.path.basename(f)[:-5] for f in glob.glob('datos/ediciones/*.json')],reverse=True)
json.dump({"ediciones":fs},open('datos/indice.json','w'),ensure_ascii=False)
print(len(fs),'ediciones')
