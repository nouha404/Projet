# Dans cet exercice, vous allez devoir vérifier la validité 
# d'un mot de passe à l'aide de structures conditionnelles 
# et de méthodes vues au cours de cette section.

# password = input("Entrez votre mots de passe : \n")

# if len(password) > 8:
#     print("Votre password contient plus de 8 caracteres")
# else:
#     print("Veillez entrez un password d'aumoins 8 caracteres")

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

if len(mdp) == 0:
    print(mdp_trop_court.upper())
elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
elif len(mdp) < 8:
    print(mdp_trop_court.title())
else:
    print("Inscription terminée.")