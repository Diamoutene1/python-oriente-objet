import tkinter as tk
import random

# Définition de la classe PlanetTK
class PlanetTK:
    # Définition des points cardinaux et de la rose des vents
    CARDINAL_POINTS = (0, 90, 180, 270)
    WIND_ROSE = (45, 135, 225, 315)
    
    # Initialisation de la classe PlanetTK
    def __init__(self):
        pass

# Définition de la classe Element
class Element:
    # Classe de base pour les éléments du jeu, contenant le nom et le type de terrain
    def __init__(self, name: str, ground: str):
        self.name = name
        self.ground = str

# Définition de la classe Snake, héritant de la classe Element
class Snake(Element):
    # Initialisation de la classe Snake
    def __init__(self, name: str, ground: str, size: int, speed: int, direction: str):
        super().__init__(name, ground)
        self.size = size
        self.speed = speed
        self.direction = direction
        self.body = [(10, 10), (9, 10), (8, 10)]

    # Méthode pour obtenir la prochaine position de la tête du serpent
    def get_next_position(self):
        x, y = self.body[0]
        if self.direction == "up":
            return (x, y - 1)
        elif self.direction == "down":
            return (x, y + 1)
        elif self.direction == "left":
            return (x - 1, y)
        elif self.direction == "right":
            return (x + 1, y)

    # Méthode pour faire avancer le serpent
    def advance(self):
        new_position = self.get_next_position()
        self.body.insert(0, new_position)
        self.body.pop()

    # Méthode pour tourner le serpent vers la gauche
    def turn_left(self):
        if self.direction == "up":
            self.direction = "left"
        elif self.direction == "down":
            self.direction = "right"
        elif self.direction == "left":
            self.direction = "down"
        elif self.direction == "right":
            self.direction = "up"

    # Méthode pour tourner le serpent vers la droite
    def turn_right(self):
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "down":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "up"
        elif self.direction == "right":
            self.direction = "down"

    # Méthode pour faire manger le serpent
    def mange(self):
        new_position = self.get_next_position()
        self.body.insert(0, new_position)

# Définition de la classe Food, héritant de la classe Element
class Food(Element):
    # Initialisation de la classe Food
    def __init__(self, name: str, ground: str, x: int, y: int):
        super().__init__(name, ground)
        self.x = x
        self.y = y

# Définition de la classe PlanetAlpha, héritant de la classe PlanetTK
class PlanetAlpha(PlanetTK):
    # Initialisation de la classe PlanetAlpha
    def __init__(self, name: str, latitude_cells_count: int, longitude_cells_count: int, ground: str):
        self.name = name
        self.ground = ground
        self.latitude_cells_count = latitude_cells_count
        self.longitude_cells_count = longitude_cells_count
        self.cells = [[None for _ in range(longitude_cells_count)] for _ in range(latitude_cells_count)]

    # Méthode pour obtenir une position libre aléatoire sur la planète
    def get_random_free_place(self):
        free_cells = [(x, y) for x in range(self.latitude_cells_count) for y in range(self.longitude_cells_count) if self.cells[x][y] is None]
        if free_cells:
            return random.choice(free_cells)
        else:
            return None

    # Méthode pour placer un élément à une position sur la planète
    def spawn(self, x: int, y: int, element: Element):
        self.cells[x][y] = element

    # Méthode pour supprimer un élément d'une position sur la planète
    def despawn(self, x: int, y: int):
        self.cells[x][y] = None

# Définition de la classe Button
class Button:
    # Initialisation de la classe Button
    def __init__(self, canvas, text, command, x, y):
        self.button = tk.Button(canvas, text=text, command=command)
        self.button.place(x=x, y=y)

    # Méthode pour détruire le bouton
    def destroy(self):
        self.button.destroy()

# Définition de la classe SnakeGame
class SnakeGame:
    # Initialisation de la classe SnakeGame
    def __init__(self, canvas: tk.Canvas, root: tk.Tk):
        self.score = 0
        self.canvas = canvas
        self.root = root
        self.planet_alpha = PlanetAlpha("Alpha", 20, 20, "grass")
        self.snake = Snake("Snake", "grass", 3, 300, "right")
        self.food = Food("Food", "grass", *self.planet_alpha.get_random_free_place())
        for x, y in self.snake.body:
            self.planet_alpha.spawn(x, y, self.snake)
        self.planet_alpha.spawn(self.food.x, self.food.y, self.food)
        # Bind des événements clavier pour contrôler le serpent
        root.bind('<Left>', lambda event: self.change_direction('left'))
        root.bind('<Right>', lambda event: self.change_direction('right'))
        root.bind('<Up>', lambda event: self.change_direction('up'))
        root.bind('<Down>', lambda event: self.change_direction('down'))

    # Méthode pour démarrer le jeu
    def start(self):
        self.update()
        self.root.mainloop()

    # Méthode pour mettre à jour l'état du jeu
    def update(self):
        self.draw()
        self.snake.advance()
        if self.snake.body[0] == (self.food.x, self.food.y):
            self.snake.mange()
            self.planet_alpha.despawn(self.food.x, self.food.y)
            self.food.x, self.food.y = self.planet_alpha.get_random_free_place()
            self.planet_alpha.spawn(self.food.x, self.food.y, self.food)
            self.score += 1
        if self.check_collision():
            self.game_over()
        else:
            self.root.after(self.snake.speed, self.update)

    # Méthode pour dessiner le serpent et la nourriture sur le canvas
    def draw(self):
        self.canvas.delete("all")
        for x, y in self.snake.body:
            self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="green", outline="")
        self.canvas.create_oval(self.food.x * 20, self.food.y * 20, (self.food.x + 1) * 20, (self.food.y + 1) * 20, fill="red", outline="")
        self.canvas.create_text(40, 40, text=f"Score: {self.score}", fill="white", font=("Arial", 14))

    # Méthode pour changer la direction du serpent
    def change_direction(self, new_direction: str):
        if new_direction == 'left':
            if self.snake.direction != 'right':
                self.snake.direction = new_direction
        elif new_direction == 'right':
            if self.snake.direction != 'left':
                self.snake.direction = new_direction
        elif new_direction == 'up':
            if self.snake.direction != 'down':
                self.snake.direction = new_direction
        elif new_direction == 'down':
            if self.snake.direction != 'up':
                self.snake.direction = new_direction

    # Méthode pour vérifier les collisions
    def check_collision(self):
        head_x, head_y = self.snake.body[0]
        if head_x < 0 or head_x >= self.planet_alpha.longitude_cells_count or head_y < 0 or head_y >= self.planet_alpha.latitude_cells_count:
            return True
        for segment in self.snake.body[1:]:
            if segment == self.snake.body[0]:
                return True
        return False

    # Méthode pour afficher la fin du jeu
    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2, text="Game Over", font=("Arial", 24), fill="red")
        score_text = self.canvas.create_text(40, 40, text=f"Score: {self.score}", font=("Arial", 14), fill="white")
        self.create_restart_button()

    # Méthode pour créer le bouton de redémarrage
    def create_restart_button(self):
        self.restart_button = Button(self.canvas, "Restart", self.restart_game, 160, 150)

    # Méthode pour redémarrer le jeu
    def restart_game(self):
        self.canvas.delete("all")
        self.destroy_restart_button()
        self.__init__(self.canvas, self.root)
        self.start()

    # Méthode pour détruire le bouton de redémarrage
    def destroy_restart_button(self):
        if hasattr(self, 'restart_button'):
            self.restart_button.destroy()
