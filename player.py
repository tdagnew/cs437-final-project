#player.py
import pygame
import random
import math
from bullet import Bullet

PLAYER_IMAGE = "tank.png"
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 66

class Player(pygame.sprite.Sprite):
	def __init__(self, screen, number):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(PLAYER_IMAGE)
		self.image = self.image.convert_alpha()
		self.width = PLAYER_WIDTH
		self.height = PLAYER_HEIGHT
		self.rect = self.image.get_rect()

		self.state = "PAUSED"
		self.screen = screen
		self.number = number
		self.score = 0

		if (self.number == 1):
			self.x = self.screen.get_width() / 4
			self.y = self.screen.get_height()
			self.image = pygame.transform.flip(self.image, True, False)
		else:
			self.x = (self.screen.get_width() / 4) * 3
			self.y = self.screen.get_height()

		self.moveSpeed = 10
		self.shotAngle = 0
		self.bullets = []*5

		self.rect.center = (self.x, self.y)
		#for key events
		self.justPressed = True

	def setBullets(self, bullets):
		'''this is run once for sending the bullets to the player object'''
		print("Bullets have been set for player {}".format(self.number))
		self.bullets = bullets

	def fire(self):
		'''this is only called to fire a bullet'''
		print("Player {} fired a bullet.".format(self.number))
		for i in range(5):
			if(self.bullets[i].getIsFired()==False):
				#first bullet not fired
				self.bullets[i].fire(self.shotAngle)
				break

	def checkKeys(self):
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if (event == pygame.KEYDOWN):
				if self.number == 1:
					print("Comparing {} and {}".format(event.key,40))
					if(event.key == 40):
						self.fire()
						print("fire")

				if self.number == 2:
					print("Comparing {} and {}".format(event.key,pygame.KRCTRL))
					if(event.key == pygame.K_RCTRL):
						self.fire()
						print("fire")


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

	def pause(self):
		self.state = "PAUSED"

	def unpause(self):
		self.state = "RUNNING"

	def update(self):
		if self.state == "RUNNING":
			self.checkKeys()

		self.checkBounds()

		self.rect.center = (self.x, self.y)
