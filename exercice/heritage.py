from dataclasses import dataclass
from typing import ClassVar

projets = ['pr_GameOfThrone', 'harryPoter', 'pr_Avengers', 'One piece']

@dataclass
class Users:
    nom : str
    prenom : str
  
    def __str__(self):
        return f'{self.nom} {self.prenom}'
    
    def afficher_projet(self):
        for i in projets:
            print(i)
@dataclass
class Junior(Users):
    nom : str
    prenom : str
    #surcharge
    def afficher_projet(self):
        for i in projets:
            if not i.startswith('pr_'):
                print(i)
    # def test(self):
    #     #Afficher une methode de la classe parent
    #     super().afficher_projet()
    
dms = Users('dms', 'Marega')   
dms.afficher_projet()
#Parti eritage
junior = Junior('nouha', 'Marega')
junior.afficher_projet()


