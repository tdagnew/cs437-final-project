#player.py
import pygame

DIVIDER_IMAGE = "divider.png"
DIVIDER_WIDTH = 4
DIVIDER_HEIGHT = 70

class Divider(pygame.sprite.Sprite):
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(DIVIDER_IMAGE)
		self.image = self.image.convert_alpha()
		self.width = DIVIDER_WIDTH
		self.height = DIVIDER_HEIGHT
		self.rect = self.image.get_rect()
		
		self.screen = screen
		self.x = self.screen.get_width() / 2 - 2
		self.y = self.screen.get_height() + 70
		
		self.rect.center = (self.x, self.y)

	def update(self):
		self.x = self.screen.get_width() / 2
		self.y = self.screen.get_height() - self.height / 2
		
		self.rect.center = (self.x, self.y)