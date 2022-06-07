from pathlib import Path
import glob
import os

# p = Path(r'C:\Users\Mugiwara no nouha\Downloads')
#iterdir() recupere all dir and file
# print(p)
# for i in p.rglob('*.png'):
#     print(i.name)
    
# is_dir
# glob . avec glob on utilise par iterdir()
# rglob agit de facon recurssive
# p.glob(*.png)
#    

# p = Path(r'C:\Users\Mugiwara no nouha\Desktop\learn\module_path\docu.txt')

# p = p.parent / p.stem 
# p = p.parent / (p.stem + 'cument10' + p.suffix)

# print(p)


SOURCES = os.path.realpath(__file__) ##recuperer le vrai chemain du script
FOLDER_SOURCE = os.path.dirname(__file__) #le dossier parent du script


# Avec Path
SOURC = Path(__file__).resolve() ##recuperer le vrai chemain du script
FOLDER_PARENT = SOURC.parent #le dossier parent du script
ROOT = FOLDER_PARENT.parent #lz parent du parent
print(FOLDER_PARENT)