from colors import *

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