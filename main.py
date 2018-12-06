################################################################################
#                             Tank Volleyball                                  #
#                       Corey Stockton, Thomas Agnew                           #
#                               CSCI 43700                                     #
#                                11/27/18                                      #
################################################################################
import pygame
from ball import Ball
from player import Player
from bullet import Bullet

pygame.init()

def main():
	screen = pygame.display.set_mode((800,400),pygame.RESIZABLE)
	pygame.display.set_caption("Tank Volleyball")

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((255, 255, 255))
	screen.blit(background, (0, 0))

	state = "PAUSED"

	#create players and ball
	player1 = Player(screen, 1)
	player2 = Player(screen, 2)
	print("Players have been created.")

	ball = Ball(screen, player1, player2, "PAUSED")
	print("Ball has been created.")

	#create bullets
	p1Bullets = [None]*1
	p2Bullets = [None]*1

	for i in range(1):
		p1Bullets[i] = Bullet(screen,player1,ball)
		p2Bullets[i] = Bullet(screen,player2,ball)
	print("Populated list of bullets.")

	player1.setBullets(p1Bullets)
	player2.setBullets(p2Bullets)
	print("Finished passing bullets to players.")

	#group sprites
	ballSprite = pygame.sprite.Group(ball)
	playerSprites = pygame.sprite.Group(player1,player2)
	p1BulletSprites = pygame.sprite.Group()
	p2BulletSprites = pygame.sprite.Group()

	for i in range(1):
		p1BulletSprites.add(p1Bullets[i])
		p2BulletSprites.add(p2Bullets[i])

	#UI
	pause_text = pygame.font.SysFont('Consolas', 32).render("Paused", True, pygame.color.Color("Red"))

	scoreline = "Player 1: {0} Player 2: {1}".format(player1.score, player2.score)

	score_text = pygame.font.SysFont('Consolas', 32).render(scoreline, True, pygame.color.Color("Red"))
	print("Created UI.")

	clock = pygame.time.Clock()
	print("Clock set.")
	keepGoing = True
	print("Running main game loop...")
	while keepGoing:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				keepGoing = False
			if event.type == pygame.VIDEORESIZE:
				screen = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
				background = pygame.Surface(screen.get_size())
				background = background.convert()
				background.fill((255, 255, 255))
			if event.type == pygame.KEYDOWN:
				#return key or p key (ascii)
				if event.key == 13 or event.key == 112:
					#unpause
					if state == "PAUSED":
						for ball in ballSprite.sprites():
							ball.unpause()
						for player in playerSprites.sprites():
							player.unpause()

						state = "RUNNING"
					#pause
					elif state == "RUNNING":
						for ball in ballSprite.sprites():
							ball.pause()
						for player in playerSprites.sprites():
							player.pause()

						state = "PAUSED"
				#r key
				if event.key == 114:
					if state == "END":
						main()

		screen.blit(background, (0, 0))

		#clear sprites
		ballSprite.clear(screen, background)
		playerSprites.clear(screen, background)


		#update sprites
		ballSprite.update()
		playerSprites.update()
		p1BulletSprites.update()
		p2BulletSprites.update()

		#draw sprites
		ballSprite.draw(screen)
		p1BulletSprites.draw(screen)
		p2BulletSprites.draw(screen)
		playerSprites.draw(screen)

		scoreline = "Player 1: {0} Player 2: {1}".format(player1.score, player2.score)

		score_text = pygame.font.SysFont('Consolas', 32).render(scoreline, True, pygame.color.Color("Red"))

		screen.blit(score_text, (0, 0))
		if state == "PAUSED":
			screen.blit(pause_text, (0, 50))

		if player1.score >= 5:
			win_text = pygame.font.SysFont('Consolas', 32).render("Player 1 wins!", True, pygame.color.Color("Red"))

			screen.blit(win_text, (screen.get_width() / 2, screen.get_height() / 2))

			for ball in ballSprite.sprites():
				ball.pause()
			for player in playerSprites.sprites():
				player.pause()

			state = "END"
		elif player2.score >= 5:
			win_text = pygame.font.SysFont('Consolas', 32).render("Player 2 wins!", True, pygame.color.Color("Red"))

			screen.blit(win_text, (screen.get_width() / 2, screen.get_height() / 2))

			for ball in ballSprite.sprites():
				ball.pause()
			for player in playerSprites.sprites():
				player.pause()

			state = "END"

		pygame.display.flip()

if __name__ == "__main__":
	main()
