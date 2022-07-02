from pathlib import Path


# p = Path(r'C:\Users\Mugiwara no nouha\Downloads')
#iterdir() recupere all dir and file
# print(p)
# for i in p.rglob('*.png'):
#     print(i.name)
    
# is_dir
# glob . avec glob on utilise pas iterdir()
# rglob agit de facon recurssive
# p.glob(*.png)
#    

# p = Path(r'C:\Users\Mugiwara no nouha\Desktop\learn\module_path\docu.txt')

# p = p.parent / p.stem 
# p = p.parent / (p.stem + 'cument10' + p.suffix)

# print(p)




# Avec Path
# FOLDER_PARENT = SOURC.parent #le dossier parent du script
# SOURC = Path(__file__).resolve() ##recuperer le vrai chemain du script
# ROOT = FOLDER_PARENT.parent #lz parent du parent
SOURC = Path(r'C:\Users\Mugiwara no nouha\Downloads')
print(SOURC)


for p in SOURC.rglob('*.mp4'):
    print(p.name)

