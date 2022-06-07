#ABOUBACAR MAREGA L1 CDSD 770811045

som = 0
for i in range(1,4):
    nombre = int(input('Entrez un nombre impaire : \n'))
    
    while nombre % 2 == 0:
        nombre = int(input('Entrez un nombre impaire : \n'))
        if nombre % 2 != 0:
            continue
    
    if nombre % 2 != 0:
        som += nombre
print(f'La somme des nombres impaires est de : {som}')
   