import math
from graphique import *
from globals import *

BACKGROUND_COLOR = hex_white; DISPLAY_COLOR = hex_black
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

NaN : float = float('nan')

def draw_point(surface, pos, color=DISPLAY_COLOR) -> None:
	surface.set_at(pos, color)

def draw_square(surface, size, center, border=0, border_color=DISPLAY_COLOR) -> None:
	pygame.draw.polygon(
		surface,
		border_color,
		(
			[center[0] - size//2, center[1] - size//2],
			[center[0] + size//2, center[1] - size//2],
			[center[0] + size//2, center[1] + size//2],
			[center[0] - size//2, center[1] + size//2],
		),
		border
	)


def draw_triangle(surface, p1, p2, p3, border=1, border_color=DISPLAY_COLOR) -> None:
	pygame.draw.polygon(
		surface,
		border_color,
		(p1, p2, p3),
		border
	)

def reset_window(flip : bool = False) -> None:
	window.fill(BACKGROUND_COLOR, rect=None, special_flags=0)
	if flip:
		pygame.display.flip()
reset_window(True)

def calc_dist_v(x1, x2):
	return abs(x1-x2)

def calc_dist_p(p1, p2) -> tuple[int, int]:
	return (
		abs(p1[0] - p2[0]),
		abs(p1[1] - p2[1])
	)

def is_in_rect(point, rect : pygame.Rect, account_corners : bool = False) -> bool:
	corners = False
	if account_corners:
		corners = point[0] == rect.x or point[0] == rect.x + rect.w or point[1] == rect.y or point[1] == rect.y + rect.h
	return (rect.x < point[0] < rect.x + rect.w and rect.y < point[1] < rect.y + rect.h) or corners

def is_NaN_point(point) -> bool:
	"""
	If the points has all coordonates at NaN
	"""
	return math.isnan(point[0]) and math.isnan(point[1])

def hex_to_rgb(color_hex : int) -> tuple[int, int, int]:
	"""
	Return the rgb version of `color_hex` as a tuple (1st elem is red, 2nd is green, 3rd is blue)
	"""
	return (
		max(min((color_hex & 0xFF0000) >> 4*4, 255), 0),
		max(min((color_hex & 0x00FF00) >> 2*4, 255), 0),
		max(min(color_hex & 0x0000FF		 , 255), 0)
	)
assert(hex_to_rgb(hex_black)	== rgb_black)
assert(hex_to_rgb(hex_white)	== rgb_white)
assert(hex_to_rgb(hex_red)		== rgb_red	)
assert(hex_to_rgb(hex_green)	== rgb_green)
assert(hex_to_rgb(hex_blue)		== rgb_blue	)


def rgb_to_hex(color_rgb) -> int:
	return (
			(max(0, min(255, color_rgb[0])) << 4*4)
		+	(max(0, min(255, color_rgb[1])) << 2*4)
		+	 max(0, min(255, color_rgb[2]))
	)
assert(rgb_to_hex(rgb_black)	== hex_black)
assert(rgb_to_hex(rgb_white)	== hex_white)
assert(rgb_to_hex(rgb_red)		== hex_red	)
assert(rgb_to_hex(rgb_green)	== hex_green)
assert(rgb_to_hex(rgb_blue)		== hex_blue	)


def darken_color(color_hex : int, how_much : float) -> int:
	"""
	Darken `color_hex` by `how_much*100`%.
	"""
	assert(0 <= how_much <= 1), "Parameter `how_much` have to be in [0, 1]"
	color_rgb = hex_to_rgb(color_hex)

	res = []
	for col_val in color_rgb:
		res.append(round(col_val * how_much))
	return rgb_to_hex(res)