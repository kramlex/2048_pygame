import pygame

class MENU:
	def init(self,screen ,score):
		pygame.font.init()
		self.font = pygame.font.Font('10289.otf',45)
		self.draw(score,screen)
	def draw(self, score, screen):
		screen.fill( (0,0,0) )
		score_text = "SCORE:" + str(score)
		score_box = self.font.render(score_text , True , (255,255,255) )
		screen.blit(score_box , (20,40))