import random
import tkinter as tk
from S05_TP09_1_Grid import Grid
from S07_TP14_1_element import Human


class GridCanvas(Grid, tk.Canvas):

    def __init__(self, master, lines_count, columns_count, cell_size, gutter_size, margin_size, background='yellow', cell_fill='orange', cell_foreground='white', **kw):
        Grid.__init__(self, [[Human()] * columns_count for _ in range(lines_count)])
        kw['width'] = cell_size * columns_count + 2 * margin_size + (columns_count - 1) * gutter_size
        kw['height'] = cell_size * lines_count + 2 * margin_size + (lines_count - 1) * gutter_size
        kw['bg'] = background
        tk.Canvas.__init__(self, master, **kw)
        for cell_number in range(self.get_lines_count() * self.get_columns_count()):
            i, j = self.get_coordinates_from_cell_number(cell_number)
            x = j * (cell_size + gutter_size) + margin_size
            y = i * (cell_size + gutter_size) + margin_size
            self.create_rectangle(x, y, x + cell_size, y + cell_size, fill=background, tags=(f'c_{i}_{j}', f'c_{cell_number}'))
            self.create_text(x + cell_size // 2, y + cell_size // 2, text=str(self.get_cell(cell_number)), fill=background, font=('Arial', cell_size // 5, 'bold'), tags=(f't_{i}_{j}', f't_{cell_number}'))
        self.__master = master
        self.__cell_size = cell_size
        self.__gutter_size = gutter_size
        self.__margin_size = margin_size
        self.__background = background
        self.__cell_fill = cell_fill
        self.__cell_foreground = cell_foreground

    def get_master(self):
        return self.__master

    def set_cell_colors(self, cell_number, filled=True):
        if filled:
            self.itemconfigure(f'c_{cell_number}', fill=self.__cell_fill)
            self.itemconfigure(f't_{cell_number}', fill=self.__cell_foreground)
        else:
            self.itemconfigure(f'c_{cell_number}', fill=self.__background)
            self.itemconfigure(f't_{cell_number}', fill=self.__background)

    def get_cell_colors(self, cell_number):
        return self.itemcget(f'c_{cell_number}', 'fill'), self.itemcget(f't_{cell_number}', 'fill')


class MyApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.__c_grid = GridCanvas(self, 10, 20, 50, 3, 50)
        self.__c_grid.pack()
        self.__c_grid.bind("<Button-1>", self.b1_handler)
        self.bind("<space>", self.space_handler)
        tk.Button(self, text='Quitter', command=self.quit).pack()

    def get_grid(self):
        return self.__c_grid

    def b1_handler(self, event):
        print(event.widget, event.x, event.y)
        cell_number = random.randrange(self.__c_grid.get_columns_count() * self.__c_grid.get_lines_count())
        self.__c_grid.set_cell_colors(cell_number)

    def space_handler(self, event):
        print(event.widget)
        cell_number = random.randrange(self.__c_grid.get_columns_count() * self.__c_grid.get_lines_count())
        self.__c_grid.set_cell_colors(cell_number)


if __name__ == '__main__':
    MyApp().mainloop()
