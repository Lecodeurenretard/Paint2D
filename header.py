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