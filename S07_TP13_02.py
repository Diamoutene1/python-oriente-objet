#S07_TP13_02
import tkinter as tk

class AppBase(tk.Tk):
    
    
    def __init__(self,title,width,height,pos_x,pos_y):
        tk.Tk.__init__(self)
        
        self.title(title)

        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        
        self.__f_main = tk.Frame(self)
        self.__f_main.pack()
        
        self.__c_draw = tk.Canvas(self.__f_main,bg = "white")
        self.__c_draw.pack()
        
        self.__b_quit = tk.Button(self,text = "Quitter", command = self.quit)
        self.__b_quit.pack(side = tk.RIGHT)
        

        
        
if __name__=="__main__":
    TITLE = "Test tkinter"
    WIDTH=800
    HEIGHT=500
    POS_X=100
    POS_Y=50

    app = AppBase(TITLE,WIDTH,HEIGHT,POS_X,POS_Y)
    app.mainloop()