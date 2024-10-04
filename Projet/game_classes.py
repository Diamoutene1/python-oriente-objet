import tkinter as tk  # Importation de la bibliothèque tkinter pour l'interface graphique
import random  # Importation du module random pour la génération aléatoire

class PlanetAlpha:  # Définition de la classe PlanetAlpha
    def __init__(self, name):  # Initialisation de la classe avec le nom de la planète
        self.name = name  # Attribution du nom à l'attribut de l'instance

    def display_name(self):  # Méthode pour afficher le nom de la planète
        print("Name:", self.name)  # Affichage du nom de la planète

class Tk(PlanetAlpha):  # Définition de la classe Tk qui hérite de PlanetAlpha
    def __init__(self, master, name):  # Initialisation de la classe avec un maître et un nom
        super().__init__(name)  # Appel du constructeur de la classe parente
        self.master = master  # Attribution du maître à l'attribut de l'instance
        self.conway_game = Conway(master, 10, 10)  # Initialisation du jeu de Conway
        self.title('jeu de la vie')  # Définition du titre de la fenêtre

class Element:  # Définition de la classe Element
    def __init__(self, x, y, state):  # Initialisation de la classe avec des coordonnées et un état
        self.x = x  # Attribution de la coordonnée x à l'attribut de l'instance
        self.y = y  # Attribution de la coordonnée y à l'attribut de l'instance
        self.state = state  # Attribution de l'état à l'attribut de l'instance

    def count_human_neighbors(self, grid):  # Méthode pour compter les voisins humains
        count = 0  # Initialisation du compteur
        for i in range(-1, 2):  # Boucle sur les voisins en x
            for j in range(-1, 2):  # Boucle sur les voisins en y
                if (i != 0 or j != 0) and 0 <= self.x + i < grid.width and 0 <= self.y + j < grid.height:
                    # Vérification des coordonnées valides dans la grille
                    if grid.cells[self.x + i][self.y + j].state == 1:  # Si le voisin est humain
                        count += 1  # Incrément du compteur
        return count  # Retour du nombre de voisins humains

class Human(Element):  # Définition de la classe Human qui hérite de Element
    def __init__(self, x, y, state):  # Initialisation de la classe avec des coordonnées et un état
        super().__init__(x, y, state)  # Appel du constructeur de la classe parente

class Conway(Element):  # Définition de la classe Conway qui hérite de Element
    def __init__(self, master, width, height):  # Initialisation de la classe avec un maître, une largeur et une hauteur
        super().__init__(0, 0, 0)  # Appel du constructeur de la classe parente
        self.master = master  # Attribution du maître à l'attribut de l'instance
        self.width = width  # Attribution de la largeur à l'attribut de l'instance
        self.height = height  # Attribution de la hauteur à l'attribut de l'instance
        self.game = GameOfLife(width, height)  # Initialisation du jeu de la vie
        self.canvas = tk.Canvas(master, width=width*20, height=height*20)  # Création d'un canevas pour l'affichage
        self.canvas.pack()  # Affichage du canevas
        self.draw_grid()  # Dessin de la grille

        self.dead_count = 0  # Initialisation du compteur de morts
        self.born_count = 0  # Initialisation du compteur de naissances
        self.label = tk.Label(master, text="")  # Création d'une étiquette pour afficher les statistiques
        self.label.pack()  # Affichage de l'étiquette

        self.canvas.bind("<Enter>", self.start_game)  # Liaison de l'événement "Entrée" au démarrage du jeu
        self.canvas.bind("<Leave>", self.stop_game)  # Liaison de l'événement "Sortie" à l'arrêt du jeu
        self.canvas.bind("<Button-1>", self.click_cell)  # Liaison de l'événement "Clic gauche" à l'interaction avec les cellules

        self.game_running = False  # Initialisation de l'état du jeu à arrêté
        self.paused = False  # Initialisation de l'état du jeu à non suspendu
        self.speed = 100  # Initialisation de la vitesse du jeu

        self.speed_button = tk.Button(master, text="Vitesse: Normal", command=self.toggle_speed)  # Création d'un bouton pour changer la vitesse
        self.speed_button.pack()  # Affichage du bouton

        self.quit_button = tk.Button(master, text="Quitter", command=self.quit_game)  # Création d'un bouton pour quitter le jeu
        self.quit_button.pack(side=tk.BOTTOM)  # Affichage du bouton

    def draw_grid(self):  # Méthode pour dessiner la grille
        self.canvas.delete("all")  # Effacement de tout ce qui est dessiné sur le canevas
        for x in range(self.width):  # Boucle sur les colonnes de la grille
            for y in range(self.height):  # Boucle sur les lignes de la grille
                if self.game.grid.cells[x][y].state == 1:  # Si la cellule est vivante
                    self.canvas.create_rectangle(x*20, y*20, (x+1)*20, (y+1)*20, fill="black")  # Dessiner une cellule vivante
                else:
                    self.canvas.create_rectangle(x*20, y*20, (x+1)*20, (y+1)*20, fill="white")  # Dessiner une cellule morte

    def start_game(self, event):  # Méthode pour démarrer le jeu
        if not self.paused:  # Si le jeu n'est pas suspendu
            self.game_running = True  # Mettre l'état du jeu à démarré
            self.game_loop()  # Démarrer la boucle de jeu

    def stop_game(self, event):  # Méthode pour arrêter le jeu
        self.game_running = False  # Mettre l'état du jeu à arrêté

    def game_loop(self):  # Méthode pour la boucle de jeu
        if self.game_running:  # Si le jeu est en cours
            dead_count, born_count = self.game.simulate_step()  # Simuler une étape du jeu
            self.dead_count += dead_count  # Mettre à jour le compteur de morts
            self.born_count += born_count  # Mettre à jour le compteur de naissances
            self.label.config(text=f"Nombre d'humains morts : {self.dead_count}\nNombre d'humains nés : {self.born_count}")  # Mettre à jour les statistiques
            self.draw_grid()  # Dessiner la grille
            self.master.after(self.speed, self.game_loop)  # Planifier la prochaine étape du jeu après un délai de vitesse

    def click_cell(self, event):  # Méthode pour interagir avec les cellules en cliquant
        cell_x = event.x // 20  # Calcul de la colonne de la cellule cliquée
        cell_y = event.y // 20  # Calcul de la ligne de la cellule cliquée
        cell = self.game.grid.cells[cell_x][cell_y]  # Récupération de la cellule correspondante dans la grille
        cell.state = 1 if cell.state == 0 else 0  # Inversion de l'état de la cellule (vie/mort)
        self.draw_grid()  # Dessiner la grille mise à jour

    def toggle_game(self, event=None):  # Méthode pour suspendre ou reprendre le jeu
        if self.paused:  # Si le jeu est suspendu
            self.paused = False  # Reprise du jeu
            if self.game_running:  # Si le jeu est en cours
                self.game_loop()  # Démarrer la boucle de jeu
        else:  # Si le jeu est en cours
            self.paused = True  # Suspension du jeu

    def toggle_speed(self):  # Méthode pour changer la vitesse du jeu
        if self.speed == 100:  # Si la vitesse est normale
            self.speed = 50  # Changer la vitesse à rapide
            self.speed_button.config(text="Vitesse: Rapide")  # Mettre à jour l'étiquette du bouton
        elif self.speed == 50:  # Si la vitesse est rapide
            self.speed = 200  # Changer la vitesse à lente
            self.speed_button.config(text="Vitesse: Lent")  # Mettre à jour l'étiquette du bouton
        else:  # Si la vitesse est lente
            self.speed = 100  # Changer la vitesse à normale
            self.speed_button.config(text="Vitesse: Normal")  # Mettre à jour l'étiquette du bouton

    def reset_game(self, event=None):  # Méthode pour réinitialiser le jeu
        self.game.grid.populate_grid()  # Réinitialiser la grille
        self.dead_count = 0  # Réinitialiser le compteur de morts
        self.born_count = 0  # Réinitialiser le compteur de naissances
        self.label.config(text=f"Nombre d'humains morts : {self.dead_count}\nNombre d'humains nés : {self.born_count}")  # Mettre à jour les statistiques
        self.draw_grid()  # Dessiner la grille mise à jour

    def quit_game(self):  # Méthode pour quitter le jeu
        self.master.quit()  # Quitter l'application

class GameOfLife:  # Définition de la classe GameOfLife
    def __init__(self, width, height):  # Initialisation de la classe avec une largeur et une hauteur
        self.grid = Grid(width, height)  # Initialisation de la grille du jeu

    def simulate_step(self):  # Méthode pour simuler une étape du jeu
        return self.grid.simulate_step()  # Retourner le résultat de la simulation de la grille

class Grid:  # Définition de la classe Grid
    def __init__(self, width, height):  # Initialisation de la classe avec une largeur et une hauteur
        self.width = width  # Attribution de la largeur à l'attribut de l'instance
        self.height = height  # Attribution de la hauteur à l'attribut de l'instance
        self.cells = [[Element(x, y, 0) for y in range(height)] for x in range(width)]  # Initialisation de la grille de cellules avec des cellules mortes
        self.populate_grid()  # Remplissage aléatoire de la grille

    def populate_grid(self):  # Méthode pour remplir aléatoirement la grille
        for x in range(self.width):  # Boucle sur les colonnes de la grille
            for y in range(self.height):  # Boucle sur les lignes de la grille
                if random.random() < 0.1:  # Si un nombre aléatoire est inférieur à 0.1
                    self.cells[x][y].state = 1  # Définir l'état de la cellule à vivant

    def simulate_step(self):  # Méthode pour simuler une étape du jeu
        dead_count = 0  # Initialisation du compteur de morts
        born_count = 0  # Initialisation du compteur de naissances
        new_grid = [[Element(x, y, 0) for y in range(self.height)] for x in range(self.width)]  # Initialisation d'une nouvelle grille
        for x in range(self.width):  # Boucle sur les colonnes de la grille
            for y in range(self.height):  # Boucle sur les lignes de la grille
                cell = self.cells[x][y]  # Récupération de la cellule actuelle
                neighbors_count = cell.count_human_neighbors(self)  # Compter le nombre de voisins humains
                if (neighbors_count == 3) or (cell.state == 1 and neighbors_count == 2):  # Si les règles du jeu de la vie sont respectées
                    new_grid[x][y].state = 1  # La cellule reste vivante ou naît
                    if cell.state == 0:  # Si la cellule était morte
                        born_count += 1  # Incrémenter le compteur de naissances
                else:  # Sinon
                    new_grid[x][y].state = 0  # La cellule meurt
                    if cell.state == 1:  # Si la cellule était vivante
                        dead_count += 1  # Incrémenter le compteur de morts
        self.cells = new_grid  # Mettre à jour la grille avec la nouvelle génération de cellules
        return dead_count, born_count  # Retourner le nombre de morts et de naissances
