# Créez une fonction prime_finder() qui prend un nombre, n,
# et renvoie tous les nombres premiers de 1 à n (inclus). 
# Pour rappel, un nombre premier est un nombre qui n'est divisible que par 1 et lui-même.

# Par exemple, prime_finder(11) devrait renvoyer [2, 3, 5, 7, 11].

import typer 

def prime_finder(n : int =  typer.Argument(5, help='nombre par defaut')):
    array = []
    
    for i in range(1,n+1):
        if i % 2 == 0:
            array.append(i)
                    
    typer.secho(f"{array} ", fg= typer.colors.BRIGHT_GREEN)

if __name__ == '__main__':
    typer.run(prime_finder) 
    