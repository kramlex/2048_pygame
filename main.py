import pygame
import class_game
import class_menu

pygame.init()
window = pygame.display.set_mode((510,620))
screen = pygame.Surface((500,500))
screen.fill( (0,0,0) )
game = class_game.GAME()
game.init()
menu = class_menu.MENU()
menu.init(window, game.score)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Finished = True
			break
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				game.direction = "up"
				game.update()
				menu.draw(game.score, window)
				break
			if event.key == pygame.K_s:
				game.direction = "down"
				game.update()
				menu.draw(game.score, window)
				break
			if event.key == pygame.K_a:
				game.direction = "left"
				game.update()
				menu.draw(game.score, window)
				break
			if event.key == pygame.K_d:
				game.direction = "right"
				game.update()
				menu.draw(game.score, window)
				break
			if event.key == pygame.K_ESCAPE:
				game.Finished = True
				break
	if game.Finished == True:
		break
	window.blit(screen , (5,115) )
	game.draw(screen)
