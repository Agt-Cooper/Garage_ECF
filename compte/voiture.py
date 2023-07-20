from compte.models import *
from pathlib import Path
import json

def voiture():
    file = Path.cwd() / "compte/voiture.json"
    with open(file, 'r', encoding='utf-8') as f:
        datas = json.load(f)
        
    for row in datas:     
        marq = Marque(nom=row['marque'])
        marq.save()     
        for mod in row['models']:
            try:
                mod = Modele(id=None, nom=mod, marque=marq)
                mod.save()            
            except:
                print(mod)