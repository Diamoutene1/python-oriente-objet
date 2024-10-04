import tkinter as tk
from game_classes import Conway
from gamesnake import SnakeGame

# Définition de la classe GameChoiceDialog pour la boîte de dialogue de choix du jeu
class GameChoiceDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Choix du Jeu")
        self.geometry("300x100")
        self.choice = None

        # Éléments de la boîte de dialogue : étiquette et boutons de choix
        tk.Label(self, text="Choisissez le jeu à jouer :").pack(pady=5)
        tk.Button(self, text="Jeu de la Vie", command=self.choose_conway).pack(side=tk.LEFT, padx=10)
        tk.Button(self, text="Jeu du Serpent", command=self.choose_snake).pack(side=tk.RIGHT, padx=10)

    # Méthode pour choisir le Jeu de la Vie
    def choose_conway(self):
        self.choice = "Conway"
        self.destroy()

    # Méthode pour choisir le Jeu du Serpent
    def choose_snake(self):
        self.choice = "Snake"
        self.destroy()

# Définition de la classe MyApp pour l'application principale
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Affichage de la boîte de dialogue de choix du jeu
        choice_dialog = GameChoiceDialog(self)
        self.wait_window(choice_dialog)

        # Lancement du jeu sélectionné ou fermeture de l'application
        if choice_dialog.choice == "Conway":
            self.play_conway()
            self.title("Jeu de la vie")
        elif choice_dialog.choice == "Snake":
            self.play_snake()
        else:
            self.quit()

    # Méthode pour lancer le Jeu de la Vie
    def play_conway(self):
        self.frame_conway = tk.Frame(self)
        self.frame_conway.pack(side=tk.LEFT)
        canvas_conway = tk.Canvas(self.frame_conway, width=400, height=400, bg="black")
        canvas_conway.pack()

        # Initialisation du jeu de Conway et ajout des boutons de contrôle
        self.game_conway = Conway(canvas_conway, 30, 30)
        self.reset_button = tk.Button(self, text="Réinitialiser", command=self.game_conway.reset_game)
        self.reset_button.pack(side=tk.BOTTOM)
        self.pause_button = tk.Button(self, text="Pause", command=self.game_conway.toggle_game)
        self.pause_button.pack(side=tk.BOTTOM)

    # Méthode pour lancer le Jeu du Serpent
    def play_snake(self):
        self.frame_snake = tk.Frame(self)
        self.frame_snake.pack(side=tk.LEFT)
        canvas_snake = tk.Canvas(self.frame_snake, width=400, height=400, bg="black")
        canvas_snake.pack()

        # Initialisation du jeu du Serpent
        self.game_snake = SnakeGame(canvas_snake, self)
        self.game_snake.start()

# Point d'entrée de l'application
if __name__ == '__main__':
    MyApp().mainloop()
