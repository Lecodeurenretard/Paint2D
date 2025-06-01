# Créé par adekambin, le 28/05/2025 en Python 3.7
# All global variables
from pygame import Rect, Surface
from colorlib import *
from graphique import *

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
DRAWING_OFFSET = MENU_ZONES[0].h

COLOR_LIST : tuple[int, ...] = (
	hex_black,
	hex_sienna,
	rgb_to_hex(rgb_brown),
	hex_red,
	hex_tomato,
	hex_orange,
	hex_yellow,
	hex_magenta,
	hex_tan,
	hex_hotpink,
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
)
COLOR_LIST_LEN : int = len(COLOR_LIST)

current_color	: int = 0x000000	# black
brush_size 		: int = 1
is_eraser		: bool = False