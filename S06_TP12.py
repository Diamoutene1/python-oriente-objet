from S01_TP04_template import get_all_letters
import random

class Human:

    def __init__(self, first_names, last_name, alpha_code2, greetings, majority=18):
        self.__full_name = " ".join(first_names) + " " + "".join(last_name)
        self.__nationality = alpha_code2.upper()
        self.__greetings = greetings
        self.__age = 0
        self.__majority = majority

    def get_name(self):
        return self.__full_name

    def is_adult(self):
        return self.__age >= self.__majority

    def ageing(self, years=1):
        self.__age += years

    def get_info(self):
        status = "majeur" if self.is_adult() else "mineur"
        return f"Identité : {self.__full_name} - Nationalité : {self.__nationality} - Age : {self.__age} ans ({status})"

    def get_shout(self):
        if self.__age < 1:
            return "Ouin ouin"
        elif 1 <= self.__age < 2:
            return "Areuh baba gaga"
        elif 2 <= self.__age < 3:
            return "Bonrujo"
        else:
            return self.__greetings

class Animal:

    def __init__(self, nickname, owner):
        self.__nickname = nickname
        self.__owner = owner


    def get_nickname(self):
        return self.__nickname

    def set_nickname(self,nickname):
        self.__nickname=nickname

    def get_owner(self):
        return self.__owner

    def take_owner(self, owner):
        self.__owner = owner



class Cow(Animal):

    def __init__(self, nickname, weight, owner):
        Animal.__init__(self,nickname,owner)
        self.__weight = weight
          
    def get_info(self):
        owner_name = Animal.get_owner(self).get_name() if Animal.get_owner(self) else "Pas d'owner"
        return f"{Animal.get_nickname(self)} : cow de {self.__weight} Kg. Appartient à {owner_name}."

    def gain_weight(self, weight=1):
        self.__weight += weight

    def lose_weight(self, weight=1):
        self.__weight -= weight

    @classmethod
    def get_shout(self):
        return f"{Animal.get_nickname(self)} appartient à {Animal.get_owner(self).get_name()}. C'est une de {self.__weight} Kg"


class Dog(Animal):

    def __init__(self, nickname, owner=None, state=0):
        Animal.__init__(self,nickname,owner)
        self.__state = state


    def get_info(self):
        owner_name ="Appartient à "+Animal.get_owner(self).get_name()+"." if Animal.get_owner(self) else "N'a pas de propriétaire."
        state_info = "cool" if self.__state == 0 else "en colère"

        return f"{Animal.get_nickname(self)} : dog {state_info}. {owner_name}"
     
    def swap_state(self):
        self.__state = 1 if self.__state == 0 else 0


    def get_shout(self):
        owner_name ="Appartient à "+Animal.get_owner(self).get_name()+"." if Animal.get_owner(self) else "n'a pas de propriétaire"
        state_info = "cool" if self.__state == 0 else "en colère"
        return f"{Animal.get_nickname(self)} {owner_name}, c'est un chien {state_info}"


class Farm:
     
    __inhabitants=[]
    def __init__(self,Name,owner:Human):
        self.__name=Name
        self.__owner=owner

    
    def get_name(self):
        return self.__name
    
    def get_inhabitant(self):
        return self.__inhabitants
        #set {cow|Dog|Humain}
    def populate(self,inhabitant:Human|Dog|Cow):
        self.__inhabitants.append(inhabitant)

    def get_talk(self):
        for inhabitant in self.__inhabitants:
            return f"-{inhabitant.get_name()} : {inhabitant.get_shout()} \n"
    
class French(Human):
    __Nationalite="Française"
    def __init__(self,first_name,last_name):

        self.__full_name = " ".join(first_name) + " " + "".join(last_name)
    def get_shout(self):
        return f"Je m'appelle {self.__full_name} et j'ai la natrionalité {self.__Nationalite}, Bonjour !"

class English(Human):
   
    __Nationalite="Anglaise"
    def __init__(self,first_name,last_name):
        self.__full_name = " ".join(first_name) + " " + "".join(last_name)
    def get_shout(self):
        return f"Je m'appelle {self.__full_name} et j'ai la natrionalité {self.__Nationalite}, Hello !"

class Portuges(Human):

    __Nationalite="Portuguèse"
    def __init__(self,first_name,last_name):
        self.__full_name = " ".join(first_name) + " " + "".join(last_name)
    def get_shout(self):
        return f"Je m'appelle {self.__full_name} et j'ai la natrionalité {self.__Nationalite}, Bonjour !"
    

    





            




































if __name__ == "__main__":
    random.seed(100)
    farmer = Human(["Marcel", "Robert"], "Duchamps", "fr", "Bonjour", 18)
    farmer.ageing(35)
    assert farmer.get_info() == 'Identité : Marcel Robert Duchamps - Nationalité : FR - Age : 35 ans (majeur)'
    assert farmer.get_shout() == 'Bonjour'
    farmeress = Human(["Marcela"], "Zpola", "pl", "Dzień dobry", 18)
    farmeress.ageing(36)
    assert farmeress.get_info() == 'Identité : Marcela Zpola - Nationalité : PL - Age : 36 ans (majeur)'
    assert farmeress.get_shout() == 'Dzień dobry'
    boy = Human(["Marcel", "junior"], "Duchamps Zpola", "fr", "Bonjour")
    assert boy.get_info() == 'Identité : Marcel junior Duchamps Zpola - Nationalité : FR - Age : 0 ans (mineur)'
    assert boy.get_shout() == 'Ouin ouin'
    boy.ageing()
    assert boy.get_info() == 'Identité : Marcel junior Duchamps Zpola - Nationalité : FR - Age : 1 ans (mineur)'
    assert boy.get_shout() == 'Areuh baba gaga'
    boy.ageing()
    assert boy.get_info() == 'Identité : Marcel junior Duchamps Zpola - Nationalité : FR - Age : 2 ans (mineur)'
    assert boy.get_shout() == 'Bonrujo'
    boy.ageing()
    assert boy.get_info() == 'Identité : Marcel junior Duchamps Zpola - Nationalité : FR - Age : 3 ans (mineur)'
    assert boy.get_shout() == 'Bonjour'
    milk_cow = Cow("Aglaë", 300, farmer)
    milk_cow.gain_weight(30)
    milk_cow.lose_weight(20)
    #print(milk_cow.get_info())
    assert milk_cow.get_info() == 'Aglaë : cow de 310 Kg. Appartient à Marcel Robert Duchamps.'
    milk_cow.take_owner(farmeress)
    assert milk_cow.get_info() == 'Aglaë : cow de 310 Kg. Appartient à Marcela Zpola.'
    #assert milk_cow.get_shout() == 'Meuh'
    stray_dog = Dog("Médor", state=0)
    #print(stray_dog.get_info())
    assert stray_dog.get_info() == "Médor : dog cool. N'a pas de propriétaire."
    #print(stray_dog.get_shout())
    #assert stray_dog.get_shout() == 'Ouah ouah'
    stray_dog.take_owner(boy)
    stray_dog.swap_state()
    #print(stray_dog.get_info())
    assert stray_dog.get_info() == "Médor : dog en colère. Appartient à Marcel junior Duchamps Zpola."
    print(stray_dog.get_shout())
    assert stray_dog.get_shout() == 'Grrr'
    farm=Farm("Farmacel",farmer)
    farm.populate(farmer)
    farm.populate(farmeress)
    farm.populate(boy)
    farm.populate(milk_cow)
    farm.populate(stray_dog)
    #print(farm.get_talk())

    couple=(French(["Amélie"],"le mouton"),French(["JOAO"],"Félix"))

    #print(couple[0].get_shout())
    print("Tests all OK")