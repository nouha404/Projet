# 4. Écrire un algorithme Python qui renvoie la liste des diviseurs d’un entier donné.
# Exemple si n = 18, l’algorithme renvoie la liste [1, 2, 3, 6, 9, 18].

array_diviseur = []
nombre = int(input("Entrez un nombre : \n"))

for i in range(1,nombre + 1):
    if i % 2 == 0:
        array_diviseur.append(i)
print(array_diviseur)
        