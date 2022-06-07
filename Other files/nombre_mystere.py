# Le but de ce projet est de recréer
# le jeu du nombre mystère dans lequel le joueur doit trouver un nombre aléatoire généré par l'ordinateur.

import random

vie = 5
nombre_random = random.randrange(0,101);
print(f"🏆🏆🏆 Le jeu du nombre mystere 🏆🏆🏆")


while vie > 0:
    nombre = int(input("Devine le nombre : "))
    vie -= 1
    
    if vie == 0 and nombre_random != nombre:
        print(f"Dommage ! le nombre mystere était {nombre_random}")
        break
    
    elif nombre_random == nombre:
        print(f"Bravo ! Le nombre mystere était bien {nombre_random} !") 
        print(f"Tu as trouvé le nombre mystere en {vie} essais")
        print("Fin du jeu")
        break
    
    elif nombre_random < nombre:
         print(f"Le nombre mystere est plus petit que {nombre}")
         print(f"Il te reste {vie} essais")
         
    elif nombre_random > nombre :
         print(f"Le nombre mystere est plus grand que {nombre}")
         print(f"Il te reste {vie} essais")
         
    else:
         print(f"Veillez entrer un nombre valide.")
         print(f"Il te reste {vie} essais")
#Gerer le cas ou il rentre autre chose qu'un nombre ...  print(f"Veillez entrer un nombre valide.") print(f"Il te reste {vie} essais")

        
    
    
    


    
 