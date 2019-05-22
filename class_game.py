import random
import func
import pygame

class GAME:
	def init(self):
		self.game_box = func.init_game_box()
		self.Finished = False
		self.direction = ""
		self.tmp_game_box = []
		self.score = 0

	def draw(self, screen):
		self.by = 0
		for i in range(4):
			self.bx = 0
			for j in range(4):
				nubmer_surf = func.get_surf(self.game_box , i , j )
				screen.blit(nubmer_surf, (self.bx, self.by) )
				self.bx += 125
			self.by+= 125
		pygame.display.flip()

	def update(self):
		self.tmp_game_box = func.get_tmp_list(self.game_box)
		if self.direction == "up":
			for i in range(4):
				tmp = func.get_column(self.game_box , i, self.direction)
				self.score += tmp[4]
				self.game_box = func.column_tmp_to_list( tmp , self.game_box , i)

		elif self.direction == "down":
			for i in range(4):
				tmp = func.get_column(self.game_box , i,self.direction )
				self.score += tmp[4]
				self.game_box = func.column_tmp_to_list( tmp , self.game_box , i)

		elif self.direction == "left":
			for i in range(4):
				tmp = func.get_line(self.game_box , i , self.direction)
				self.score += tmp[4]
				self.game_box = func.line_tmp_to_list( tmp , self.game_box , i)

		elif self.direction == "right":
			for i in range(4):
				tmp = func.get_line(self.game_box , i , self.direction )
				self.score += tmp[4]
				self.game_box = func.line_tmp_to_list( tmp , self.game_box , i)
		
		if func.equal_lists(self.game_box, self.tmp_game_box) == False:
			self.game_box = func.add_new_cell(self.game_box)