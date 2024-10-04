import tkinter as tk
import random

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [["white" for _ in range(width // 5)] for _ in range(height // 5)]

    def get_color(self, x, y):
        return self.grid[y // 5][x // 5]

    def set_color(self, x, y, color):
        self.grid[y // 5][x // 5] = color

class Element:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + 5, self.y + 5, fill=self.color, outline="")

class Turmite(Element):
    def __init__(self, x, y, color, grid):
        super().__init__(x, y, color)
        self.direction = random.choice(["N", "E", "S", "W"])
        self.grid = grid

    def move(self):
        current_color = self.grid.get_color(self.x, self.y)
        if current_color == "white":
            self.turn_right()
            self.grid.set_color(self.x, self.y, "black")
        else:
            self.turn_left()
            self.grid.set_color(self.x, self.y, "white")
        self.update_position()

    def turn_right(self):
        directions = ["N", "E", "S", "W"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def turn_left(self):
        directions = ["N", "E", "S", "W"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index - 1) % 4]

    def update_position(self):
        if self.direction == "N":
            self.y -= 5
        elif self.direction == "E":
            self.x += 5
        elif self.direction == "S":
            self.y += 5
        elif self.direction == "W":
            self.x -= 5

class PlanetAlpha:
    def __init__(self):
        self.turmites = []

    def add_turmite(self, x, y, color):
        turmite = Turmite(x, y, color, self.grid)
        self.turmites.append(turmite)

    def draw_turmites(self):
        self.canvas.delete("all")
        for turmite in self.turmites:
            turmite.draw(self.canvas)

    def move_turmites(self):
        for turmite in self.turmites:
            turmite.move()
        self.draw_turmites()
        self.update()

class PlanetTk(PlanetAlpha, tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.grid = Grid(width, height)
        self.canvas = tk.Canvas(self, width=width, height=height, bg="white")
        self.canvas.pack()

def main():
    window = PlanetTk(500, 500)
    window.add_turmite(250, 250, "black")  # You can add more turmites with different colors and positions

    for _ in range(1000):  # Number of steps
        window.move_turmites()

    window.mainloop()

if __name__ == "__main__":
    main()
