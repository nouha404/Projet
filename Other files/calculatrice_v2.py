# Dans ce projet, vous devez créer une calculatrice en ligne de commande 
# qui demande à l'utilisateur de saisir deux nombres et qui affiche ensuite le résultat de l'addition de ces deux nombres.
# Vous devez également gérer le cas de figure dans lequel l'utilisateur ne rentre pas de données valides


# On déclare deux variables
a = b = ""

# Tant que a et b ne sont pas des nombres, on boucle
while not (a.isdigit() and b.isdigit()):
    
    # On demande deux nombres à l'utilisateur
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    
    # On affiche une phrase si les nombres entrés ne sont pas valides.
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")

# On affiche le résultat de l'addition
print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")