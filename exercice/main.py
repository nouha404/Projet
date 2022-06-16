from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Voiture:
    marque : str
    vitesse : int
    prix : str
    
    #STR s'execute directement apres les attribut d'instances
    def __str__(self):
        return f"Voiture de marque {self.marque} avec une vitesse de {self.vitesse}"
    
    @classmethod
    def lamborghini(cls):
        return cls(marque='Lamborghini', vitesse=400, prix='5M')
    
    def __post_init__(self):
        return f"Voiture de marque {self.marque} avec une vitesse de {self.vitesse}"
    
    @classmethod
    def porsh(cls):
        return cls(marque='Porsh', vitesse=390, prix='4.5M')
    
    


lambo = Voiture.lamborghini()
porsh = Voiture.porsh()

test = Voiture('car rapide', 450, '150k')
print(lambo.marque)


# print(lambo.prix)
