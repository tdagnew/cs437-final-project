#player.py
import pygame
import random
import math
from bullet import Bullet

PLAYER_IMAGE = "tank.png"
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 66

class Player(pygame.sprite.Sprite):
	def __init__(self, screen, ball, number):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(PLAYER_IMAGE)
		self.image = self.image.convert_alpha()
		self.width = PLAYER_WIDTH
		self.height = PLAYER_HEIGHT
		self.rect = self.image.get_rect()

		self.screen = screen
		self.ball = ball
		self.number = number

		if (self.number == 1):
			self.x = 400
			self.y = 900
			self.image = pygame.transform.flip(self.image, True, False)
		else:
			self.x = 1200
			self.y = 900

		self.moveSpeed = 10
		self.shotAngle = 0
		self.bullet = Bullet(self.screen, self, self.ball)

		self.rect.center = (self.x, self.y)

	def fire(self):
		self.bullet.fire(self.shotAngle)

	def checkKeys(self):
		keys = pygame.key.get_pressed()

		if self.number == 1:
			if keys[pygame.K_a]:
				self.x -= self.moveSpeed
			if keys[pygame.K_d]:
				self.x += self.moveSpeed
			if keys[pygame.K_w] and self.shotAngle < 90:
				self.shotAngle += 1
			if keys[pygame.K_d] and self.shotAngle > 0:
				self.shotAngle -= 1
			if keys[pygame.K_SPACE]:
				self.fire()
		if self.number == 2:
			if keys[pygame.K_LEFT]:
				self.x -= self.moveSpeed
			if keys[pygame.K_RIGHT]:
				self.x += self.moveSpeed
			if keys[pygame.K_UP] and self.shotAngle < 90:
				self.shotAngle += 1
			if keys[pygame.K_DOWN] and self.shotAngle > 0:
				self.shotAngle -= 1
			if keys[pygame.K_RCTRL]:
				self.fire()

	def checkBounds(self):
		#ensure player is always on ground
		if (self.y + (self.height / 2)) < self.screen.get_height():
			self.y = self.screen.get_height() - (self.height / 2)
		if (self.y + (self.height / 2)) > self.screen.get_height():
			self.y = self.screen.get_height() - (self.height / 2)

		#left border
		if (self.x - (self.width / 2)) < 0:
			self.x = 0 + (self.width / 2)
		#right border
		if (self.x + (self.width / 2)) > self.screen.get_width():
			self.x = self.screen.get_width() - (self.width / 2)

		#middle of screen (dividing two halves)
		if self.number == 1 and self.x + (self.width / 2) > (self.screen.get_width() / 2):
			self.x = (self.screen.get_width() / 2) - (self.width / 2)
		elif self.number == 2 and self.x - (self.width / 2) < (self.screen.get_width() / 2):
			self.x = (self.screen.get_width() / 2) + (self.width / 2)

	def update(self):
		self.checkKeys()
		self.checkBounds()

		self.rect.center = (self.x, self.y)
