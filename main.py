# Créé par adekambin, le 28/05/2025 en Python 3.7
from header import *
from button import *

PLUS_IMAGE : Surface = pygame.image.load("img/plus.png")

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
	if max_size < 0:
		pygame.draw.circle(surface, current_color, pos, brush_size/2, 0)
		return
	
	pygame.draw.circle(surface, current_color, pos, min(brush_size, max_size)/2, 0)

def save_drawing() -> None:
	pygame.image.save(drawing_surf, "my_drawing.png")

def increase_brush_size(how_much : int) -> None:
	global brush_size
	brush_size += how_much
	brush_size = max(1, brush_size)

def toggle_eraser() -> None:
	global is_eraser
	is_eraser = not is_eraser

SAVE_BUTTON : Button = Button(
	5,
	5,
	Button.DEFAULT_SIZE,
	save_drawing,
	"img/save.png"
)

LOWER_SIZE_BUTTON : Button = Button(
	Button.location_on_horizontal_grid((5, 5), Button.DEFAULT_SIZE, 3)[0],
	5,
	Button.DEFAULT_SIZE,
	(lambda: increase_brush_size(-5)),
	"img/lower_size.png"
)
INCREASE_SIZE_BUTTON : Button = Button(
	Button.location_on_horizontal_grid((5, 5), Button.DEFAULT_SIZE, 4)[0],
	5,
	Button.DEFAULT_SIZE,
	(lambda: increase_brush_size(5)),
	"img/increase_size.png"
)

ERASER_BUTTON : Button = Button(
	Button.location_on_horizontal_grid((5, 5), Button.DEFAULT_SIZE, 8)[0],
	5,
	Button.DEFAULT_SIZE,
	toggle_eraser,
	"img/eraser.png",
	True
)

drawing_surf.fill(hex_white)

prev_mouse_pos = (NaN, NaN)
was_clicking : bool = False
is_clicking : bool = False
while True:
	menu_surf.unlock()
	window.blits((
		(menu_surf, (0, 0)),
		(drawing_surf, (0, DRAWING_OFFSET)),
	))
	pygame.display.flip()
	draw_menus()

	brush_coord = Button.location_on_horizontal_grid((5 + 11, 15), Button.DEFAULT_SIZE, 5)
	draw_brush((
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
				pygame.draw.line(drawing_surf, current_color, shifted_prev_mouse_pos, shifted_mouse_pos, brush_size)
				draw_brush(shifted_mouse_pos)
				current_color = color_remember


		for butt in Button.butt_list:
			butt.handle_click(mouse_pos)


	Button.update_button_presses(is_clicking, mouse_pos)
	prev_mouse_pos = mouse_pos
	was_clicking = is_clicking