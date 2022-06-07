from pathlib import Path
import shutil # pour supprimer un dossier
p = Path.cwd()
p = p / 'module_path'
p = p / 'DossierTest'
p = p / 'one_piece' / 'ohara'
# p.mkdir(parents=True) creer un sous- dossier a l'interieur  sans erreur
p = p.parent.parent
p = Path.cwd()
print(p)

