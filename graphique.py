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
pygame.display.set_caption("Lycée Louis Bascan Rambouillet						  Formation N.S.I.")


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

###########################################################
# variables couleur 18 principales
###########################################################
rgb_vert = (0, 255, 0)
rgb_rouge = (255, 0, 0)
rgb_bleu = (0, 0, 255)
rgb_cyan = (0, 255, 255)
rgb_blanc = (255, 255, 255)
rgb_jaune = (255, 255, 0)
rgb_orange = (255, 165, 0)
rgb_noir = (0, 0, 0)
rgb_argent = (192, 192, 192)
rgb_bleumarine = (0, 0, 128)
rgb_citronvert = (0, 255, 0)
rgb_magenta = (255, 0, 255)
rgb_gris = (128, 128, 128)
rgb_marron = (128, 0, 0)
rgb_sarcelle = (0, 128, 128)
rgb_vertclair = (0, 128, 0)
rgb_vertolive = (128, 128, 0)
rgb_violet = (128, 0, 128)

###########################################################
# variables couleur 140 en Anglais
###########################################################
rgb_aliceblue = (240, 248, 255)
rgb_antiquewhite = (250, 235, 215)
rgb_aqua = (0, 255, 255)
rgb_aquamarine = (127, 255, 212)
rgb_azure = (240, 255, 255)
rgb_beige = (245, 245, 220)
rgb_bisque = (255, 228, 196)
rgb_black = (0, 0, 0); hex_black = 0x000000
rgb_blanchedalmond = (255, 235, 205)
rgb_blue = (0, 0, 255); hex_blue = 0x0000FF
rgb_blueviolet = (138, 43, 226)
rgb_brown = (165, 42, 42)
rgb_burlywood = (222, 184, 135)
rgb_cadetblue = (95, 158, 160)
rgb_chartreuse = (127, 255, 0)
rgb_chocolate = (210, 105, 30)
rgb_coral = (255, 127, 80)
rgb_cornflowerblue = (100, 149, 237)
rgb_cornsilk = (255, 248, 220)
rgb_crimson = (220, 20, 60)
rgb_darkblue = (0, 0, 139)
rgb_darkcyan = (0, 139, 139)
rgb_darkgoldenrod = (184, 134, 11)
rgb_darkgray = (169, 169, 169)
hex_darkgreen = 0x006400
hex_darkkhaki = 0xBDB76B
hex_darkmagenta = 0x8B008B
hex_darkolivegreen = 0x556B2F
hex_darkorange = 0xFF8C00
hex_darkorchid = 0x9932CC
hex_darkred = 0x8B0000
hex_darksalmon = 0xE9967A
hex_darkseagreen = 0x8FBC8F
hex_darkslateblue = 0x483D8B
hex_darkslategray = 0x2F4F4F
hex_darkturquoise = 0x00CED1
hex_darkviolet = 0x9400D3
hex_deeppink = 0xFF1493
hex_deepskyblue = 0x00BFFF
hex_dimgray = 0x696969
hex_dodgerblue = 0x1E90FF
hex_firebrick = 0xB22222
hex_floralwhite = 0xFFFAF0
hex_forestgreen = 0x228B22
hex_fuchsia = 0xFF00FF; rgb_fuchsia = (255, 0, 255)
hex_gainsboro = 0xDCDCDC
hex_ghostwhite = 0xF8F8FF
hex_gold = 0xFFD700
hex_goldenrod = 0xDAA520
hex_gray = 0x808080
hex_green = 0x008000; rgb_green = (0, 128, 0)
hex_greenyellow = 0xADFF2F
hex_honeydew = 0xF0FFF0
hex_hotpink = 0xFF69B4
hex_indianred = 0xCD5C5C
hex_indigo = 0x4B0082
hex_ivory = 0xFFFFF0
hex_khaki = 0xF0E68C
hex_lavender = 0xE6E6FA
hex_lavenderblush = 0xFFF0F5
hex_lawngreen = 0x7CFC00
hex_lemonchiffon = 0xFFFACD
hex_lightblue = 0xADD8E6
hex_lightcoral = 0xF08080
hex_lightcyan = 0xE0FFFF
hex_lightgoldenrodyellow = 0xFAFAD2
hex_lightgreen = 0x90EE90
hex_lightgrey = 0xD3D3D3
hex_lightpink = 0xFFB6C1
hex_lightsalmon = 0xFFA07A
hex_lightseagreen = 0x20B2AA
hex_lightskyblue = 0x87CEFA
hex_lightslategray = 0x778899
hex_lightsteelblue = 0xB0C4DE
hex_lightyellow = 0xFFFFE0
hex_lime = 0x00FF00; rgb_lime = (0, 255, 0)
hex_limegreen = 0x32CD32
hex_linen = 0xFAF0E6
hex_magenta = 0xFF00FF
hex_maroon = 0x800000
hex_mediumaquamarine = 0x66CDAA
hex_mediumblue = 0x0000CD
hex_mediumorchid = 0xBA55D3
hex_mediumpurple = 0x9370DB
hex_mediumseagreen = 0x3CB371
hex_mediumslateblue = 0x7B68EE
hex_mediumspringgreen = 0x00FA9A
hex_mediumturquoise = 0x48D1CC
hex_mediumvioletred = 0xC71585
hex_midnightblue = 0x191970
hex_mintcream = 0xF5FFFA
hex_mistyrose = 0xFFE4E1
hex_moccasin = 0xFFE4B5
hex_navajowhite = 0xFFDEAD
hex_navy = 0x000080
hex_oldlace = 0xFDF5E6
hex_olive = 0x808000
hex_olivedrab = 0x6B8E23
hex_orange = 0xFFA500
hex_orangered = 0xFF4500
hex_orchid = 0xDA70D6
hex_palegoldenrod = 0xEEE8AA
hex_palegreen = 0x98FB98
hex_paleturquoise= 0xAFEEEE
hex_palevioletred = 0xDB7093
hex_papayawhip = 0xFFEFD5
hex_peachpuff = 0xFFDAB9
hex_peru = 0xCD853F
hex_pink = 0xFFC0CB
hex_plum = 0xDDA0DD
hex_powderblue = 0xB0E0E6
hex_purple = 0x800080
hex_red = 0xFF0000; rgb_red = (255, 0, 0)
hex_rosybrown = 0xBC8F8F
hex_royalblue = 0x4169E1
hex_saddlebrown = 0x8B4513
hex_salmon = 0xFA8072
hex_sandybrown = 0xF4A460
hex_seagreen = 0x2E8B57
hex_seashell = 0xFFF5EE
hex_sienna = 0xA0522D
hex_silver = 0xC0C0C0
hex_skyblue = 0x87CEEB
hex_slateblue = 0x6A5ACD
hex_slategray = 0x708090
hex_snow = 0xFFFAFA
hex_springgreen = 0x00FF7F
hex_steelblue = 0x4682B4
hex_tan = 0xD2B48C
hex_teal = 0x008080
hex_thistle = 0xD8BFD8
hex_tomato = 0xFF6347
hex_turquoise = 0x40E0D0
hex_violetlight = 0xEE82EE
hex_wheat = 0xF5DEB3
hex_white = 0xFFFFFF; rgb_white = (255, 255, 255)
hex_whitesmoke = 0xF5F5F5
hex_yellow = 0xFFFF00; rgb_yellow = (255, 255, 255)
hex_yellowgreen = 0x9ACD32