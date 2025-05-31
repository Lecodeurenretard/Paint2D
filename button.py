# Créé par adekambin, le 28/05/2025 en Python 3.7
from header import *
from globals import *
class Button:
	BASE_COLOR = 0x613434

	butt_list = []
	icon_scale : float = .8		# The scale factor of the icon (in [0, 1])

	def __init__(self, x : int, y : int , size : int, action, icon : str | None =None):
		self.zone		= Rect(x, y, size, size)
		self.callback	= action
		self.already_clicked = False

		if icon != None:
			self.icon = pygame.transform.scale(pygame.image.load(icon), (size * Button.icon_scale, size * Button.icon_scale))
		else:
			self.icon = None
		Button.butt_list.append(self)

	@staticmethod
	def create_button(rect : Rect, action): #-> Button:
		return Button(rect.x, rect.y, rect.w, action)

	@staticmethod
	def update_button_presses(is_mouse_pressed : bool, mouse_pos : tuple[int, int]) -> None:
		if not is_mouse_pressed:
			for butt in Button.butt_list:
				butt.already_clicked = False
			return
		
		for butt in Button.butt_list:
			butt.already_clicked = butt.is_clicked(mouse_pos)

	def is_clicked(self, mouse_pos) -> bool:
		return is_in_rect(mouse_pos, self.zone)

	def is_just_clicked(self, mouse_pos) -> bool:
		return not self.already_clicked and is_in_rect(mouse_pos, self.zone)

	def handle_click(self, mouse_pos) -> None:
		if self.is_clicked(mouse_pos):
			self.activate()

	def activate(self) -> object:
		return self.callback()
	
	def draw(self) -> None:
		if self.already_clicked:
			pygame.draw.rect(menu_surf, darken_color(Button.BASE_COLOR, .8), self.zone)
		else:
			pygame.draw.rect(menu_surf, Button.BASE_COLOR, self.zone)
		
		if self.icon != None:
			offset : float = self.zone.w * (1-Button.icon_scale) / 2	# offset to center the icon
			menu_surf.blit(self.icon, (self.zone.x + offset, self.zone.y + offset))

		pygame.draw.lines(menu_surf, hex_black, True, (
			(self.zone.x				, self.zone.y),
			(self.zone.x + self.zone.w	, self.zone.y),
			(self.zone.x + self.zone.w	, self.zone.y + self.zone.h),
			(self.zone.x 				, self.zone.y + self.zone.h),
		), 2)
