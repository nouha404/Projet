# Exercice 3:
# Écrivez une fonction unique_characters() qui détermine
# si une chaîne donnée contient tous les caractères uniques
# (c'est-à-dire qu'aucun caractère de la chaîne n'est dupliqué). 
# Si la chaîne contient tous des caractères uniques, 
# la fonction doit renvoyer True. Si la chaîne ne contient pas tous les caractères uniques,
# renvoyez False.

# Par exemple, unique_characters("apple") doit renvoyer False.

import typer

def unique_characters(chaine : str = typer.Argument('apple', help='Chaine rechercher par defaut')):
    
    for i in list(chaine):
        if chaine.count(i) > 1:
            return typer.secho(False, fg= typer.colors.BRIGHT_RED)
    return typer.secho(True, fg= typer.colors.BRIGHT_GREEN)

typer.run(unique_characters)
