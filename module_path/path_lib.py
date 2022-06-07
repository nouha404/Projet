from pathlib import Path

p = Path(r'C:\Users\Mugiwara no nouha\Desktop\learn\module_path\docu.txt')

print(p.parent) #parent
print(p.stem) #avant le .txt
print(p.suffix) #suffix
print(p.suffixes) #tout les .tar.gz
print(p.name) #nom du document
print(p.parts) #tous les parti du chemin ex C User Mugiwara no nouha Desktop etc
print(p.exists()) #si le fichier existe ou pas
print(p.is_dir()) #si c un dosssier
print(p.is_file()) #si c'est un fichier