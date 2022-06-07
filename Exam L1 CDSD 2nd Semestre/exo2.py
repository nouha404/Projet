#ABOUBACAR MAREGA L1 CDSD 770811045

vie = 0

while True:
   
    face = int(input('Entrez la face du dée : \n'))
    user2 = int(input('Devinez la face : \n'))
    
    if face == user2:
        print(f'Bravo vous avez deviner la face avec {vie} tentative')
        break
    elif face != user2:
        print('Try again')
    elif face < 0 and face >= 7:
        print('Entrez une face compris entre 1 et 6 inclus : \n')
        
    vie += 1
        
    
