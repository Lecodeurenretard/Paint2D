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

def change_color_to(color_list_index : int) -> None:
	assert 0 <= color_list_index < COLOR_LIST_LEN
	global current_color
	current_color = COLOR_LIST[color_list_index]

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

def draw_brush(pos, surface : Surface = drawing_surf, max_size : int = -1) -> None:
	if max_size < 0:	# no limit
		pygame.draw.circle(surface, current_color, pos, brush_size/2, 0)
		return
	if brush_size < 2:
		draw_point(surface, pos, current_color)
		return

	pygame.draw.circle(surface, current_color, pos, min(brush_size, max_size)/2, 0)

def save_drawing() -> None:
	pygame.image.save(drawing_surf, "my_drawing.png")

BUTTON_DIST_FROM_TOP		: int = 3	# Distance from the top of the screen for buttons
BUTTON_FIRST_DIST_FROM_LEFT	: int = 5	# Distance from the left side of the screen for the first button

SAVE_BUTTON : Button = Button(
	BUTTON_FIRST_DIST_FROM_LEFT,
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	save_drawing,
	"img/save.png"
)

LOWER_SIZE_BUTTON : Button = Button(
	Button.location_on_horizontal_grid(BUTTON_FIRST_DIST_FROM_LEFT, Button.DEFAULT_SIZE, 2),
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	(lambda: change_brush_size(-5)),
	"img/lower_size.png"
)
INCREASE_SIZE_BUTTON : Button = Button(
	Button.location_on_horizontal_grid(BUTTON_FIRST_DIST_FROM_LEFT, Button.DEFAULT_SIZE, 3),
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	(lambda: change_brush_size(5)),
	"img/increase_size.png"
)

ERASER_BUTTON : Button = Button(
	WIN_WIDTH//2 - Button.DEFAULT_SIZE//2,		#centering the button
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	toggle_eraser,
	"img/eraser.png",
	enable_toggle=True
)

RESET_BUTTON : Button = Button(
	Button.location_on_horizontal_grid(WIN_WIDTH//2 - Button.DEFAULT_SIZE//2, Button.DEFAULT_SIZE, 4),		#centering the button
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	(lambda: drawing_surf.fill(hex_white)),
	"img/reset.png"
)
FILL_BUTTON : Button = Button(
	Button.location_on_horizontal_grid(WIN_WIDTH//2 - Button.DEFAULT_SIZE//2, Button.DEFAULT_SIZE, 5),		#centering the button
	BUTTON_DIST_FROM_TOP,
	Button.DEFAULT_SIZE,
	(lambda: drawing_surf.fill(current_color)),
	"img/fill.png"
)

COLOR_BUTTONS : list[Button] = []

COLOR_BUTT_DIST_FROM_TOP: int = 3
COLOR_BUTT_MARGIN		: int = 4
COLOR_BUTT_CELL_OFFSET	: int = 32
# Generating color buttons
IS_COLOR_LIST_LEN_EVEN : bool = COLOR_LIST_LEN%2 == 0
for i in range(COLOR_LIST_LEN):	# I miss C-style for loops
	# Dynamic lambda generation, without `eval()` only the lastest value of `i` is read (in this case `COLOR_LIST_LEN-1`)
	change_color_lambda = eval(f"lambda: change_color_to({i})")
	
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
				change_color_lambda,
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
			change_color_lambda,
			color_overrride=COLOR_LIST[i]
		)
	)










def __main__() -> None:
	global current_color
	global brush_size
	global is_eraser

	# Check for file in cmd line input
	if len(argv) > 1 and isfile(argv[1]):
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
	else:
		drawing_surf.fill(hex_white)









	prev_mouse_pos = (NaN, NaN)
	was_clicking : bool = False
	is_clicking : bool = False
	while True:
		menu_surf.unlock()
		window.blits((					# Draw `menu_surf` and `drawing_surf` on screen
			(menu_surf, (0, 0)),
			(drawing_surf, (0, DRAWING_OFFSET)),
		))
		pygame.display.flip()
		draw_menus()

		brush_coord = (
			Button.location_on_horizontal_grid(BUTTON_FIRST_DIST_FROM_LEFT + 11, Button.DEFAULT_SIZE, 4),
			15
		)
		draw_brush((			# Draw the brush preview
			brush_coord[0],
			brush_coord[1]
		), menu_surf, 25)
		if brush_size > 25:
			# Display a plus sign
			menu_surf.blit(pygame.transform.scale(PLUS_IMAGE, (14, 14)), (brush_coord[0] - 7, brush_coord[1] - 7))
		menu_surf.lock()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				is_clicking = True
			if event.type == pygame.MOUSEBUTTONUP:
				is_clicking = False

		mouse_pos = get_mouse()
		if is_clicking:
			shifted_mouse_pos = (
				mouse_pos[0],
				mouse_pos[1] - DRAWING_OFFSET
			)
			shifted_prev_mouse_pos = (
				prev_mouse_pos[0],
				prev_mouse_pos[1] - DRAWING_OFFSET
			)
			if can_draw_at(mouse_pos):
				if is_NaN_point(prev_mouse_pos):
					draw_brush(shifted_mouse_pos)
				else:
					# Draw circle so the start and end positions are round
					# Draw a line bc in a lot of cases, the mouse moves faster than 1 pixel per frame
					color_remember = current_color
					if is_eraser:
						current_color = BACKGROUND_COLOR

					draw_brush(shifted_prev_mouse_pos)
					pygame.draw.line(drawing_surf, current_color, shifted_prev_mouse_pos, shifted_mouse_pos, globals()["brush_size"])
					draw_brush(shifted_mouse_pos)

					current_color = color_remember


			for butt in Button.butt_list:
				if not was_clicking:
					butt.handle_click(mouse_pos)


		Button.update_button_presses(is_clicking, mouse_pos)
		prev_mouse_pos = mouse_pos
		was_clicking = is_clicking

if __name__ == "__main__":
	__main__()