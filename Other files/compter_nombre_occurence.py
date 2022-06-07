# from unittest import result


# nous cherchons le nombre de fois que la lettre 'o' apparait dans la phrase "Bonjour tout le monde"

# Votre script devra retourner dans ce cas-ci dans une variable result le nombre 4

lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
resultat = phrase.count(lettre_a_chercher)
print(resultat)






"""_code_
    lettre_a_chercher = "o"
    phrase = "Bonjour tout le monde"
    resultat = phrase.lower().count(lettre_a_chercher)
    
    EXPLICATIONS

Pour compter le nombre d'occurrences d'une lettre dans une chaîne de caractère,
on utilise la fonction count.
Afin d'éviter toute confusion quant aux majuscules et minuscules,
nous prenons le soin de convertir auparavant notre chaîne de caractère en minuscule 
avec la fonction lower.
"""