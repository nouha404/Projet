import random

# r = random.randint(0,100) #pour les entier
# print(r)

# r = random.randrange(0,101,2) #
# print(r)


a = random.randint(0,100);
b = random.randint(0,100);

if a == b :
     print(f"Le nombre {a} et le nombre {b} sont égaux")
elif b > a :
    print(f"Le nombre {b} est plus grand que le nombre {a}")
else:
    print(f"Le nombre {a} est plus grand que le nombre {b}")



"""_summary_
Il faut dabord importer le module random
import random

la fonction randint(0,100) permet de generer des nombre entier
dans un intervale ici qui est de 0 a 100 inclus

Pour les nombre decimales on utilise la fonction uniform

code

import random

r = random.randint(0,100) #pour les entier
print(r)

r = random.uniform(0,100) #pour les nombres decimales
print(r)

La fonction randrange accepte lui la valeur de fin exclu
Il a une avantage d'avoir un nombre de pas 

r = random.randrange(0,101,2) #
print(r)

On commence de 0, on va jusqu'a 100 et par pas de 2



    """