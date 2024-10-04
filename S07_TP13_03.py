#S07_TP13_03
import tkinter as tk
class MyApp(tk.Tk):
    __COLORS = {'cell_baclgroud' : "white","celle_foreground":"res","grid_lines":"black","grid_text":"dark blue","widget_text":"orange"}
    
    def __init__(self,grid,cell_size,gutter_size,margin_size):
        tk.Tk.__init__(self)
        self.__grid = grid
        self.__cell_size = cell_size
        self.__gutter_size = gutter_size
        self.__margin_size = margin_size
        
        self.__f_main = tk.Frame(self)
        self.__f_main.pack()
        l, c=grid.get_Lines_count(),grid.get_colums_count()
        widh= c*cell_size + (c-1)*gutter_size+2*margin_size
        height= l*cell_size + (l-1)*gutter_size+2*margin_size
        self.__c_draw = tk.Canvas(self.__f_main,bg = "white")
        self.__c_draw.pack()
        
        self.__b_quit = tk.Button(self,text = "Quitter", command = self.quit)
        self.__b_quit.pack(side = tk.RIGHT)
        self.__b_quit.pack()


if __name__=="__main__":
    from S05_TP09_01_template import Grid
    LINES_COUNT= 20
    COLUMS_COUNT=30
    GRID_TEST = Grid([[0]*COLUMS_COUNT for _ in range(LINES_COUNT)])
    GRID_TEST.fill_random(range(1000))
    CELL_SIZE=50
    GUTEER_SIZE=5
    MARGIN_SIZE=19
    app = MyApp(GRID_TEST,CELL_SIZE,GUTEER_SIZE,MARGIN_SIZE)
    app.mainloop()

    