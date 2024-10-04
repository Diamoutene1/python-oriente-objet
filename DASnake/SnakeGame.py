import tkinter as tk
from PlanetTk import PlanetTK
from Element import Snake
import random
from tkinter import simpledialog



class SnakeGame(PlanetTK):

    obstacle_color="red"
    food_color="green"
    
    def __init__(self, root, name, latitude_cells_count, longitude_cells_count, authorised_class, background_color="white", foreground_color="darkblue", gridlines_color="maroon", cell_size=20, gutter_size=0, margin_size=0, show_content=True, show_gridlines=True, **kw):
        """ Initialisation du plateau de jeu  dans lequel va se dérouler le jeu"""
        PlanetTK.__init__(self, root, name, latitude_cells_count, longitude_cells_count, authorised_class, background_color, foreground_color, gridlines_color, cell_size, gutter_size, margin_size, show_content, show_gridlines, **kw)
        self.__Snake = Snake(latitude_cells_count, longitude_cells_count, char_repr=None,taille=1,vitesse=260)
        self.__vitesse=self.__Snake.get_vitesse()
        self.timer_seconds = 60 
        self.obstacle_color="red"
        self.food_color="green"
        self.paused=False
        self.root=root
        self.move_id=None
        self.liste_obstacle = [] 
        self.lat = latitude_cells_count
        self.long = longitude_cells_count
        self.line_direction = "RIGHT"
        self.cell_ocuup = [self.get_cell_number_from_coordinates(self.__Snake.get_parts()[len(self.__Snake.get_parts()) - i - 1][0], self.__Snake.get_parts()[len(self.__Snake.get_parts()) - i - 1][1]) for i in range(len(self.__Snake.get_parts()))]
        self.queu=self.cell_ocuup[-1]
        self.head=self.cell_ocuup[0]
        self.food = None  # Position de la nourriture
        self.game_running = True 
        self.score = 0  # Initialize the score attribute
        self.bind("<KeyPress>", self.change_direction)
        self.focus_set()
        self.move_snake()
        self.generate_food()  # Générer la nourriture au démarrage du jeu
        self.player_name=None
        self.file="Historique_SnakeGame/simple_scores.txt"
        self.paused=False
    

    
    def get_cell_occ(self):
        """ Accesseur en lecture qui permet de récupérer la liste des cellules ocuupées par le serpent"""
        return self.cell_ocuup
        
    def get_score(self):
        """Permet de récupere le score"""
        return self.score

    def get_queu(self):
        """Récupère la numéro de la cellule sans laquelle se trouve la queu du serpent"""
        return self.queu

    def die(self, cell_number,color):
        """Une spécialiation de la méthode die() de PlanetTk qui au lieu de travailler avec l'élément contenu dans la cellule
        travaillera plûtot avec les couleurs de remplissage """
        self.set_cell_colors(cell_number, color,filled=False)

    def born(self, cell_number,color):
        """Une spécialiation de la méthode born() de PlanetTk qui au lieu de travailler avec l'élément contenu dans la cellule
        travaillera plûtot avec les couleurs de remplissage """
        self.set_cell_colors(cell_number, color,filled=True)

    def move_element(self, cell, new_cell):
        """Spécialiation de la méthode move_element() de PlanetTk """
        self.die(cell,color=None)
        self.born(new_cell,self.get_foreground_color())
    def generate_obstacles(self):
        """ Permet de  Générer des obstacles de manière aléatoire """
        num_obstacles = min(40, self.lat * self.long // 10)  # Limite le nombre d'obstacles
        for _ in range(num_obstacles):
            while True:
                obstacle_cell = random.randint(0, self.lat * self.long - 1)
                if obstacle_cell not in self.cell_ocuup and obstacle_cell != self.food and obstacle_cell not in self.liste_obstacle:
                    self.liste_obstacle.append(obstacle_cell)
                    self.born(obstacle_cell,self.obstacle_color)
                    break
    



    def start_timer(self):
        """Cette méthode joue le rôle de minuteur, dès que le self.timer_seconds passe à 0, elle met fin au jeu"""
        if self.game_running:
            self.timer_seconds -= 1
            self.timer_label.config(text=f"Temps restant: {self.timer_seconds}")
        if self.timer_seconds > 0:
            self.after(1000, self.start_timer)
        else:
            self.game_running = False
            self.Game_Over("Temps écoulé",self.file)
    def calculate_new_head_position(self):
        """Cette méthode renvoie la position de la nouvelle tếte en fonction de la direction courante du serpent """
        if self.line_direction == "RIGHT":
            new_head = self.head + 1
            if new_head % self.long == 0:
                new_head -= self.long
            else:
                new_head=new_head
        elif self.line_direction == "LEFT":
            new_head = self.head - 1
            if new_head % self.long == self.long - 1:
                new_head += self.long
            else:
                new_head=new_head
        elif self.line_direction == "UP":
            new_head = self.head - self.long
            if new_head < 0:
                new_head += self.lat * self.long
        elif self.line_direction == "DOWN":
            new_head = self.head + self.long
            if new_head >= self.lat * self.long:
                new_head -= self.lat * self.long
        return new_head

    def toggle_pause(self):
        """Activer ou désactiver la pause."""
        self.paused = not self.paused
        self.game_running=not self.game_running
        

        if self.paused:
            # Arrêter le mouvement si le jeu est en pause
            self.after_cancel(self.move_id)
        else:
            # Reprendre le mouvement si le jeu n'est pas en pause
            self.move_snake()
    def change_direction(self, event):
        """Méthode de changement de directement du serpent sur le plateau de jeu graâce aux 4 touches de direction"""
        key = event.keysym
        if key == "Up" and self.line_direction != "DOWN":
            self.line_direction = "UP"
        elif key == "Down" and self.line_direction != "UP":
            self.line_direction = "DOWN"
        elif key == "Left" and self.line_direction != "RIGHT":
            self.line_direction = "LEFT"
        elif key == "Right" and self.line_direction != "LEFT":
            self.line_direction = "RIGHT"
        elif key == "space" :  # Si la barre d'espace est pressée, inversez l'état du jeu
            self.toggle_pause()
    def generate_food(self):
        """ Génération de la nourriture sur le plateau de jeu de manière aléatoire  (position aleéatoire) """     
        while True:
            food_cell = random.randint(0,self.lat*self.long-1)
            if food_cell not in self.cell_ocuup:
                self.food = food_cell
                self.born(self.food,self.food_color)
                break
    def ask_player_name(self):
        """ Méthode pour récuperer le nom du joueur afin de le sauvegarder après dans l'historique, cette méthode sera déclenchée après un Game_Over"""
        if not self.player_name:
            self.player_name = simpledialog.askstring("Nom du joueur", "Entrez votre nom:")
            if not self.player_name:
                self.player_name = "Joueur Anonyme"
                return self.player_name 
    def move_snake(self):
        """Méthode de démarrage du jeu qui conditionne tous les évènements succeptibles de se réaliser et les comportement qui en résultent"""
        if self.game_running:
            if not self.paused:
                new_head = self.calculate_new_head_position()  
                queu=self.get_queu() 
                if new_head in self.cell_ocuup  or new_head in self.liste_obstacle:
                    self.Game_Over("Bro, C'est Djinzin hein!",self.file)
                    self.ask_player_name()
                    print(self.player_name)
                    return
                if new_head == self.food:  # Si le serpent atteint la nourriture
                    if self.line_direction == "RIGHT": 
            # Si le serpent se déplace vers la droite, ajoutez une nouvelle cellule à droite de la tête
                        self.cell_ocuup.append(new_head + 1) 
                    elif self.line_direction == "LEFT": 
            # Si le serpent se déplace vers la gauche, ajoutez une nouvelle cellule à gauche de la tête
                        self.cell_ocuup.append(new_head - 1) 
                    elif self.line_direction == "UP": 
            # Si le serpent se déplace vers le haut, ajoutez une nouvelle cellule au-dessus de la tête
                        self.cell_ocuup.append(new_head - self.long) 
                    elif self.line_direction == "DOWN": 
            # Si le serpent se déplace vers le bas, ajoutez une nouvelle cellule en dessous de la tête
                        self.cell_ocuup.append(new_head + self.long) 
                    self.generate_food()  # Générez une nouvelle nourriture
                    self.score+=1
                    if self.score%5 and self.__vitesse>150:
                        self.__vitesse-=5
                self.cell_ocuup.pop()
                self.cell_ocuup.insert(0,new_head)
                self.move_element(queu, new_head)
                self.queu=self.cell_ocuup[-1]
                self.head=self.cell_ocuup[0]
            #time.sleep(self.__vitesse / 1000)  # Délai en secondes
        self.move_id=self.after(self.__vitesse, self.move_snake)
       
    
    def Game_Over(self, message,file):
        """ Cette méthode permet de mettre fin à une instance de jeu en donnant la valeur False à l'attribut self.game_running.
        Une deuxième mission qui est de sauvegarder le joueur dans l'historique a été donné à cette méthode."""
        game_over_label = tk.Label(self, text=message + " Score: " + str(self.get_score()), font=("Helvetica", 24), bg="red", fg="white")
        game_over_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.game_running=False
        if not self.player_name:
            self.player=self.ask_player_name()
    # Save player's name and score to file
        if self.player_name:
            with open(file, "a") as file:
                file.write(f"{self.player_name}: {self.get_score()}\n")
       

class Classique_Mode(SnakeGame):
    """Une spécialisation de la classe SnakeGame qu'on va appeler Classique_Mode. Ce mode a la particularité de contenir des obstacles dans le plateu de jeu"""
    def __init__(self, root, name, latitude_cells_count, longitude_cells_count, authorised_class, background_color="white", foreground_color="darkblue", gridlines_color="maroon", cell_size=20, gutter_size=0, margin_size=0, show_content=True, show_gridlines=True, **kw):
        #self.liste_obstacle = [] 
        SnakeGame.__init__(self,root, name, latitude_cells_count, longitude_cells_count, authorised_class, background_color, foreground_color, gridlines_color, cell_size, gutter_size, margin_size, show_content, show_gridlines, **kw)
        self.file="Historique_SnakeGame/classic_scores.txt"
        self.generate_obstacles()
        #print(self.liste_obstacle)
 

class Timer_Mode(SnakeGame):
    """Une spécialisation de la classe SnakeGame qu'on va appeler Timer_Mode. Il s'agit du mode contre-la-montre dans lequel lejoueur est améné récolter le plus de points dans un laps de temps déterminé"""
    def __init__(self, root, name, latitude_cells_count, longitude_cells_count, authorised_class, background_color="white", foreground_color="darkblue", gridlines_color="maroon", cell_size=20, gutter_size=0, margin_size=0, show_content=True, show_gridlines=True, **kw):
        SnakeGame.__init__(self,root, name, latitude_cells_count, longitude_cells_count, authorised_class, background_color, foreground_color, gridlines_color, cell_size, gutter_size, margin_size, show_content, show_gridlines, **kw)
        self.timer_seconds = 60  # Temps initial pour le mode contre la montre
        self.timer_label = tk.Label(self, text=f"Temps restant: {self.timer_seconds}", font=("Helvetica", 12))
        self.file="Historique_SnakeGame/timer_scores.txt"
        self.start_timer() 

    
    
class High_Level(SnakeGame):
    """Une spécialisation de la classe SnakeGame qu'on va appeler Timer_Mode. Il s'agit du mode High_Level qui est un mixe du mode classique et du mode contre la montre """

    def __init__(self, root, name, latitude_cells_count, longitude_cells_count, authorised_class, background_color="white", foreground_color="darkblue", gridlines_color="maroon", cell_size=20, gutter_size=0, margin_size=0, show_content=True, show_gridlines=True, **kw):
        SnakeGame.__init__(self,root, name, latitude_cells_count, longitude_cells_count, authorised_class, background_color, foreground_color, gridlines_color, cell_size, gutter_size, margin_size, show_content, show_gridlines, **kw)
        self.timer_label = tk.Label(self, text=f"Temps restant: {self.timer_seconds}", font=("Helvetica", 12))
        self.file="Historique_SnakeGame/high_level_scores.txt"
        self.generate_obstacles()
        self.timer_seconds = 60  # Temps initial pour le mode contre la montre
        
        self.start_timer() 





if __name__ == "__main__":
    root = tk.Tk()
    root.title("DASnake")
    PLANET_TEST = SnakeGame(root, "snake", 30, 50, authorised_class=None,background_color="white", foreground_color="darkblue", gridlines_color="maroon", cell_size=20, gutter_size=0, margin_size=0, show_content=True, show_gridlines=False)
    PLANET_TEST.pack()
    root.mainloop()