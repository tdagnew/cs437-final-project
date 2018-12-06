#bullet.py
import pygame
import random
import math

BULLET_IMAGE = "bullet.png"
BULLET_WIDTH = 40
BULLET_HEIGHT = 40

class Bullet(pygame.sprite.Sprite):
	def __init__(self, screen, player, ball):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(BULLET_IMAGE)
		self.image = self.image.convert_alpha()
		self.width = BULLET_WIDTH
		self.height = BULLET_HEIGHT
		self.image = pygame.transform.scale(self.image, (self.width,self.height))
		self.rect = self.image.get_rect()
		self.x = 0
		self.y = 0
		self.dx = 0
		self.dy = 0
		self.ddy = 0
		self.speedScalar = 10
		self.screen = screen
		self.player = player
		self.ball = ball
		self.rect.center = (self.x, self.y)

		self.isFired = False

	def getIsFired(self):
		 return self.isFired

	def fire(self, deg):
		self.x = self.player.rect.centerx + 10
		self.y = self.player.rect.centery
		self.dx = self.speedScalar*math.cos(deg)
		self.dy =self.speedScalar*math.sin(deg)
		print("Fired at {} and {} with a speed of {} and {}".format(self.x,self.y,self.dx,self.dy))
		self.isFired = True

	def checkHitBounds(self):
		if(self.isFired):
			#only checking alive bullets
			if(self.rect.centery > self.screen.get_height()):
				#in the floor
				self.isFired = False
			if(0 > self.rect.centery):
				#in the ceiling
				self.isFired = False
			if(self.rect.centerx > self.screen.get_width()):
				#in the right wall
				self.isFired = False
			if(0 > self.rect.centerx):
				#in the left wall
				self.isFired = False

	def checkBallHit(self):
		if(self.isFired):
			dx = self.rect.centerx - self.ball.rect.centerx
			dy = self.rect.centery - self.ball.rect.centery
			mag = math.sqrt(((dx**2)+(dy**2)))
			if(mag <= self.ball.radius):
				self.isFired = False
				try:
					unitVec = (dx/mag, dy/mag)
				except: #in the case the user clicks on the topmid and divide by zero
					unitVec = (0, -1)
				self.ball.addForce(unitVec)

	'''def checkGravity(self):
		if(self.isFired):
			ddy = 1
		else:
			ddy = 0'''

	def updateSpeed(self):
		if(self.isFired):
			self.x += self.dx
			self.y += self.dy
			self.dy += self.ddy

	def update(self):
		self.checkHitBounds()
		self.updateSpeed()
		self.checkBallHit()
		self.rect.center = (self.x, self.y)
