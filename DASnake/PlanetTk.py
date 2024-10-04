import tkinter as tk
from Grid import Grid
from PlanetAlpha import PlanetAlpha
from Element import *
import random

class PlanetTK(PlanetAlpha,tk.Canvas):

    def __init__(self,root,name,latitude_cells_count,longitude_cells_count,authorised_class,background_color="white",foreground_color="darkblue",gridlines_color="maroon",cell_size=40,gutter_size=0,margin_size=0,show_content=True,show_gridlines=True,**kw):
        PlanetAlpha.__init__(self,name,latitude_cells_count,longitude_cells_count,Ground())
        self.__root=root
        self.__background_color=background_color
        self.__foreground_color=foreground_color
        self.__cell_size=cell_size
        self.__gutter_size=gutter_size
        self.__margin_size=margin_size
        self.__show_content=show_content
        self.__show_gridlines=show_gridlines
        self.__authorised_class=authorised_class
        self.__gridlines_color=gridlines_color
        self.game_running=False
        kw['width'] = self.__cell_size * longitude_cells_count + 2 * self.__margin_size + (longitude_cells_count - 1) * self.__gutter_size
        kw['height'] = self.__cell_size * latitude_cells_count + 2 * self.__margin_size + (latitude_cells_count - 1) * self.__gutter_size
        tk.Canvas.__init__(self, root, **kw)
        for cell_number in range(self.get_lines_count() * self.get_columns_count()):
            i, j = self.get_coordinates_from_cell_number(cell_number)
            x = j * (self.__cell_size + self.__gutter_size) + self.__margin_size
            y = i * (self.__cell_size + self.__gutter_size) + self.__margin_size
            self.create_rectangle(x, y, x + self.__cell_size, y + self.__cell_size, tags=(f'c_{i}_{j}', f'c_{cell_number}'),fill="white")
            self.create_text(x + self.__cell_size // 2, y + self.__cell_size // 2, fill="white", font=('Arial', self.__cell_size // 5, 'bold'), tags=(f't_{i}_{j}', f't_{cell_number}'))

        """self.tag_bind(f't_{cell_number}', "<Button-1>", lambda event, c=cell_number: self.b1_handler(event, c))
        root.bind("<Button-1>", self.b1_handler)
        self.tag_bind(f't_{cell_number}', "<Button-1>", lambda event, c=cell_number: self.b1_handler(event, c))
        root.bind("<space>", self.space_handler)"""

    def set_cell_colors(self, cell_number, color,filled=True):
        if filled:
            self.itemconfigure(f'c_{cell_number}', fill=color)
            self.itemconfigure(f't_{cell_number}', fill=color)
        else:
            self.itemconfigure(f'c_{cell_number}', fill=self.__background_color)
            self.itemconfigure(f't_{cell_number}', fill=self.__background_color)
    

    def b1_handler(self, event):
        print(event.widget, event.x, event.y)
        i = (event.y - self.__margin_size) // (self.__cell_size + self.__gutter_size)
        j = (event.x - self.__margin_size) // (self.__cell_size + self.__gutter_size)
        cell_number = self.get_cell_number_from_coordinates(i, j)
        self.set_cell_colors(cell_number)

    def space_handler(self, event):
        print(event.widget)
        cell_number = random.randrange(self.get_columns_count() * self.get_lines_count())
        self.set_cell_colors(cell_number)

    def get_root(self):
        return self.__root

    def get_background_color(self):
        return self.__background_color
    
    def get_foreground_color(self):
        return self.__foreground_color

    def born(self,cell_number,element):

        if element.__class___ in self.__authorised_class :
            self.born(cell_number,element)
    def born_randomly(self,element):

        cell_number=self.get_random_free_place()
        if element.__class___ in self.__authorised_class:
            self.born(cell_number,element)

    def die(self,cell_number,element):
        self.die(cell_number,element)


    def populate(self,class_names_count):

        for element , element_count in class_names_count.items() :
            for _ in range ( element_count):
                self.born(self.get_random_free_place(),element)


    def move_element(self,cell_number,new_cell_number):

        elem=self.get_cell(cell_number)
        self.die(cell_number,elem)
        self.born(new_cell_number,elem)



    def get_class_cell_number(self) :
        class_cell_numbers = {}

        for lat in range(self.get_latitude_cells_count()):
            for lon in range(self.get_longitude_cells_count()):
                cell_number = self.get_cell_number(lat, lon)
                cell_content = self.get_cell(cell_number)

                if cell_content.__class__ in class_cell_numbers:
                    class_cell_numbers[cell_content.__class__].append(cell_number)
                else:
                    class_cell_numbers[cell_content.__class__] = [cell_number]

        return class_cell_numbers



        

    


if __name__ == "__main__":

    root=tk.Tk()
    root.title("PlanetTk")
    PLANET_TEST=PlanetTK(root,"Terre",60,60,{"D","C","E","H"},"white","darkblue","black",20,0,0,True,True)

    PLANET_TEST.pack()

    root.mainloop()
    print(PLANET_TEST.__class__)