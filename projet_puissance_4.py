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

def trace_ligne_ver(x):
    x1=x
    y1=100
    x2=x
    y2=700
    Zone.create_line(x1,y1,x2,y2,width=1,fill="black")

def trace_ligne_hor(x):
    x1=100
    y1=x
    x2=800
    y2=x
    Zone.create_line(x1,y1,x2,y2,width=1,fill="black")

Zone=Canvas(jeu,width=1000,height=900,bg="white")
Zone.place(x=0,y=0)
x=0

while x!=900:
    trace_ligne_ver(x)
    x=x+100

x=0
while x!=800:
    trace_ligne_hor(x)
    x=x+100

Joueur=random.randint(1,2)
total=0
def Attendre_clic(event):
    global JEU
    global Joueur
    Nbre_jetons=0
    global total
    xClic,yClic = event.x,event.y
    if 100<xClic<800: #Vérifier que le clic est dans le tableau
        colonne=Recherche_colonne(xClic)
        ligne=Recherche_ligne(colonne)


        if Joueur==1: #tour joueur rouge
            Zone.create_oval(colonne*100-20+150,ligne*100+170,colonne*100+20+150,ligne*100+130, fill='red') #Placement du jeton au milieu de la case
            Joueur=2
            print("C'est au tour du joueur 2")
            JEU[ligne][colonne]=1      #Définir que cette case est rouge dans le tableau
            total=total+1


        elif Joueur==2: #Tour du joueur jaune
            Zone.create_oval(colonne*100-20+150,ligne*100+170,colonne*100+20+150,ligne*100+130, fill='yellow')
            Joueur=1
            print("C'est au tour du joueur 1")
            JEU[ligne][colonne]=2
            total=total+1



    if total==42: #Vérification de tout les jetons placés pour l'égalité
        print("égalité")
jeu.bind("<Button-1>", Attendre_clic)

def Recherche_colonne(xClic):
    colonne=(xClic)//100-1 #Définir dans quelle colonne est le clic
    return colonne

def Recherche_ligne(colonne):
    ligne1=5
    for loop in range (6):        #Vérifier si des jetons sont déjà présent dans la colonne pour choisir la ligne
        if JEU[ligne1][colonne]==0:
            ligne=ligne1
        else:
            ligne1=ligne1-1
    return ligne



chaine = Label(jeu)
chaine.pack()
jeu.mainloop()