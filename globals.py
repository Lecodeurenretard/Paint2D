# Créé par adekambin, le 28/05/2025 en Python 3.7
# All global variables
from pygame import Rect, Surface

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


current_color	: int = 0x000000   # black
brush_size 		: int = 1
is_eraser		: bool = False