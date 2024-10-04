import random

class Element:
    
    def __init__(self, char_repr):
        self.__char_repr = char_repr
        
    def __repr__(self):
        return self.__char_repr

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__char_repr == other.__char_repr

class Ground(Element):

    def __init__(self):
        Element.__init__(self, "\u2B1C")

class Resource(Element):

    def __init__(self, char_repr, value=0):
        Element.__init__(self, char_repr)
        self.__value = value

    def get_value(self):
        return self.__value

class Animal(Element):

    def __init__(self, char_repr, life_max):
        Element.__init__(self, char_repr)
        self.__age = 0
        self.__gender = random.randint(0, 1)
        self.__bar_life = [life_max, life_max]
        self.__current_direction = random.randrange(-1, 2)

    def get_age(self):
        return self.__age

    def ageing(self):
        self.__age += 1

    def get_gender(self):
        return self.__gender
    
    def get_life_max(self):
        return self.__bar_life[1]

    def get_life(self):
        return self.__bar_life[0]
    
    def is_alive(self):
        return self.__bar_life[0] != 0

    def is_dead(self):
        return self.__bar_life[0] == 0

    def recovering_life(self, value):
        pass

    def losing_life(self, value):
        pass

    def get_current_direction(self):
        pass

    def set_current_direction(self, line_direction, column_direction):
        self.__current_direction = [line_direction, column_direction]

class Water(Resource):

    def __init__(self):
        Resource.__init__(self, "\U0001F41F", 1)

class Herb(Resource):

    def __init__(self):
        Resource.__init__(self, "\U0001F33F", 2)

class Cow(Animal):

    def __init__(self):
        Animal.__init__(self, "\U0001F42E", 10)

class Dragon(Animal):

    def __init__(self):
        Animal.__init__(self, "\U0001F432", 50)

class Lion(Animal):

    def __init__(self):
        Animal.__init__(self, "\U0001F981", 20)

class Mouse(Animal):

    def __init__(self):
        Animal.__init__(self, "\U0001F42D", 5)

if __name__ == '__main__':
    print(Ground(), str(Ground()))
    print(Ground() == str(Ground()))
    print(Ground() == Ground())
    print(Ground() is Ground())

    TYPES_COUNT = {Herb: 2, Water: 3, Cow: 2, Dragon: 1, Lion: 5, Mouse: 10}

    ELEMENTS_BY_TYPE = {element_type: [element_type() for _ in range(element_count)]
                        for element_type, element_count in TYPES_COUNT.items()}

    for element_type, elements in ELEMENTS_BY_TYPE.items():
        print(element_type.__name__, elements)
