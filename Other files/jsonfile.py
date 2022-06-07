import json


chemin = r'C:\Users\Mugiwara no nouha\Desktop\learn\lire_un_fichier\document\doc.json'


with open(chemin, 'w' ) as file:
    json.dump(list(range(5)), file, indent=4 ) #ecrire un list de 0 a 4 stocké dans file et indenté de 4
    
    # lire le fichier json
with open(chemin, 'r' ) as file:
    contenue = json.load(file)
    print(contenue)
    