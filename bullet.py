#bullet.py
import pygame
import random
import math

BULLET_IMAGE = "bullet.png"
BULLET_WIDTH = 56
BULLET_HEIGHT = 56

class Bullet(pygame.sprite.Sprite):
	def __init__(self, player):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(BULLET_IMAGE)
		self.image = self.image.convert_alpha()
		self.width = BULLET_WIDTH
		self.height = BULLET_HEIGHT
		self.rect = self.image.get_rect()
		self.x = 0
		self.y = 0
		self.dx = 0
		self.dy = 0
		self.rect.center = (self.x, self.y)
		
		self.player = player
		self.isFired = False
		
	def fire(self, shotAngle):
		self.x = self.player.x
		self.y = self.player.y
		
		#self.dx = 
		
		self.isFired = True
		
		print("fire")

	def update(self):
		self.rect.center = (self.x, self.y)

		# dy = tBall.y - reticle.y;
		# dx = tBall.x - reticle.x; 
		# theta = Math.atan2(dy, dx);	//angle in radians
		# angle = theta * 180 / Math.PI;	//angle in degrees
		
		# this.show();
		# this.setMoveAngle(angle - 90);	//-90 to change angle to traditional degrees system
		# this.setSpeed(10);
		# this.setPosition(x, y);

		# shots--;
		# tBall.isFired = true;