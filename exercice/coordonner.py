import math

class Point:
    def __init__(self,x = 0.0,y = 0.0):
        self.x = x
        self.y = y
    #Écrivez le code ici

    def _getx(self):
        
        return self.x
        #Écrivez le code ici

    def _gety(self):
        
        return self.y
        #Écrivez le code ici
        
    def distance_from_xy(self, x, y):
        
        return math.hypot(self.x, self.y)
        #Écrivez le code ici

    def distance_from_point(self, point):
        # Bruh
        point = Point.distance_from_xy(self, self.x, self.y )
        return point       
        #Écrivez le code ici

point1 = Point(0, 0)
point2 = Point(1, 1)

print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))