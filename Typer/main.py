import typer
from pathlib import Path

ROOT = Path(__file__).resolve().parent / 'data'


def main(extension : str = typer.Argument('...', help="Recherche de l'extension par defaut txt"), delete : bool = typer.Option(False, help='Suppression des fichiers')):
    
    array = list(ROOT.rglob(f'*.{extension}'))
    if array:
        for i in ROOT.rglob(f'*.{extension}'):
            typer.secho(i.name, fg = typer.colors.BRIGHT_GREEN)
            
            if delete:
                typer.confirm('Voulez vous vraiment supprimer les fichiers ? ')
                i.unlink()
                typer.secho('Suppression reussi ! ', bg= typer.colors.BRIGHT_WHITE, fg=typer.colors.BRIGHT_RED)
    else:           
        typer.secho(f" L'extension {extension} est introuvable .", bg= typer.colors.BRIGHT_RED )
    

typer.run(main)