# Regles du jeu 
# Le but de ce projet est creer un jeu de role textuel dans le terminal
# Le jeu comporte deux joueurs : vous et Yonko
# Vous commencez toute les deux a 50 points de vie
# Votre personnage dispose de 3 potions qui vous permettent de recuperer des points de vie
# L'ennemi ne dispose d'aucune potion
# Chaque potion vous permet de récuperer un nombre aléatoire de points de vie, compris entre 15 et 50.
# Votre attaque inflige a l'ennemi des dégats aleatoires compris entre 5 et 10 points de vie.
# Lorsque vous utiliser une potion, vous passez le prochain tour

import random



while True:
    choix = int(input('Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? '))
    player_vie = 50
    yonko_vie = 50
    potion = random.randrange(15,51)
    player_attaque = random.randrange(5,11)
    yonko_attaque = random.randrange(5,16)
    nombre_potion = 3
    
 
    if choix == 2:
        player_vie += potion
        
        if nombre_potion < 0:
            nombre_potion -= 1
            if nombre_potion == 0:
                potion = 0
                print(f"Vous n'avez plus de potion...")
        else:
            print(f"Vous avez recuperer {player_vie} point de vie ({nombre_potion} restantes")
        
        
                       
            
        
        
            
            
            
## vie augmente d'un nombre aleatoire compris entre 5-10
# Afficher Vous passez votre tour ...
        
    # if choix == 1:
    #     print(f"Yonko vous a infligé {yonko_attaque} de dégats ")
    #     print(f"Il vous reste {player_vie} points de vie.")
        
            
        
            
                
                    
            
        
            
        
            
        
        
        
            
        
    # if player_vie < 0:
    #     player_vie -= attaque
    #     if choix == 1:
            
    #     # while yonko_vie < 0:    
    #     #     yonko_vie -= attaque
    #     #     print(f"Il reste {yonko_vie} de vie a Yonko.")
    #     #     print( '-' * 50)
        
        
        
        
    
    
#     if choix == 1:        
        
#         while player_vie < 0:
#             player_vie -= attaque
            
#             print(f"Il vous reste {player_vie} points de vie. ")
#         while yonko_vie < 0:
#             yonko_vie -= attaque
#             print(f"Il reste {yonko_vie} de vie a Yonko.")
            
#         print('-' * 50)
        
#         # attaque = random.randrange(5,11)
#         # yonko_vie_restant = yonko_vie - attaque

#     elif choix == 2:
#         player_vie += potion
#         nombre_potion -= 1
        
#         if nombre_potion == 0:
#             potion = 0
#             print("Vous n'avez plus de potions ...")
        
#         else:            
#             print(f"Vous avez recuperer {potion} point de vie ({nombre_potion} restantes)")
#             print("Vous passez votre tour..")
#         player_vie -= attaque
#         print(f"Yonko vous a infliger {attaque} points de dégats")
#         print(f"Il vous reste {player_vie} points de vie")
#         print(f"Il reste {yonko_vie} de vie a Yonko")
#     print('-' * 50)
            
#     #     attaque = random.randrange(5,11)
#     #     player_vie_restant -= attaque            
    
            
    
# # while player_vie > 0 or yonko_vie > 0:
# #     player_vie -= attaque
# #     yonko_vie -= attaque
    
        
    
        

# Tu vas te battre contre un ennemi, pouvoir attaquer, prendre une potion et te faire attaquer en retour.
# Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?
#Si son choix different de 1 ou 2 reafficher la premiere phrase
# si choix = 1 :
#Afficher L'enemi vous a infligé {degat aleatoire} de dégats 
# Reafficher Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?

# SI choix = 2 
# Afficher VOus avez recuperer {potion} point de vie ({potion-1} restantes)
## vie augmente d'un nombre aleatoire compris entre 5-10
# Afficher Vous passez votre tour ...
# L'ennemi vous a infliger {degat ennemie} points de dégats
# Vous reste {vie} points de vie
# Il reste {vie ennemie} de vie a l'ennemi
# -*50
# Reaffichez la premiere phrase : 

##le user a droit qu'a 3 potion qui varie de 15 a 50 vie
## si user essaye le choix 2 apres potion epuisé, Afficher "Vous n'avez plus de potions ..."
##Reafficher la premiere phrase

# Si vie user plus grand que ennemie AFFICHER Tu as gagnez Fin du jeu.
