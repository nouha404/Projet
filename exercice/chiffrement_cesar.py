WORDLIST = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
        'p','q','r','s','t','u','v','w','x','y','z']

passowrd = input('Saisir la clé de chiffrement : \n')
passowrd = list(passowrd.lower())

while True:
    """ Boucle qui verifie si la valeur de decalage est valide
    """
    try:
        nombre_decalage = int(input('Entrez le nombre de decalage : \n'))
    except ValueError:
        print('Veillez un chiffre \n', '❌'*35)
    else:
        print(f'Validé ✔️ \n')     
        break
print('✅ '*25)



def chiffrement(liste: list , nombre_decalage: int = 0):
    """chiffrement
    Args:
        liste (list): _on recupere une liste pour pouvoir y iterer_
        nombre_decalage (int, optional): on recupere une valeur de type int a l'aide duquel nous allons faire le decalage des mots. Defaults to 0.
        La valeur par defaut ne sert a rien vu qu'on a une boucle au debut qui verifie obligatoirement le nombre . Mais pour le teste je le mets
    """
    word_retourner = []
    
    for i in range(len(liste)):
    
        for j in range(len(WORDLIST)):
            if liste[i] == WORDLIST[j]: 
                word_retourner.append(WORDLIST[j+nombre_decalage])
                
                        
    word_retourner_in_string = " ".join(word_retourner)        
    print(f'Votre clée chiffrer : {word_retourner_in_string}')

chiffrement(passowrd,nombre_decalage) 
#Si password contient un Z on aura une erreur 