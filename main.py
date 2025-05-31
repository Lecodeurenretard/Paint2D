# Créé par adekambin, le 28/05/2025 en Python 3.7
from header import *
from button import *

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

def save_drawing() -> None:
	pygame.image.save(drawing_surf, "my_drawing.png")

SAVE_BUTTON : Button = Button(5, 5, 20, save_drawing, "img/save.png")

drawing_surf.fill(hex_white)

prev_mouse_pos = (NaN, NaN)
is_clicking : bool = False
while True:
	menu_surf.unlock()
	window.blits((
		(menu_surf, (0, 0)),
		(drawing_surf, (0, DRAWING_OFFSET)),
	))
	pygame.display.flip()
	draw_menus()
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
				draw_point(drawing_surf, shifted_mouse_pos, current_color)
			else:
				# Draw lines bc in a lot of cases, the mouse mouve faster than 1 pixel per frame
				pygame.draw.line(drawing_surf, current_color, shifted_prev_mouse_pos, shifted_mouse_pos)

		for butt in Button.butt_list:
			if butt.is_just_clicked(mouse_pos):
				butt.activate()


	Button.update_button_presses(is_clicking, mouse_pos)
	prev_mouse_pos = mouse_pos