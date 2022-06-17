BIbliotheque qui permet de faire des choses sympa sur le terminal notament ajouter des couleurs, les arguments , creer des commande etc
On import dabord typer
    import typer

on creer notre fonction
    def main():
    """
        Les docstring permet de documents notre fonction quand on va mettre la commande
        nomdu_programe.py --help

    """
Pour afficher ce qu'on veut afficher (comme la commande print ) on utilise typer.echo
    typer.echo("quelque chose")

Une fois la fonction creer pour l'appeler on utilise run
    typer.run(nom_de_la_fonction)

--------------------------------------------------------------------------
 def main(extension : str):
 
    typer.echo(f"quelque chose de type {}")

l'argument extension en parametre devient obligatoire quand on appel 
la fonction sinon on aura une erreur
-------------------------------------------------------------
 def main(extension : str = 'txt'):

 Si on mets une valeur par defaut , ca devient une option
 -----------------------------------------------------------------------
def presentation(extension):
    """Fonction qui afficher quelque chose
    """
    typer.echo(f"Hello word I'm pythonista de type {extension}")

# Si je tape la commande : 
#   python biblio2.py txt 
# A la place de {extension} on aura txt
# Sinon je fais :
#   python biblio2.py
# On aura une erreur 


typer.run(presentation)
--------------------------------------------------------------------------------------------
def presentation(extension : str = 'txt'):
    """Fonction qui afficher quelque chose
    """
    typer.echo(f"Hello word I'm pythonista de type {extension}")


#Pour utiliser l'option on fait
#   python biblio.py --extension py 
# On aura
# f"Hello word I'm pythonista de type {extension}"

typer.run(presentation)
----------------------------------------------------------------------------------------------
Pour creer un argument avec une valeur par defaut 

def presentation(extension : str = typer.Argument(..., help="extension txt par defaut")):
    """Fonction qui afficher quelque chose
    """
    typer.echo(f"Hello word I'm pythonista de type {extension}")


# les ... signifie que l'argument sera requis
#Pour avec le text d'aide on mets le help
# help = "text"
# A la place des 3 points on mets "txt" et ca sera l'argument a chercher  par defaut ce qui sera chercher 
# Pour que l'argument se sois plus requis on mets None a la place du txt

# En gros une option a une valeur par defaut : def main(delete : bool = True)
# Un argument n'a pas de valeur par defaut : def main(delete : bool)
# On peut utiliser un argument avec une valeur par defaut grace a typer.Argument()

typer.run(presentation)
-----------------------------------------------------------------------------------------------

def presentation(delete : bool = typer.Option(..., help="suprime une extention") ,extension : str = typer.Argument(..., help="extension txt par defaut")):
    """Fonction qui afficher quelque chose
    """
    typer.echo(f"Hello word I'm pythonista de type {extension}")

# Pour ajouter une messager d'aide on mets typer.Option
#   Le typer.Option(..., help='txt')
# A la place des 3 points on peut mettre False comme valeuur par defaut

typer.run(presentation)
------------------------------------------------------------------------------------------
# Demander des infos ainsi qu'une confirmation
# Demander une info est l'équivalent de input
    extension = typer.prompt("Ce qu'on demande ")
# Privlegier confirm a la place de prompt
                typer.confirm("text a chercher : ")
# Pour annuler le demande on fait :
    raise type.Abort()

----------------------------------------------------------------------------------------------
# Pour aborder directement le truc on mets le abort=True a l'interieur du confirm 

def main(delete : bool = typer.Option(False, help="suppression des fichier"), extension : str = typer.Argument('txt', help="extension par defaut") ):
    
    typer.echo(f"Supression de l'extension {extension}")
    if delete:
        typer.confirm("Voulez vous supprimer cette extension : ", abort=True)
        
    print(f"Supression de l'extension {extension}")

typer.run(main)
---------------------------------------------------------------------------------------------
# comment ajouter des commandes 
# On doit creer un instace de Typer()
# app = typer.Typer()

@app.command('delete')
def delete():
    main(delete=False, extension='py')
    
@app.command('search')
def search():
    main(delete=True , extension='py')

# a la fin on appel app()
--------------------------------------------------------------------------------------------------------------------------------------

# les couleurs 
# fg = font size
# bg = baground color
# On fait :
# secho et echo c'est pareille sauf que le premier permet de les mettre sur une seul ligne
# typer.secho('Bonjour patrick', fg = typer.style.color.RED)
Les styles :
fg = typer.style.color.BLUE
bold=True

def main(prenom : str = typer.Argument(..., help="Votre prenom")):
    
    TEST = typer.style(prenom, fg = typer.colors.RED )
    
    typer.echo(f'Bonjour {TEST}',)

typer.run(main) 

# Quand on le mets sur une seule ligne  on utilise secho et on enleve .style: secho = style echo
      typer.secho('bonjour', fg = typer.colors.RED)

------------------------------------------------------------------------------------------------------------------------------
# Barre de progression
def main():
    nombre = range(40)
    with typer.progressbar(nombre) as progress:
        for i in progress:
           
            time.sleep(0.04)

typer.run(main)
666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
