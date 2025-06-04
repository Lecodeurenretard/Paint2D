# Créé par adekambin, le 28/05/2025 en Python 3.7
# All global variables
from pygame import Rect, Surface
from colorlib import *
from graphique import *

# source: https://stackoverflow.com/questions/34287938/how-to-distinguish-left-click-right-click-mouse-clicks-in-pygame
PYGAME_LEFT_CLICK	= 1
PYGAME_MIDDLE_CLICK	= 2
PYGAME_RIGHT_CLICK	= 3

WIN_HEIGHT : int = 600; WIN_WIDTH : int = 600; WIN_MIN : int = min(WIN_WIDTH, WIN_HEIGHT)
MENU_COLOR = 0x824E4E
MENU_ZONES = (
	Rect((0, 0), (WIN_WIDTH, 30)),
)

menu_surf = Surface(
	(MENU_ZONES[0].w, MENU_ZONES[0].h)	# change accordingly if adding more menus
)

drawing_surf = Surface(
	(WIN_WIDTH, WIN_HEIGHT - MENU_ZONES[0].h)	# change accordingly if adding more menus
)
DRAWING_OFFSET : int = MENU_ZONES[0].h

COLOR_LIST : tuple[int, ...] = (
	hex_black,
	hex_sienna,
	rgb_to_hex(rgb_brown),
	hex_red,
	hex_tomato,
	hex_orange,
	hex_yellow,
	hex_lime,
	hex_forestgreen,
	hex_green,
	hex_olivedrab,
	hex_darkgreen,
	hex_purple,
	hex_blue,
	rgb_to_hex(rgb_darkblue),
	hex_teal,
	hex_turquoise,
	hex_tan,
	hex_hotpink,
	hex_magenta,
)
COLOR_LIST_LEN : int = len(COLOR_LIST)

foreground_color	: int = hex_black
background_color	: int = hex_tan

brush_size 		: int = 1
is_eraser		: bool = False