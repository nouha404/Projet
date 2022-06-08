from pathlib import Path

chemin = Path(__file__).resolve()
chemin_fichier = chemin.parent / 'readme.txt'

fichier = input('Entrez le fichier a ouvrir : ')

try:
    with open(chemin_fichier, 'r') as f:
        contenue = f.read()
        print(contenue)
        
except FileNotFoundError:
    print('Le fichier est introuvable ')
        
except UnicodeDecodeError:
    print("Impossible d'ouvrir ce fichier ")

