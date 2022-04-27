from tkinter import *
import random

jeu=Tk()
# CONSTANTES
TITRE = "PUISSANCE 4"
# Nombre de lignes de l’aire de jeu
NB_LIGNES = int(6)
# Nombre de colonnes de l’aire de jeu 
NB_COLONNES = int(7)
# Nombre de pions alignés pour gagner
NB_ALIGNES_GAGNANT = int(4)
# Nombre de joueurs dans une partie
NB_JOUEURS = int(2)
# Couleurs
VIDE = 0 ; ROUGE = 1 ; JAUNE = 2
# Lettre associée
SYMBOLE_COULEUR = (" ","*","o")

# Construction de la grille
def ligne_verticale(x):
    x1=x
    y1=100
    x2=x
    y2=700
    Zone.create_line(x1,y1,x2,y2,width=1,fill="black")

def ligne_horizontale(x):
    x1=100
    y1=x
    x2=800
    y2=x
    Zone.create_line(x1,y1,x2,y2,width=1,fill="black")

Zone=Canvas(jeu,width=1000,height=900,bg="white")
Zone.place(x=0,y=0)
x=0
while x!=900:
    ligne_verticale(x)
    x=x+100

x=0
while x!=800:
    ligne_horizontale(x)
    x=x+100


chaine = Label(jeu)
chaine.pack()
jeu.mainloop()