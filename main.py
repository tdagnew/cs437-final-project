################################################################################
#                               Tankball!                                      #
#                       Corey Stockton, Thomas Agnew                           #
#                               CSCI 43700                                     #
#                                11/27/18                                      #
################################################################################
import pygame
from ball import Ball
from player import Player
from bullet import Bullet
from turret import Turret
from divider import Divider

pygame.init()

def main(width, height):
	screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
	pygame.display.set_caption("Tankball!")

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((255, 255, 255))
	screen.blit(background, (0, 0))

	state = "PAUSED"

	#sound effect
	victorySound = pygame.mixer.Sound("victory.wav")
	victoryPlayed = False
	
	#create players and ball
	player1 = Player(screen, 1)
	player2 = Player(screen, 2)
	turret1 = Turret(player1)
	turret2 = Turret(player2)
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
	divider = Divider(screen)

	#group sprites
	ballSprite = pygame.sprite.Group(ball)
	playerSprites = pygame.sprite.Group(player1,player2)
	turretSprites = pygame.sprite.Group(turret1,turret2)
	p1BulletSprites = pygame.sprite.Group()
	p2BulletSprites = pygame.sprite.Group()

	for i in range(1):
		p1BulletSprites.add(p1Bullets[i])
		p2BulletSprites.add(p2Bullets[i])
	uiSprites = pygame.sprite.Group(divider)

	#UI
	title_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 10)).render("Tankball!", True, pygame.color.Color("Black"))

	pause_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 20)).render("Paused (Return/P)", True, pygame.color.Color("Red"))

	controls_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("Controls", True, pygame.color.Color("Red"))

	unpause_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("Return or P - Pause/Unpause", True, pygame.color.Color("Red"))
	
	move_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("A/D or Left/Right - Move", True, pygame.color.Color("Red"))

	aim_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("W/S or Up/Down - Aim", True, pygame.color.Color("Red"))

	fire_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("Spacebar or Right CTRL - Fire", True, pygame.color.Color("Red"))

	win_text1 = pygame.font.SysFont('Consolas', int(screen.get_width() / 20)).render("Player 1 wins!", True, pygame.color.Color("Black"))

	win_text2 = pygame.font.SysFont('Consolas', int(screen.get_width() / 20)).render("Player 2 wins!", True, pygame.color.Color("Black"))
	
	restart_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("R to Restart", True, pygame.color.Color("Black"))

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
				
				#recenter ball
				ball.x = screen.get_width() / 2
				ball.y = screen.get_height() / 3

				#resize UI
				title_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 10)).render("Tankball!", True, pygame.color.Color("Black"))

				pause_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 20)).render("Paused", True, pygame.color.Color("Red"))

				controls_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("Controls", True, pygame.color.Color("Red"))

				unpause_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("Return or P - Pause/Unpause", True, pygame.color.Color("Red"))
				
				move_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("A/D or Left/Right - Move", True, pygame.color.Color("Red"))

				aim_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("W/S or Up/Down - Aim", True, pygame.color.Color("Red"))

				fire_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("Spacebar or Right CTRL - Fire", True, pygame.color.Color("Red"))

				win_text1 = pygame.font.SysFont('Consolas', int(screen.get_width() / 20)).render("Player 1 wins!", True, pygame.color.Color("Black"))

				win_text2 = pygame.font.SysFont('Consolas', int(screen.get_width() / 20)).render("Player 2 wins!", True, pygame.color.Color("Black"))
				
				restart_text = pygame.font.SysFont('Consolas', int(screen.get_width() / 40)).render("R to Restart", True, pygame.color.Color("Black"))
				
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
						return True, screen.get_width(), screen.get_height()

		screen.blit(background, (0, 0))

		#clear sprites
		ballSprite.clear(screen, background)
		playerSprites.clear(screen, background)
		uiSprites.clear(screen, background)

		#update sprites
		ballSprite.update()
		turretSprites.update()
		playerSprites.update()
		p1BulletSprites.update()
		p2BulletSprites.update()
		uiSprites.update()

		#draw sprites
		ballSprite.draw(screen)
		p1BulletSprites.draw(screen)
		p2BulletSprites.draw(screen)
		playerSprites.draw(screen)
		turretSprites.draw(screen)
		uiSprites.draw(screen)

		score_text1 = pygame.font.SysFont('Consolas', int(screen.get_width() / 10)).render("{0}".format(player1.score), True, pygame.color.Color("Black"))
		score_text2 = pygame.font.SysFont('Consolas', int(screen.get_width() / 10)).render("{0}".format(player2.score), True, pygame.color.Color("Black"))

		screen.blit(score_text1, (0, 0))
		screen.blit(score_text2, (screen.get_width() - score_text2.get_width(), 0))
		if state == "PAUSED":
			screen.blit(title_text, (screen.get_width() / 2 - (title_text.get_width() / 2), 0))

			offset = score_text1.get_height()
			screen.blit(pause_text, (0, offset))
			offset += pause_text.get_height()
			screen.blit(controls_text, (0, offset))
			offset += controls_text.get_height()
			screen.blit(unpause_text, (0, offset))
			offset += unpause_text.get_height()
			screen.blit(move_text, (0, offset))
			offset += move_text.get_height()
			screen.blit(aim_text, (0, offset))
			offset += aim_text.get_height()
			screen.blit(fire_text, (0, offset))

		if player1.score >= 5:
			screen.blit(win_text1, ((screen.get_width() / 2) - (win_text1.get_width() / 2), (screen.get_height() / 2) - (win_text1.get_height() / 2)))
			screen.blit(restart_text, ((screen.get_width() / 2) - (restart_text.get_width() / 2), (screen.get_height() / 2) + win_text1.get_height()))

			if victoryPlayed == False:
				victorySound.play()
				victoryPlayed = True
			
			for ball in ballSprite.sprites():
				ball.pause()
			for player in playerSprites.sprites():
				player.pause()

			state = "END"
		elif player2.score >= 5:
			screen.blit(win_text2, ((screen.get_width() / 2) - (win_text2.get_width() / 2), (screen.get_height() / 2) - (win_text2.get_height() / 2)))
			screen.blit(restart_text, ((screen.get_width() / 2) - (restart_text.get_width() / 2), (screen.get_height() / 2) + win_text2.get_height()))

			if victoryPlayed == False:
				victorySound.play()
				victoryPlayed = True
			
			for ball in ballSprite.sprites():
				ball.pause()
			for player in playerSprites.sprites():
				player.pause()

			state = "END"

		pygame.display.flip()

	return False, 0, 0

if __name__ == "__main__":
	replay, width, height = main(800, 400)

	while replay == True:
		replay, width, height = main(width, height)
