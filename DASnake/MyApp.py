from tkinter import messagebox

import tkinter as tk

#from turmitegame import GameTurmite
#from Conway_Game import Conway
from SnakeGame import *
from tkinter import PhotoImage
from PIL import Image, ImageTk


class SnakeGameWindow(tk.Toplevel):
    """La classe SnakeGameWindow répresente la sous fénêtre de MyApp qui va accueillir le SnakeGame"""
    def __init__(self, master, **kw):
        """ Construction de la sous fenêtre SnakeGameWindow avec ses widgets"""
        tk.Toplevel.__init__(self, master, **kw)
        self.configure(bg="#6699CC")
        self.maxsize(2100,1000)
        self.__master = master
        self.mode = tk.StringVar()
        self.game_frame = tk.Frame(self, bg="#D2B48C")
        self.game_frame.pack(side="left", padx=10, pady=10)
        self.modes = ["Simple", "Classique", "Contre la montre","High-Level"]
        self.mode_frame=tk.Frame(self.game_frame,bg="#D2B48C")
        self.mode_frame.pack(fill="x",expand=True,pady=10)
        for i in range(len(self.modes)):
            tk.Radiobutton(self.mode_frame, text=self.modes[i], variable=self.mode, value=self.modes[i], command=self.setup_game,bg="#D2B48C",font=("Helvetica", 12, "bold")).grid(row=0, column=i+2, padx=(40, 80))
        self.affiche_mode=tk.Label(self.game_frame, text="Bienvenue dans le SnakeGame!", font=("Helvetica", 16, "bold"), bg="#D2B48C")
        self.affiche_mode.pack()
        self.__game = PlanetTK(self.game_frame, "snake", 30, 30, authorised_class=None, background_color="white", foreground_color="darkblue", gridlines_color="maroon", cell_size=20, gutter_size=0, margin_size=0, show_content=True, show_gridlines=False)
        self.__game.pack(side="top")
        self.setup_game()

        self.score_frame = tk.Frame(self)
        self.score_label = tk.Label(self.score_frame, text="Score: 0", font=("Helvetica", 12))
        
        self.score_label.pack()
        self.score_frame.pack(side="right", padx=10, pady=1)
        tk.Label(self.score_frame, text="Historique", font=("Helvetica", 16, "bold")).pack()
        self.score_list = tk.Listbox(self.score_frame, height=10, width=20)
        self.score_list.pack(pady=1)    
        # Boutons de contrôle  
        self.control_frame = tk.Frame(self.game_frame,bg="#D2B48C")
        self.control_frame.pack(side="bottom", pady=10,fill="x",expand=True)
        tk.Button(self.control_frame, text="Accueil",bg="Orange",width=15,height=2,font=("Helvetica", 12,"bold"),command=lambda:self.reset()).grid(row=0, column=4, padx=(90, 50))
        self.Pause=tk.Button(self.control_frame, text="Pause/Reprendre",bg="white",width=15,height=2,font=("Helvetica", 12,"bold"),command=lambda:self.__game.toggle_pause()).grid(row=0, column=6, padx=(0, 50))
        tk.Button(self.control_frame, text="Quitter le jeu",bg="green", width=15,height=2,font=("Helvetica", 12,"bold"),command=self.destroy).grid(row=0, column=9, padx=(0, 20))
        self.copy_r=tk.Frame(self)
        self.copy_r.pack(side="bottom")
        tk.Label(self.copy_r,text="By Aboubacar Sidik Dao",font=("Helvetica", 8, "bold")).pack(side="right")
        print("largeur ",self.winfo_width())
        print("Hauteur ",self.winfo_height())
    def reset(self):
        self.__game.destroy()
        self.__game = PlanetTK(self.game_frame, "snake", 30, 30, authorised_class=None, background_color="white", foreground_color="darkblue", gridlines_color="maroon", cell_size=20, gutter_size=0, margin_size=0, show_content=True, show_gridlines=False)
        self.__game.pack(side="top")
        self.affiche_mode.config(text="Bienvenue dans le SnakeGame!")           
        
    def update_score(self):
        """ Cette méthode met à jour le score affiché en fonction du score actuel du jeu"""
        score = self.__game.get_score()
        self.score_label.config(text="Score: " + str(score))
        self.after(100, self.update_score)
    
    def update_timer(self):
        """ Cette méthode met à jour le temps restant affiché en fonction du temps restant dans le jeu"""
        timer_seconds = self.__game.timer_seconds
        self.timer_label.config(text="Temps restant: " + str(timer_seconds))
        if timer_seconds > 0:
            self.after(1000, self.update_timer)  

    def create_game_mode(self, mode_name, game_class):
        """ La méthode create_game_mode() permettra de créer un mode de jeu"""
        if self.__game and self.__game.game_running:
            self.__game.game_running = False
            # Si un jeu est en cours et que l'utilisateur veut changer de mode, lui demander une confirmation avant de switcher.
            if not messagebox.askokcancel("Confirmation", "Un jeu est déjà en cours. Êtes-vous sûr de vouloir changer de mode ?"):
                self.__game.game_running = True
                return
        self.affiche_mode.config(text=f"MODE {mode_name.upper()}")
        self.__game.destroy()
        self.__game = game_class(self.game_frame, "snake", 30, 30, authorised_class=None, background_color="white", foreground_color="darkblue", gridlines_color="maroon", cell_size=20, gutter_size=0, margin_size=0, show_content=True, show_gridlines=False)
        self.__game.pack(side="top")
    
        self.load_scores(self.__game.file)
        if mode_name == "Contre la montre" or mode_name=="High-Level":
            
            #Vérification si une instance de jeu est en cours
            if hasattr(self, "timer_label") and self.timer_label:
                self.timer_label.destroy()
            self.timer_label = tk.Label(self.score_frame, text="Temps restant: 60", font=("Helvetica", 12))
            self.timer_label.pack()
            self.update_score()
            self.update_timer()
        else:
            self.update_score()    

    def setup_game(self):
        """Méthode pour configurer le jeu en fonction du mode sélectionné.
        Elle récupère le mode sélectionné par l'utilisateur et crée le jeu en fonction de ce mode.
        Si un jeu est déjà en cours, il est détruit avant de créer un nouveau jeu."""
        selected_mode = self.mode.get()
        if hasattr(self, "__game") and self.__game:
            self.__game.destroy()
        if selected_mode == "Simple":
            self.create_game_mode("Simple", SnakeGame)
        elif selected_mode == "Classique":
            self.create_game_mode("Classique", Classique_Mode)
        elif selected_mode == "Contre la montre":
            self.create_game_mode("Contre la montre", Timer_Mode)
        elif selected_mode == "High-Level":
            self.create_game_mode("High-Level", High_Level)
        
    def load_scores(self,file):
        """Méthode pour charger les scores à partir d'un fichier et les afficher dans une liste.
        Elle  efface la liste actuelle des scores, puis ouvre le fichier spécifié et lit les scores.
        Chaque score est ajouté à la liste des scores pour être affiché."""
        self.score_list.delete(0, tk.END)
        try:
            with open(file, "r") as file:
                scores = file.readlines()
                for line in scores:
                    # Vérifier que la ligne contient deux parties (nom du joueur et score)
                    if ":" in line:
                        player, score = line.strip().split(": ")
                        self.score_list.insert(tk.END, f"{player}: {score}")
                    else:
                        # Les lignes mal renseignées sont ignorées 
                        continue
        except FileNotFoundError:
            # Fichier inexistant, pas de scores à charger
            pass


class TurmitesWindow(tk.Toplevel):

    def __init__(self, master, **kw):
        tk.Toplevel.__init__(self, master, **kw)
        self.__master = master
        main_frame = tk.Frame(self)
        main_frame.pack(fill="both", expand=True)
        # Frame pour l'image et les boutons
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side="left")
        # Ajout de l'image de Turmite
        turmite_image = tk.PhotoImage(file="images/coloriage-fourmi-6942.png")
        self.turmite_label = tk.Label(left_frame, image=turmite_image)
        self.turmite_label.image = turmite_image
        self.turmite_label.pack()
        # Cadre pour les boutons
        button_frame = tk.Frame(left_frame)
        button_frame.pack()
        # Création des boutons
        button_styles = {'bg': 'orange', 'fg': 'white', 'activebackground': 'darkorange', 'activeforeground': 'white', 'padx': 10, 'pady': 5}
        self.start_button = tk.Button(button_frame, text="Démarrer", command=self.start_simulation, **button_styles)
        self.stop_button = tk.Button(button_frame, text="Arrêter", command=self.stop_simulation, **button_styles)
        self.set_position_button = tk.Button(button_frame, text="Définir Position", command=self.set_position, **button_styles)
        self.show_state_button = tk.Button(button_frame, text="Afficher État", command=self.show_state, **button_styles)
        self.add_turmite_button = tk.Button(button_frame, text="Ajouter Turmite", command=self.add_turmite, **button_styles)
        # Placement des boutons
        self.start_button.grid(row=0, column=0)
        self.stop_button.grid(row=0, column=1)
        self.set_position_button.grid(row=1, column=0)
        self.show_state_button.grid(row=1, column=1)
        self.add_turmite_button.grid(row=2, column=0, columnspan=2)
        # Frame pour la grille
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side="left")
        # Ajout du composant GameTurmite à la fenêtre
        self.game_turmite = GameTurmite(right_frame, "Turmite", 60, 60, 60,cell_size=700//60)
        self.game_turmite.pack(fill="both", expand=True)

    def add_turmite(self):
        # Méthode pour ajouter une turmite
        self.game_turmite.set_position()

    def start_simulation(self):
        # Méthode pour démarrer la simulation
        self.game_turmite.start_simulation()

    def stop_simulation(self):
        # Méthode pour arrêter la simulation
        self.game_turmite.stop_simulation()

    def set_position(self):
        # Méthode pour définir la position initiale de la turmite
        self.game_turmite.set_position()

    def show_state(self):
        # Méthode pour afficher l'état actuel de la turmite
        self.game_turmite.show_state()


class ConwayWindow(tk.Toplevel):

    def __init__(self, master, **kw):
        tk.Toplevel.__init__(self, master, **kw)
        self.__master = master
        self.__game = Conway(self, "Conway", 25, 25, 10, background_color="white", foreground_color="black", gridlines_color="blue", cell_size=20)
        self.__game.pack()
        tk.Button(self, text="Quit", command=self.destroy).pack()


class MyApp(tk.Tk):
    """Configuration de la fenêtre principale"""
    def __init__(self):
        super().__init__()
        self.title("MULTI-JEU")
        self.config(bg="#AFEEEE")
        self.frame = tk.Frame(self, bg="#AFEEEE")
        self.frame.pack()
        self.afficher_message_bienvenue()
        self.images = {}
        self.jeux_images = {
            "Conway": ("images/conway.jpeg", "#D2B48C", ConwayWindow),
            "Turmites": ("images/turmite.jpeg", "#FF7F50", TurmitesWindow),
            "SnakeGame": ("images/snake.png", "#FFD700", SnakeGameWindow)
        }

        for jeu, infos_jeu in self.jeux_images.items():
            description = self.obtenir_description(jeu)
            self.afficher_jeu(jeu, description, infos_jeu[2], infos_jeu[1])
        tk.Button(self, text='Quitter', command=self.quit, bg="red", width=8, height=2, font=("Helvetica", 12, "bold")).pack()
        tk.Label(text="By Aboubacar Sidik Dao",font=("Helvetica", 8, "bold")).pack(side="right")
    def afficher_message_bienvenue(self):
        """"Affichage d'un message de bienvenue sur un label"""
        tk.Label(self.frame, text="Préparez-vous à une aventure épique dans notre univers de jeux!", font=("Comic Sans MS", 20, "bold"), fg="black", bg="#AFEEEE").pack(pady=20)

    def obtenir_description(self, jeu):
        """Méthode pour récuperer les descriptions de chaque jeu"""
        descriptions = {
            "Conway": "Explorez un univers fascinant où des formes simples évoluent de manière complexe dans ce jeu de simulation captivant basé sur les règles de Conway.",
            "Turmites": "Plongez dans un monde intrigant où une simple fourmi mécanique se déplace sur une grille infinie en noir et blanc, créant des motifs étonnants et des comportements imprévisibles.",
            "SnakeGame": "Défiez vos réflexes dans ce jeu classique du serpent où vous guidez la créature vorace à travers un terrain parsemé de délices, en évitant de se mordre la queue."
        }
        return descriptions.get(jeu, "")

    def afficher_jeu(self, jeu, description, window, bac):
        """Affichage des trois  jeux sur la fénêtre principale"""
        frame = tk.Frame(self.frame, bd=2, relief=tk.RAISED, bg=bac)
        frame.pack(side=tk.LEFT, padx=30, pady=10)
        label_titre = tk.Label(frame, text=jeu, font=('Comic Sans MS', 20, 'bold'), bg=bac)
        label_titre.pack(pady=(10, 5))
        photo_image = self.charger_image(self.jeux_images[jeu][0])
        self.images[jeu] = photo_image
        label_image = tk.Label(frame, image=photo_image)
        label_image.pack()
        label_description = tk.Label(frame, text=description, wraplength=200, bg=bac, font=("Arial", 14, ""))
        label_description.pack()
        bouton_jouer = tk.Button(frame, text="Jouer", width=10, font=("Helvetica", 12,"bold"),command=lambda: window(self), bg=bac)
        bouton_jouer.pack(pady=(5, 10))

    def charger_image(self, chemin_image):
        """ Cette méthode a pour rôle de charger les images correspondants à chaque jeu. Elle sera utlisée dans afficher_jeu() pour récuperer les images et les placer dans la fénêtre principale"""
        image = Image.open(chemin_image)
        image = image.resize((150, 150), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(image)
        return photo_image

if __name__ == '__main__':
    MyApp().mainloop()