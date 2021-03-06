# Le chiffrement de César original décale chaque caractère d'une unité : a devient b, z devient a, et ainsi de suite. Rendons les choses un peu plus difficiles et permettons à la valeur décalée de provenir de la plage 1..25 inclus.

# De plus, laissez le code préserver la casse des lettres (les lettres minuscules resteront en minuscules) et tous les caractères non alphabétiques doivent rester intacts.

# Votre tâche consiste à écrire un programme qui :

# demande à l'utilisateur une ligne de texte à chiffrer ;
# demande à l'utilisateur une valeur de décalage (un nombre entier compris entre 1 et 25 - remarque : vous devez forcer l'utilisateur à saisir une valeur de décalage valide (n'abandonnez pas et ne laissez pas les mauvaises données vous tromper !)
# imprime le texte encodé.

# Exemple d'entrée :
# abcxyzABCxyz 123
# 2

# Exemple de sortie :
# cdezabCDEzab 123