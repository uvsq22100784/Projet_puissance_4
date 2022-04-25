import tkinter as tk
import random as rd

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

# Définition d’un joueur
class Joueur :
    def __init__ (outSelf, inCouleur, inNom="") :
        outSelf.couleur = int(inCouleur) # En fait, soit ROUGE, soit JAUNE
        outSelf.nom = str(inNom) # Le nom du joueur
        outSelf.ordinateur = bool(inNom=="") # Est-ce l’ordinateur ?
        if inNom == "" : outSelf.nom = "Ordinateur"
        outSelf.nb_victoires = int(0) # Nombre de victoires
# Définition des composants du jeu
class Jeu :
    def __init__(outSelf,inNomJoueur1,inNomJoueur2="") :
#1.grille de jeu avec une bordure supplémentaire sur les 4 bords
        outSelf.grille = [] # liste vide => on va lui rajouter les lignes
for ligne in range(NB_LIGNES+2) : # 2 lignes de plus pour les bords
    def symbole_case(inCouleur) : # str
        return SYMBOLE_COULEUR[inCouleur]
def afficher_numeros_colonnes() :
    j = int() # index pour parcourir les colonnes de la grille
print(" ",end=" ") # espace pour le bord droit
for j in range(1,NB_COLONNES+1) : print(j,end=" ")
print () # pour aller à la Ligne
def afficher_grille(inJeu) :
    i = int() ; j = int() # index pour parcourir les cases de la grille
#1.afficher le titre
print() # sauter une ligne
print(" ",TITRE) # ajout de 2 espaces pour centrer le titre sur la grille
#2.afficher le bord supérieur
afficher_numeros_colonnes()
#3.afficher la grille avec les bords gauche et droit
for i in range(NB_LIGNES,0,-1) : # on affiche d’abord la ligne supérieure
#3.1.afficher le numéro de ligne à gauche
    print (i,end=" ")
