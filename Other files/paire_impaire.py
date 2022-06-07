# Exercice 1 :
# 1. Écrire un programme Python qui permet de remplir un tableau à une dimension d’entiers
# de taille N et détermine le nombre de valeurs paires et impaires.

array_paire = []
array_impaire = []

#Moi je choisis 10 comme la taille du tableau
for i in range(10):
    nombre = int(input("Entrez un nombre : \n"))
    if nombre % 2 == 0:
        array_paire.append(nombre)
        nombre_valeur_paire = len(array_paire)
    elif nombre % 2 != 0 :
        array_impaire.append(nombre)
        nombre_valeur_impaire = len(array_impaire)
        
print(f"Le nombre de valeur paire : {nombre_valeur_paire}\n Le nombre de valeur impaire : {nombre_valeur_impaire}")

# Pour afficher les valeurs paire du tableau : print(array_paire)
# Pour afficher les valeurs impaire du tableau : print(array_impaire)

