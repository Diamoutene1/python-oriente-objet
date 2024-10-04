import tkinter as tk
from S07_TP14_1_element import TurmiteAlea
from S08_TP16_1_Conway import Conway
from S08_TP16_2_turmites import Turmites
from S08_TP16_3_snake import SnakeGame


class MyApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        Conway(self, 30, 30, cell_size=20, population_density=0.2, show_gridlines=False).pack(side=tk.LEFT)
        Turmites(self, 120, 120, turmite_type=TurmiteAlea, turmites_count=5, cell_size=5).pack(side=tk.LEFT)
        SnakeGame(self, 30, 30, cell_size=20).pack(side=tk.LEFT)
        self.title("Some Planets")
        tk.Button(self, text='Quit', command=self.quit).pack(side=tk.RIGHT)


if __name__ == '__main__':
    MyApp().mainloop()
