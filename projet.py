
 
import tkinter as tk
from tkinter import ttk
class Conway:
    def __init__(self, master, width, height):
        self.master = master
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(master, width=width*20, height=height*20)
        self.canvas.pack()
        self.next_button = ttk.Button(master, text="Suivant", command=self.next_step)
        self.next_button.pack(side=tk.LEFT)
        self.quit_button = ttk.Button(master, text="Quitter", command=master.quit)
        self.quit_button.pack(side=tk.RIGHT)
        self.grid = [[0] * height for _ in range(width)]
        self.draw_grid()
    def draw_grid(self):
        self.canvas.delete("all")
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] == 1:
                    self.canvas.create_rectangle(x*20, y*20, (x+1)*20, (y+1)*20, fill="black")
                else:
                    self.canvas.create_rectangle(x*20, y*20, (x+1)*20, (y+1)*20, fill="white")
    def next_step(self):
        new_grid = [[0] * self.height for _ in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                new_grid[x][y] = self.update_cell(x, y)
        self.grid = new_grid
        self.draw_grid()
    def update_cell(self, x, y):
        # Définir les règles d'évolution ici
        pass
def main():
    root = tk.Tk()
    root.title("Jeu de la Vie")
    game = Conway(root, 20, 20)
    root.mainloop()
if __name__ == "__main__":
    main()
