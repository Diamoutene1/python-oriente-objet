import tkinter as tk
from S07_TP14_1_element import TurmiteAlea
from S08_TP16_1_Conway import Conway
from S08_TP16_2_turmites import Turmites
from S08_TP16_3_snake import SnakeGame


class SnakeGameWindow(tk.Toplevel):

    def __init__(self, master, **kw):
        tk.Toplevel.__init__(self, master, **kw)
        self.__master = master
        self.__game = SnakeGame(self, 30, 50, cell_size=30)
        self.__game.pack()
        tk.Button(self, text="Quit", command=self.destroy).pack()


class TurmitesWindow(tk.Toplevel):

    def __init__(self, master, **kw):
        tk.Toplevel.__init__(self, master, **kw)
        self.__master = master
        self.__game = Turmites(self, 120, 200, turmite_type=TurmiteAlea, turmites_count=8, cell_size=5)
        self.__game.pack()
        tk.Button(self, text="Quit", command=self.destroy).pack()


class ConwayWindow(tk.Toplevel):

    def __init__(self, master, **kw):
        tk.Toplevel.__init__(self, master, **kw)
        self.__master = master
        self.__game = Conway(self, 40, 60, cell_size=25, population_density=0.2, show_gridlines=False)
        self.__game.pack()
        tk.Button(self, text="Quit", command=self.destroy).pack()


class MyApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Some Planets")
        tk.Button(self, text='Conway game', command=lambda: ConwayWindow(self)).pack(side=tk.LEFT)
        tk.Button(self, text='Turmites game', command=lambda: TurmitesWindow(self)).pack(side=tk.LEFT)
        tk.Button(self, text='Snake game', command=lambda: SnakeGameWindow(self)).pack(side=tk.LEFT)
        tk.Button(self, text='Quit', command=self.quit).pack(side=tk.RIGHT)


if __name__ == '__main__':
    MyApp().mainloop()
