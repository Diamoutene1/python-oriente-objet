from Grid import Grid
import random

class PlanetAlpha(Grid):

    NORTH,EST,SOUTH,WEST,NORTH_EAST,SOUTH_EAST,SOUTH_WEST,NORTH_WEST=(-1,0),(0,1),(0,-1),(1,0),(-1,1),(1,1),(1,-1),(-1,-1)
    CARDINAL_POINTS=[NORTH,EST,SOUTH,WEST]
    WIND_ROSE=[NORTH,EST,SOUTH,WEST,NORTH_EAST,SOUTH_EAST,SOUTH_WEST,NORTH_WEST]


    __population=0
    def __init__(self,name,latitude_cells_count,longitude_cells_count,ground):
        Grid.__init__(self,grid_init=[[ground for _ in range(longitude_cells_count)] for _ in range(latitude_cells_count)])
        self.__name=name
        self.__latitude_cells_count=latitude_cells_count
        self.__longitude_cells_count=longitude_cells_count
        self.__ground=ground
        self.__population=0

    def get_name(self):
        return self.__name

    
    def get_ground(self):
        return self.__ground
    


    def get_place(self):
        liste=[]
        for cell_number in range(self.__latitude_cells_count*self.__longitude_cells_count):
                
                if self.get_cell(cell_number)==self.get_ground():
                    liste.append(cell_number)

        return liste

    def get_random_free_place(self):
        if len(self.get_place())==0:
            return 0
        return random.choice(self.get_place())



    def born(self,cell_number,elem):
        if cell_number not in self.get_place():
            return 0
        self.set_cell(cell_number,elem)
        self.__population+=1
        return 1
    
    def die(self,cell_number):

        self.set_cell(cell_number,self.__ground)
        self.__population-=1
        return 1
        

    def __repr__(self):
        result = f"{self.__name} ({self.__population} habitants)\n"+"\n"
        
        return result +self.get_grid_str(separator=" ")
        
    





if __name__ == "__main__":
         
    PLANET_TEST=PlanetAlpha("Terre" , 5 , 10 , "." )

    #print(PLANET_TEST)
    INHABITANTS_TEST = { "D" : 7 , "C" : 3}
    RESOURCES_TEST = {"E" : 10 ,"H" : 20}

    for letter , letter_count in INHABITANTS_TEST.items() :
        for _ in range ( letter_count):
            PLANET_TEST.born (PLANET_TEST.get_random_free_place(),letter)

    for letter , letter_count in RESOURCES_TEST.items() :
        for _ in range ( letter_count):
            PLANET_TEST.born (PLANET_TEST.get_random_free_place(),letter)


    #print (PLANET_TEST)
    #print (PLANET_TEST.get_neighbour ( 0 , 0 , PlanetAlpha .NORTH_WEST) )
    #print(PLANET_TEST.get_neighborhood ( 0 , 0 , PlanetAlpha .CARDINAL_POINTS) )
    #PLANET_TEST. die( 5 )
    #print (PLANET_TEST)