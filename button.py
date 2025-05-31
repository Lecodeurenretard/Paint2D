# Créé par adekambin, le 28/05/2025 en Python 3.7
from header import *
from globals import *
from os.path import splitext

class Button:
	BASE_COLOR = 0x613434
	DEFAULT_SIZE = 20

	butt_list = []
	icon_scale : float = .8		# The scale factor of the icon (in [0, 1])

	def __init__(self, x : int, y : int , size : int, action, icon : str | None = None, enable_toggle : bool = False):
		self.zone		= Rect(x, y, size, size)
		self.callback	= action
		self.already_clicked = False
		
		self.enable_toggle	= enable_toggle 
		self.toggled		= False

		if icon != None:
			self.icon = pygame.transform.scale(pygame.image.load(icon), (size * Button.icon_scale, size * Button.icon_scale))
		else:
			self.icon = None
		
		if enable_toggle and icon != None:
			icon_no_extention = splitext(icon)[0]
			self.icon_toggled = pygame.transform.scale(pygame.image.load(icon_no_extention + "_toggled.png"), (size * Button.icon_scale, size * Button.icon_scale))
		else:
			self.icon_toggled = None
		
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
	
	@staticmethod
	def location_on_horizontal_grid(first_button_location : tuple[int, int], cell_size : int, cell_index : int, cell_margin : int = 4) -> tuple[int, int]:
		"""
		On a virtual horizontal grid with cells of size `button_size` cell of index zero at `first_button_location`,
		what is the position of the button at index `cell_index`?
		"""
		return (
			first_button_location[0] + cell_size * cell_index + cell_margin * abs(cell_index),
			first_button_location[1],
		)


	def is_clicked(self, mouse_pos) -> bool:
		"""
		Is the button clicked by the user?
		"""
		return is_in_rect(mouse_pos, self.zone)

	def is_just_clicked(self, mouse_pos) -> bool:
		"""
		Has the button jsut been clicked by the user (is currently clicked but not on the previous frame)?
		"""
		return not self.already_clicked and is_in_rect(mouse_pos, self.zone)

	def is_toggled(self) -> bool:
		return self.enable_toggle and self.toggled

	def handle_click(self, mouse_pos) -> None:
		if self.is_just_clicked(mouse_pos):
			self.activate()
			self.toggled = not self.toggled

	def activate(self) -> object:
		return self.callback()
	
	def draw(self) -> None:
		if self.already_clicked:
			pygame.draw.rect(menu_surf, darken_color(Button.BASE_COLOR, .7), self.zone)
		elif self.enable_toggle and self.toggled:
			pygame.draw.rect(menu_surf, darken_color(Button.BASE_COLOR, .8), self.zone)
		else:
			pygame.draw.rect(menu_surf, Button.BASE_COLOR, self.zone)
		
		if self.icon != None:
			offset : float = self.zone.w * (1-Button.icon_scale) / 2	# offset to center the icon
			
			if self.enable_toggle and self.toggled:
				menu_surf.blit(self.icon_toggled, (self.zone.x + offset, self.zone.y + offset))
			else:
				menu_surf.blit(self.icon, (self.zone.x + offset, self.zone.y + offset))

		pygame.draw.lines(menu_surf, hex_black, True, (
			(self.zone.x				, self.zone.y),
			(self.zone.x + self.zone.w	, self.zone.y),
			(self.zone.x + self.zone.w	, self.zone.y + self.zone.h),
			(self.zone.x 				, self.zone.y + self.zone.h),
		), 2)
