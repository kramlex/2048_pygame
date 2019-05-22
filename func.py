import random
import os
import pygame


def get_tmp_list(list):
	list2 = []
	for i in range(4):
		tmp = []
		for j in range(4):
			tmp.append( list[i][j] )
		list2.append(tmp)
	return list2

def equal_lists(list,list2):
	equal = True
	for i in range(4):
		for j in range(4):
			if list[i][j] != list2[i][j]:
				equal = False
	return equal

def init_game_box():

	degrees = [2,4]
	list = [ [0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0] ]
	for i in range(2):
		while True:
			y = random.randint(0,3)
			x = random.randint(0,3)
			if list[y][x] == 0:
				list[y][x] = degrees[ random.randint(0,1) ]
				break
	return list

def add_new_cell(list):
	degrees = [2,4]
	while True:
		y = random.randint(0,3)
		x = random.randint(0,3)
		if list[y][x] == 0:
			list[y][x] = degrees[ random.randint(0,1) ]
			break
	#print list
	return list


def get_surf(list, x , y):
	if list[x][y] == 0:
		img = pygame.image.load(os.path.join('img' , '0.png') ).convert()
		return img
	elif list[x][y] == 2:
		img = pygame.image.load(os.path.join('img' , '2.png') ).convert()
		return img
	elif list[x][y] == 4:
		img = pygame.image.load(os.path.join('img' , '4.png') ).convert()
		return img
	elif list[x][y] == 8:
		img = pygame.image.load(os.path.join('img' , '8.png') ).convert()
		return img
	elif list[x][y] == 16:
		img = pygame.image.load(os.path.join('img' , '16.png') ).convert()
		return img
	elif list[x][y] == 32:
		img = pygame.image.load(os.path.join('img' , '32.png') ).convert()
		return img
	elif list[x][y] == 64:
		img = pygame.image.load(os.path.join('img' , '64.png') ).convert()
		return img
	elif list[x][y] == 128:
		img = pygame.image.load(os.path.join('img' , '128.png') ).convert()
		return img
	elif list[x][y] == 256:
		img = pygame.image.load(os.path.join('img' , '256.png') ).convert()
		return img
	elif list[x][y] == 512:
		img = pygame.image.load(os.path.join('img' , '512.png') ).convert()
		return img
	elif list[x][y] == 1024:
		img = pygame.image.load(os.path.join('img' , '1024.png') ).convert()
		return img
	elif list[x][y] == 2048:
		img = pygame.image.load(os.path.join('img' , '2048.png') ).convert()
		return img

def get_line(list,j,direction):
	scr = 0
	lol = []
	tmp = []
	for i in range(4):
		tmp.append(list[j][i])

	if direction == "right" or direction == "down":
		tmp_0 = []
		tmp_other = []
		for i in range(4):
			if tmp[i] == 0:
				tmp_0.append(tmp[i])
			else:
				tmp_other.append(tmp[i])
		tmp = tmp_0 + tmp_other
		for i in range(2,-1, -1):
			if tmp[i] == tmp[i+1]:
				tmp[i] = 0
				tmp[i+1] *= 2
				lol.append(tmp[i+1])
		tmp_0 = []
		tmp_other = []
		for i in range(4):
			if tmp[i] == 0:
				tmp_0.append(tmp[i])
			else:
				tmp_other.append(tmp[i])

		tmp = tmp_0 + tmp_other
		if lol != []:
			scr = lol[0]
		tmp.append(scr)
		return tmp

	elif direction == "left" or direction == "up":
		tmp_0 = []
		tmp_other = []
		for i in range(4):
			if tmp[i] == 0:
				tmp_0.append(tmp[i])
			else:
				tmp_other.append(tmp[i])
		tmp = tmp_other + tmp_0
		for i in range(1 , 4):
			if tmp[i] == tmp[i-1]:
				tmp[i] = 0
				tmp[i-1] *= 2
				lol.append(tmp[i-1])
		tmp_0 = []
		tmp_other = []
		for i in range(4):
			if tmp[i] == 0:
				tmp_0.append(tmp[i])
			else:
				tmp_other.append(tmp[i])
		tmp = tmp_other + tmp_0
		if lol != []:
			scr = lol[0]
		tmp.append(scr)
		return tmp



def get_column(list,j, direction):
	lol = []
	scr = 0
	tmp = []
	for i in range(4):
		tmp.append(list[i][j] )

	if direction == "right" or direction == "down":
		tmp_0 = []
		tmp_other = []
		for i in range(4):
			if tmp[i] == 0:
				tmp_0.append(tmp[i])
			else:
				tmp_other.append(tmp[i])
		tmp = tmp_0 + tmp_other
		for i in range(2,-1, -1):
			if tmp[i] == tmp[i+1]:
				tmp[i] = 0
				tmp[i+1] *= 2
				lol.append(tmp[i+1])
		tmp_0 = []
		tmp_other = []
		for i in range(4):
			if tmp[i] == 0:
				tmp_0.append(tmp[i])
			else:
				tmp_other.append(tmp[i])
		tmp = tmp_0 + tmp_other
		if lol != []:
			scr = lol[0]
		tmp.append(scr)
		return tmp

	elif direction == "left" or direction == "up":
		tmp_0 = []
		tmp_other = []
		for i in range(4):
			if tmp[i] == 0:
				tmp_0.append(tmp[i])
			else:
				tmp_other.append(tmp[i])
		tmp = tmp_other + tmp_0
		for i in range(1 , 4):
			if tmp[i] == tmp[i-1]:
				tmp[i] = 0
				tmp[i-1] *= 2
				lol.append(tmp[i-1])
		tmp_0 = []
		tmp_other = []
		for i in range(4):
			if tmp[i] == 0:
				tmp_0.append(tmp[i])
			else:
				tmp_other.append(tmp[i])
		tmp = tmp_other + tmp_0
		if lol != []:
			scr = lol[0]
		tmp.append(scr)
		return tmp

def column_tmp_to_list(tmp, list, j):
	for i in range(4):
		list[i][j] = tmp[i]
	return list

def line_tmp_to_list(tmp, list , j):
	for i in range(4):
		list[j][i] = tmp[i]
	return list