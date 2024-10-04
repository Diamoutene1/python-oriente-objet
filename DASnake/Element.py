import random
class Element:
    def __init__(self,char_repr):
        self.__char_repr=char_repr
    def __repr__(self):
        return self.__char_repr
    def __eq__(self, other):
        if issubclass(other.__class__, Element):
            return other.__char_repr==self.__char_repr
        return False
    def __hash__(self):
        return hash((type(self), id(self)))
class Snake(Element):

    def __init__(self,width,height,char_repr,taille,vitesse):
        Element.__init__(self,char_repr)
        self.__vitesse=vitesse
        self.__snake = [(width // 2 - i, height // 2) for i in range(taille)]
        
    def get_parts(self):
        return self.__snake
    
    def get_vitesse(self):
        return self.__vitesse
class Ground(Element):
    def __init__(self):
        Element.__init__(self,char_repr="\u2B1C")


class Turmite(Element):
    def __init__(self, x, y):
        # Initialise une Turmite avec sa position initiale (x, y)
        self.x = x
        self.y = y
        self.direction = (0, 1)  # Direction initiale vers le haut (vers le bas sur la grille)
        self.steps = 0  # Nombre de pas effectués par la turmite

    def move(self):
        # Déplace la turmite dans sa direction actuelle d'une case
        self.x += self.direction[0]
        self.y += self.direction[1]
        self.steps += 1  # Incrémente le nombre de pas

    def turn_left(self):
        # Fait tourner la turmite vers la gauche
        # Cela change la direction de la turmite de 90 degrés dans le sens anti-horaire
        self.direction = (-self.direction[1], self.direction[0])

    def turn_right(self):
        # Fait tourner la turmite vers la droite
        # Cela change la direction de la turmite de 90 degrés dans le sens horaire
        self.direction = (self.direction[1], -self.direction[0])
 
        


