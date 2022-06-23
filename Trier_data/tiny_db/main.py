# - Créer une classe Joueur
# - on aura 3 attributs (pseudo, health(points de vie), damage(dégats par tir))
# - Créer une méthode getDamage qui enlève des points de vie selon
# les dégats infligés par un autre joueur.
# - Créer une méthode shoot qui permet
# d'infliger des dégats à un autre joueur

from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Joueur:
    pseudo : str
    damage : int = 5
    health : int = 100
    
    
    def getDamage(self, degat_receive, pseudo_adversaire):
        self.health -= degat_receive
        
        print(f"{pseudo_adversaire} vous a infligé {degat_receive} de dommage")
    
    def shoot(self, adversaire):
        adversaire.getDamage(self.damage, self.pseudo) 
        


nouha = Joueur('nouha', 10)
zlorg = Joueur('zlorg', 15)


zlorg.shoot(nouha)

nouha.shoot(zlorg)
# print(zlorg.health)



                
    
    