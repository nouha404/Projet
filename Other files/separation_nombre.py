# 2. Écrire un programme Python qui permet de remplir un tableau à une dimension d’entiers
# de taille N et sépare les nombres positifs et négatifs dans des tableaux différents

array_positif = []
array_negatif = []

for i in range(10):
    nombre = int(input("Entrez un nombre : \n"))
    array_negatif.append(nombre) if nombre > 0 else array_positif.append(nombre) 
print(f"Les nombres positifs du tableaux {array_positif.split} \n Les nombres négatifs : {array_negatif}")

# Méthode 2 :
array_positif = []
array_negatif = []

for i in range(10):
    nombre = int(input("Entrez un nombre : \n"))
    if nombre > 0:
        array_negatif.append(nombre)
    else:
        array_positif.append(nombre)
print(f"Les nombres positifs du tableaux {array_positif.split} \n Les nombres négatifs : {array_negatif}")
    
    