import math

racine = math.sqrt(16)
print(racine)




"""_summary_
Si vous avez besoin d'effectuer des calculs mathématiques plus complexes, 
vous devrez utiliser le module math car pour ne pas trop surcharger les fonctions disponibles par défaut, 
Python ne charge pas toutes ces fonctions de base quand vous lancez un interpréteur.

Pour utiliser le module math, il faut l'importer comme ceci :
import math


math.ceil(-4.7) : entier immédiatement supérieur, donne ici -4:  Pour arrondir a l'unité le plus proche

math.exp(2) : exponentielle.

math.factorial(5) : factorielle 5, donc 120 ici (fonctionne uniquement pour les entiers positifs).

math.floor(-4.7) : partie entière, donne ici -5.

math.isinf(x) : teste si x est infini (inf) et renvoie True si c'est le cas.

math.log(2) : logarithme en base naturelle.

math.log(8, 2) : log de 8 en base 2.

math.log10(2) : logarithme en base 10.

math.pow(2, 3) : 2 puissance 3 (peut aussi s'écrire 2 ** 3).

math.sqrt(16) : racine carrée, donne ici 4.
    """