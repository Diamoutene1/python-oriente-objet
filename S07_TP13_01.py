import tkinter as tk

if __name__=="__main__":
	TITLE="Test tkinter"
	WIDTH = 800
	HEIGH = 500
	POST_X = 100
	POS_Y = 50
	# initialiser yk
	app = tk.Tk()
	app.title(TITLE)
	app.geometry(f"{WIDTH}x{HEIGH}+{POST_X}+{POS_Y}")
	#  creer un frame
	monFrame = tk.Frame(app)
	monFrame.pack()
	#creer un canvas pour desssiner dessus
	canevas = tk.Canvas(monFrame, background='white')
	canevas.pack()
	#cree button quitter
	bouton = tk.Button(app, text="Quitter", command= app.quit)
	bouton.pack(side=tk.RIGHT)
	#creer l'app
	app.mainloop()
