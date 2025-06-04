# Créé par adekambin, le 28/05/2025 en Python 3.7
from os.path	import isfile
from sys		import argv

from header import *
from button import *

PLUS_IMAGE : Surface = pygame.image.load("img/plus.png")

def change_brush_size(how_much : int) -> None:
	global brush_size
	brush_size += how_much
	brush_size = max(1, brush_size)

def toggle_eraser() -> None:
	global is_eraser
	is_eraser = not is_eraser

def change_color_to(color_list_index : int, foreground : bool = True) -> None:
	assert 0 <= color_list_index < COLOR_LIST_LEN
	
	global foreground_color
	global background_color
	if foreground:
		foreground_color = COLOR_LIST[color_list_index]
	else:
		background_color = COLOR_LIST[color_list_index]

def quit(exit_code: int =0):
	pygame.quit()
	exit(exit_code)

def can_draw_at(point) -> bool:
	for zone in MENU_ZONES:
		if is_in_rect(point, zone, True):
			return False
	return True

def draw_menus():
	for menu in MENU_ZONES:
		pygame.draw.rect(menu_surf, MENU_COLOR, menu)
	for butt in Button.butt_list:
		butt.draw()

def draw_brush(pos, surface : Surface = drawing_surf, max_size : int = -1, foreground : bool = True) -> None:
	global foreground_color
	global background_color

	color = foreground_color if foreground else background_color

	if max_size < 0:	# no limit
		pygame.draw.circle(surface, color, pos, brush_size/2, 0)
		return
	if brush_size < 2:
		draw_point(surface, pos, color)
		return

	pygame.draw.circle(surface, color, pos, min(brush_size, max_size)/2, 0)

def draw_brush_preview() -> None:
	global brush_size

	brush_fore_preview_coord = (
		Button.location_on_horizontal_grid(BUTTON_FIRST_DIST_FROM_LEFT + 11, Button.DEFAULT_SIZE, 4),
		15
	)
	brush_back_preview_coord = (
		Button.location_on_horizontal_grid(BUTTON_FIRST_DIST_FROM_LEFT + 11, Button.DEFAULT_SIZE, 5),
		15
	)
	draw_brush((
		brush_fore_preview_coord[0],
		brush_fore_preview_coord[1]
	), menu_surf, 25, foreground=True)
	draw_brush((
		brush_back_preview_coord[0],
		brush_back_preview_coord[1]
	), menu_surf, 25, foreground=False)

	if brush_size > 25:
		menu_surf.blit(pygame.transform.scale(PLUS_IMAGE, (14, 14)), (brush_fore_preview_coord[0] - 7, brush_fore_preview_coord[1] - 7))
		menu_surf.blit(pygame.transform.scale(PLUS_IMAGE, (14, 14)), (brush_back_preview_coord[0] - 7, brush_back_preview_coord[1] - 7))

def save_drawing() -> None:
	pygame.image.save(drawing_surf, "my_drawing.png")

BUTTON_DIST_FROM_TOP		: int = 3	# Distance from the top of the screen for buttons
BUTTON_FIRST_DIST_FROM_LEFT	: int = 5	# Distance from the left side of the screen for the first button

SAVE_BUTTON : Button = Button(
	BUTTON_FIRST_DIST_FROM_LEFT,
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	save_drawing,
	icon="img/save.png"
)

LOWER_SIZE_BUTTON : Button = Button(
	Button.location_on_horizontal_grid(BUTTON_FIRST_DIST_FROM_LEFT, Button.DEFAULT_SIZE, 2),
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	(lambda: change_brush_size(-5)),
	icon="img/lower_size.png"
)
INCREASE_SIZE_BUTTON : Button = Button(
	Button.location_on_horizontal_grid(BUTTON_FIRST_DIST_FROM_LEFT, Button.DEFAULT_SIZE, 3),
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	(lambda: change_brush_size(5)),
	icon="img/increase_size.png"
)

ERASER_BUTTON : Button = Button(
	WIN_WIDTH//2 - Button.DEFAULT_SIZE//2,		#centering the button
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	toggle_eraser,
	icon="img/eraser.png",
	enable_toggle=True
)

RESET_BUTTON : Button = Button(
	Button.location_on_horizontal_grid(WIN_WIDTH//2 - Button.DEFAULT_SIZE//2, Button.DEFAULT_SIZE, 4),		#centering the button
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	(lambda: drawing_surf.fill(hex_white)),
	icon="img/reset.png"
)
FILL_BUTTON : Button = Button(
	Button.location_on_horizontal_grid(WIN_WIDTH//2 - Button.DEFAULT_SIZE//2, Button.DEFAULT_SIZE, 5),		#centering the button
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	(lambda: drawing_surf.fill(background_color)),
	icon="img/fill.png"
)

COLOR_BUTTONS : list[Button] = []

COLOR_BUTT_DIST_FROM_TOP: int = 3
COLOR_BUTT_MARGIN		: int = 4
COLOR_BUTT_CELL_OFFSET	: int = 32
# Generating color buttons
IS_COLOR_LIST_LEN_EVEN : bool = COLOR_LIST_LEN%2 == 0
for i in range(COLOR_LIST_LEN):	# I miss C-style for loops
	# Dynamic lambda generation, without `eval()` only the lastest value of `i` is read (in this case `COLOR_LIST_LEN-1`)
	change_color_left_lambda  = eval(f"lambda: change_color_to({i}, True)")
	change_color_right_lambda = eval(f"lambda: change_color_to({i}, False)")
	
	# 
	if i < COLOR_LIST_LEN/2:
		# First row
		COLOR_BUTTONS.append(
			Button(
				Button.location_on_horizontal_grid(
					BUTTON_FIRST_DIST_FROM_LEFT,
					Button.DEFAULT_SIZE//2,
					COLOR_BUTT_CELL_OFFSET + i,
					COLOR_BUTT_MARGIN
				),
				COLOR_BUTT_DIST_FROM_TOP,
				Button.DEFAULT_SIZE//2,
				action=change_color_left_lambda,
				alt_action=change_color_right_lambda,
				color_overrride=COLOR_LIST[i]
			)
		)
		continue

	# Second row
	COLOR_BUTTONS.append(
		Button(
			Button.location_on_horizontal_grid(
				BUTTON_FIRST_DIST_FROM_LEFT,
				Button.DEFAULT_SIZE//2,
				COLOR_BUTT_CELL_OFFSET + i - COLOR_LIST_LEN//2 - (0 if IS_COLOR_LIST_LEN_EVEN else 1),
				COLOR_BUTT_MARGIN
			),
			COLOR_BUTT_DIST_FROM_TOP + Button.DEFAULT_SIZE//2 + COLOR_BUTT_MARGIN,
			Button.DEFAULT_SIZE//2,
			action=change_color_left_lambda,
			alt_action=change_color_right_lambda,
			color_overrride=COLOR_LIST[i]
		)
	)

def draw_image_or_reset() -> None:
	# Check for file in cmd line input
	if len(argv) <= 1 or not isfile(argv[1]):
		drawing_surf.fill(hex_white)
		return
	
	try:
		img = pygame.image.load(argv[1])
		drawing_surf.blit(img, (0, 0))
	except pygame.error:
		extention = argv[1].split('.', 1)
		extention = ('.' + extention[1]) if len(extention) > 1 else extention[0]
		print(f"\x1B[31mError: The image type `{extention}` is not handled by pygame.\033[39m")
		
		if not pygame.image.get_extended():
			print("\x1B[94mIt seems that pygame does not support any other format that BMP.\033[39m")
			print("\x1B[94mTry reinstalling it.\033[39m")

def draw(mouse_pos : tuple[int, int], prev_mouse_pos : tuple[int, int] | tuple[float, float], foreground : bool) -> None:
	global foreground_color
	global background_color
	global brush_size

	color :int = foreground_color if foreground else background_color

	shifted_mouse_pos = (
		mouse_pos[0],
		mouse_pos[1] - DRAWING_OFFSET
	)
	shifted_prev_mouse_pos = (
		prev_mouse_pos[0],
		prev_mouse_pos[1] - DRAWING_OFFSET
	)
	if is_NaN_point(prev_mouse_pos):
		draw_brush(shifted_mouse_pos, foreground=foreground)
		return
	
	# Draw circle so the start and end positions are round
	# Draw a line bc in a lot of cases, the mouse moves faster than 1 pixel per frame
	if is_eraser:
		color = BACKGROUND_COLOR
	
	draw_brush(shifted_prev_mouse_pos,	foreground=foreground)
	draw_brush(shifted_mouse_pos,		foreground=foreground)
	
	pygame.draw.line(drawing_surf, color, shifted_prev_mouse_pos, shifted_mouse_pos, brush_size)





def __main__() -> None:
	global brush_size
	global is_eraser

	draw_image_or_reset()



	prev_mouse_pos = (NaN, NaN)
	was_clicking : bool = False
	is_left_clicking : bool = False
	is_right_clicking : bool = False
	while True:
		menu_surf.unlock()
		window.blits((					# Draw `menu_surf` and `drawing_surf` on screen
			(menu_surf, (0, 0)),
			(drawing_surf, (0, DRAWING_OFFSET)),
		))
		pygame.display.flip()
		draw_menus()
		draw_brush_preview()
		menu_surf.lock()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		
		is_left_clicking :bool = pygame.mouse.get_pressed()[0]
		is_right_clicking : bool = pygame.mouse.get_pressed()[2]


		mouse_pos = get_mouse()
		if is_left_clicking and can_draw_at(mouse_pos):
			draw(mouse_pos, prev_mouse_pos, foreground=True)
		elif is_right_clicking and can_draw_at(mouse_pos):
			draw(mouse_pos, prev_mouse_pos, foreground=False)
		else:
			Button.check_new_click(mouse_pos, pygame.mouse.get_pressed(), was_clicking)


		Button.update_button_presses(is_left_clicking, mouse_pos, is_left_clicking)
		prev_mouse_pos = mouse_pos
		was_clicking = is_left_clicking

if __name__ == "__main__":
	__main__()