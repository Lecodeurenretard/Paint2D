# ###########################################################
#
# Name : graphique.py
# Rôle : Bibliothèque permettant une utilisation
#		simplifiée de la bibliothèque pygame.
#
# Author:	  Jean-Christophe Dagnet - Lycée Louis Bascan
# Sources :	Inspiré de la bibliothèque graphics.c - UVSQ site de Versailles
#
# Created:	 04/04/2019
# Version:	 2.0
# MAJ :		04/2023
# Copyright:   (c) JC 2019
#
# ###########################################################
#
#	  Lycee Louis Bascan -- Rambouillet
#	  Specialite N.S.I
#
# Professeur : Jean-Christophe DAGNET
#
# ############################################################
#
#   SOMMAIRE :
#
#   1. GESTION D'EVENNEMENTS			Ligne 59
#	  - Fermeture de fenêtre		   Ligne 64
#	  - Clic souris (bloquant)		 Ligne 85
#	  - Gestion souris (non bloquant)  Ligne 130
#	  - Gestion clavier				Ligne 180
#   2. AFFICHAGE DE TEXTE			   Ligne 247
#   3. GESTION D'IMAGES				 Ligne 271
#   4. GESTION DES SONS ET MUSIQUES	 Ligne 324
#	  - PARTIE 4.1 : SONS			  Ligne 329
#	  - PARTIE 4.2 : Musiques		  Ligne 366
#   5 GESTION DU TEMPS				  Ligne 443
#   6. VARIABLES COULEURS			   Ligne 475
#		   - Fançais				   Ligne 480
#		   - Anglais				   Ligne 502
#
# ############################################################


# Importation de la bibliothèque Pygame et de ses constantes
import pygame
from pygame.locals import *

# Initialisation de tous les modules de la bibliothèque pygame
pygame.init()

# Changement de l'icone et du titre
icon_NSI = pygame.image.load("img/NSI.png")
pygame.display.set_icon(icon_NSI)
pygame.display.set_caption("Paint (Projet de NSI)")


#----------------------------------------------------------#
#-----------------						 ----------------#
#				 1. GESTION D'EVENNEMENTS				 #
#-----------------						 ----------------#
#----------------------------------------------------------#

###########################################################
# PARTIE 1 : Fonction bloquante d'attente de fermeture de la fenêtre
# suite à un évenement QUIT (ctrl+F4 ou clic sur la croix rouge)
###########################################################

def wait_escape():
	"""
	Fonction blocante. Attente de fermeture de la fenêtre SDL
	"""
	continuer = 1
	while continuer:
		pygame.time.wait(200)
		for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
			if event.type == QUIT:		# Si un de ces événements est de type QUIT
				continuer = 0			 # On arrête la boucle
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer = 0
	pygame.quit()						 # on ferme la fenêtre
	return


###########################################################
# PARTIE 2 : Fonctions bloquantes d'attente d'un clic de souris
###########################################################

def wait_clic():
	"""
	Fonction blaquante. Attente d'un clic de souris.
	Sortie : tuple des coordonnées du point cliqué
	"""
	ev = pygame.event.wait()
	while(ev.type != MOUSEBUTTONDOWN):
		ev = pygame.event.wait()
	return ev.pos

def wait_left_clic():
	"""
	Fonction blaquante. Attente d'un clic gauche de souris.
	Sortie : tuple des coordonnées du point cliqué
	"""
	while 1:
		ev = pygame.event.wait()
		if (ev.type == MOUSEBUTTONDOWN and ev.button == 1):
			return ev.pos

def wait_center_clic():
	"""
	Fonction blaquante. Attente d'un clic central de souris.
	Sortie : tuple des coordonnées du point cliqué
	"""
	while 1:
		ev = pygame.event.wait()
		if (ev.type == MOUSEBUTTONDOWN and ev.button == 2):
			return ev.pos

def wait_right_clic():
	"""
	Fonction blaquante. Attente d'un clic droit de souris.
	Sortie : tuple des coordonnées du point cliqué
	"""
	while 1:
		ev = pygame.event.wait()
		if (ev.type == MOUSEBUTTONDOWN and ev.button == 3):
			return ev.pos


###########################################################
# PARTIE 3 : Fonctions non bloquantes de la souris
###########################################################

def device_mouse_off() :
	"""
	Supprime le curseur de la souris dans la fenêtre graphique
	"""
	pygame.mouse.set_visible(0)


def device_mouse_on() :
	"""
	Affiche le curseur de la souris dans la fenêtre graphique
	"""
	pygame.mouse.set_visible(1)


def get_mouse_original() :
	"""
	Renvoie la position de la souris
	Instruction non bloquante
	"""
	mouse = pygame.mouse.get_pos()
	return Point(mouse[0],mouse[1])

def get_mouse() :
	"""
	Renvoie la position de la souris
	Version simplifiée de `get_mouse_original()`
	Instruction non bloquante
	"""
	return pygame.mouse.get_pos()


def is_mouse_pressed_left() :
	"""
	Renvoie True si le bouton gauche de la souris est cliqué
	Instruction non bloquante
	"""
	pygame.event.get()
	return pygame.mouse.get_pressed()[0]


def is_mouse_pressed_right() :
	"""
	Renvoie True si le bouton droit de la souris est cliqué
	Instruction non bloquante
	"""
	pygame.event.get()
	return pygame.mouse.get_pressed()[2]

def is_mouse_focused():
	"""
	Renvoie True si la fenêtre graphique est sélectionnée
	"""
	return pygame.mouse.get_focused()

###########################################################
# PARTIE 4 : Gestion du clavier
###########################################################

def wait_key():
	"""
	Attend que l'on tape sur une touche du clavier (y compris
	une combinaison de touches) et renvoie le caractère correspondant.
	Instruction bloquante
	"""
	if PYGAME_SDL_AFFICHAGE == 1:
		affiche_all()

	pygame.event.clear()

	caractere = ""
	while caractere == "":
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				caractere = event.dict['unicode']
				if caractere != "":
					return caractere


def wait_space_letter():
	"""
	Attend que l'on presse une touche du clavier.
	Si la touche est une lettre, renvoie la lettre correspondante en majuscule.
	Si la touche est la barre d'espace, renvoie la chaîne de caractère espace.
	Sinon, renvoie une chaîne vide.
	Instruction bloquante.
	"""
	key = wait_key()
	if 96 < key < 123:
		return chr(key - 32)
	if key == 32:
		return " "
	return ""


def wait_arrow():
	"""
	Attend que l'on presse une touche du clavier.
	Renvoie "up", "down", "left" ou  "right" suivant que l'on a
	tapé sur la flèche du haut, du bas, de gauche ou de droite.
	Renvoie une chaîne vide sinon.
	Instruction bloquante.
	"""
	if PYGAME_SDL_AFFICHAGE == 1:
		affiche_all()

	pygame.event.clear()

	while 1:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_UP:
					return "up"
				elif event.key == K_DOWN:
					return "down"
				elif event.key == K_LEFT:
					return "left"
				elif event.key == K_RIGHT:
					return "right"


#----------------------------------------------------------#
#-----------------						 ----------------#
#				   2. AFFICHAGE DE TEXTE				  #
#-----------------						 ----------------#
#----------------------------------------------------------#

def aff_pol(fenetre, texte, taille, p_x, p_y, coul, text_bold=False, text_italic=False):
	"""
	Affiche une chaîne de caractère en police Verdana
	Paramètres d'entrées :
		- fenetre : fenetre d'affichage du texte
		- texte : chaine de caractère à afficher
		- taille : taille de la chaine de caractère
		- p_x et p_y : coordonnées du point en haut à gauche
		- coul : couleur de la chaine de caractère à afficher
		- text_bold : affichage en gras. Argument optionnel (False par défaut)
		- text_italic : affichage en italique. Argument optionnel (False par défaut)
	"""

	font = pygame.font.SysFont("vernada", taille, bold=text_bold, italic=text_italic)
	text = font.render(texte, 1, coul)
	fenetre.blit(text, (p_x, p_y))


#----------------------------------------------------------#
#-----------------						 ----------------#
#					3. GESTION D'IMAGES				   #
#-----------------						 ----------------#
#----------------------------------------------------------#

def affiche_image(fenetre, nom_img, p_x, p_y):
	"""
	Affiche une image.
	Paramètres d'entrées :
		- fenetre : fenetre d'affichage de l'image
		- nom_img : chaine de caractère donnant le nom du fichier image.
		- p_x et p_y : coordonnées du point en haut à gauche
	Renvoie l'image sous forme de surface pygame.
	"""
	fond = pygame.image.load(nom_img).convert()
	fenetre.blit(fond, (p_x, p_y))
	return fond

def affiche_image_transp(fenetre, nom_img, p_x, p_y):
	"""
	Affiche une image à transparence.
	Paramètres d'entrées :
		- fenetre : fenetre d'affichage de l'image
		- nom_img : chaine de caractère donnant le nom du fichier image.
		- p_x et p_y : coordonnées du point en haut à gauche
	Renvoie l'image sous forme de surface pygame.
	"""
	fond = pygame.image.load(nom_img).convert_alpha()
	fenetre.blit(fond, (p_x, p_y))
	return fond

# A voir
def transfer_image(nom_img):
	"""
	Renvoie la surface pygame correspondant à l'image F (fichier).
	Attention, l'image n'est pas affichée à l'écran ; cette fonction est
	utile pour obtenir les dimensions de l'image, la redimensionner ou la
	sauvegarder
	"""
	return pygame.image.load(nom_img)

# A voir
def resize_image(I,W,H):
	"""
	I est une surface pygame.
	W et H sont des entiers supérieurs à 1.
	Permet de redimensionner I avec la largeur W et la hauteur H.
	Renvoie la nouvelle surface pygame.
	"""
	return pygame.transform.scale(I,(W,H))


#----------------------------------------------------------#
#-----------------						 ----------------#
#			  4. GESTION DES SONS ET MUSIQUES			 #
#-----------------						 ----------------#
#----------------------------------------------------------#

############################################################
# PARTIE 4.1 : SONS
############################################################

def play_sound(mon_son):
	"""
	F est une chaîne de caractères contenant le nom du fichier son.
	Joue le son F.
	"""
	pygame.mixer.Sound(mon_son).play()


def stop_sound(mon_son):
	"""
	F est une chaîne de caractères contenant le nom du fichier son.
	Arrête le son F.
	"""
	pygame.mixer.Sound(mon_son).stop()


def set_volume_sound(mon_son, vol):
	"""
	F est une chaîne de caractères contenant le nom du fichier son.
	v est un flottant entre 0.0 et 1.0.
	Permet de régler le volume du son F.
	"""
	pygame.mixer.Sound(mon_son).set_volume(vol)


def get_volume_sound(mon_son):
	"""
	F est une chaîne de caractères.
	Renvoie le volume du son F.
	"""
	return pygame.mixer.Sound(mon_son).get_volume()


############################################################
# PARTIE 4.2 : MUSIQUES
############################################################

def load_music(ma_music):
	"""
	F est une chaîne de caractères contenant le nom du fichier audio.
	Charge la musique F mais ne la joue pas.
	Si une musique était déjà chargée, cela la stoppe si elle etait jouée.
	Utiliser de préférence des .wav
	"""
	pygame.mixer.music.load(ma_music)


def play_music(loop=0):
	"""
	Lance la musique. Si la musique était déjà jouée, elle reprend au début
	L'argument optionnel loop prend les valeurs 0 ou 1.
	Si loop vaut 1, alors la musique est jouée en boucle.
	"""
	if loop == 1:
		pygame.mixer.music.play(loops = -1)
	else:
		pygame.mixer.music.play()


def restart_music():
	"""
	Relance la musique à partir du début.
	"""
	pygame.mixer.music.rewind()


def stop_music():
	"""
	Arrête la musique.
	"""
	pygame.mixer.music.stop()


def pause_music():
	"""
	Met la musique en pause.
	"""
	pygame.mixer.music.pause()


def unpause_music():
	"""
	Reprend la musique
	"""
	pygame.mixer.music.unpause()


def set_volume_music(vol):
	"""
	v est un flottant entre 0.0 et 1.0.
	Permet de régler le volume de la musique.
	"""
	pygame.mixer.music.set_volume(vol)


def get_volume_music() :
	"""
	Renvoie le volume de la musique.
	"""
	return pygame.mixer.music.get_volume()


def get_busy_music() :
	"""
	Renvoie 1 si une musique est jouée et 0 sinon.
	"""
	return pygame.mixer.music.get_busy()


#----------------------------------------------------------#
#-----------------						 ----------------#
#					5 GESTION DU TEMPS					#
#-----------------						 ----------------#
#----------------------------------------------------------#

def attendre(millisecondes) :
	"""
	Attend le nombre de millisecondes passé en argument
	"""
	if PYGAME_SDL_AFFICHAGE == 1 :
		affiche_all()

	pygame.time.delay(millisecondes)


def chrono_start() :
	"""
	Démarre un chronomètre
	"""
	global CHRONO
	CHRONO = pygame.time.get_ticks()


def chrono_val() :
	"""
	Affiche le temps écoulé en millisecondes depuis le lancement du chronomètre
	"""
	global CHRONO
	return pygame.time.get_ticks()-CHRONO


#----------------------------------------------------------#
#-----------------						 ----------------#
#				   5 VARIABLES COULEURS				   #
#-----------------						 ----------------#
#----------------------------------------------------------#

from colors import *