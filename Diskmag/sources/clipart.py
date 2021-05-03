#
# Nomad Diskmag - CLIPARTS
# Rendering images generated by code.
#
# E-zine on a 1.44 floppy tailored made on Raspberry Pi computer.
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/nomad-diskmag
#

import pygame
from pygame.locals import *
import time
import math

class Clipart:
	def __init__(self, mag, clip, pos, transparent="white", palette=("#b21cb0", "#e532e2", "#e5b7e4")):
		self.Mag = mag
		self.clip = clip
		self.pos = pos
		self.pal_shift = 0
		self.transparent = transparent
		self.palette = palette
		self.Mag.scene.add(self)

	def draw(self):
		if self.clip == 'cover_0':
			self.draw_cover_0(self.pos)
		if self.clip == 'floppy':
			self.draw_floppy(self.pos, p=self.palette)
		if self.clip == 'rainbow':
			self.draw_rainbow(self.pos)
		if self.clip == 'pi':
			self.draw_pi(self.pos)
		if self.clip == 'fake_game':
			self.draw_fake_game(self.pos)
	
	def draw_cover_0(self, pos):
		x, y = pos
		y = y - 80 + math.sin(time.time()) * 80
		
		drive_x = self.pos[0] - 4
		drive_y = self.pos[1] - 30

		btn_x = drive_x + 170
		btn_y = drive_y

		pygame.draw.rect(self.Mag.screen, Color("#dddddd"), (drive_x-53, drive_y+20, 270, 10))
		pygame.draw.rect(self.Mag.screen, Color("#cccccc"), (drive_x-53, drive_y-20, 270, 40))

		pygame.draw.rect(self.Mag.screen, Color("#222222"), (drive_x, drive_y, 164, 14))
		pygame.draw.rect(self.Mag.screen, Color("#eeeeee"), (drive_x, drive_y+12, 164, 2))

		self.draw_floppy((x,y), self.palette)

		pygame.draw.rect(self.Mag.screen, Color("#222222"), (drive_x, drive_y, 164, 2))
		pygame.draw.rect(self.Mag.screen, Color("#cccccc"), (drive_x-53, drive_y-20, 270, 20))
		pygame.draw.rect(self.Mag.screen, Color("#eeeeee"), (drive_x-53, drive_y-180, 270, 160))
		pygame.draw.rect(self.Mag.screen, Color("#222222"), (btn_x, btn_y, 20, 12))

	def draw_floppy(self, pos, p):
		x, y = pos
		pygame.draw.rect(self.Mag.screen, Color(p[0]), (x+4, y+4, 152, 160))
		pygame.draw.rect(self.Mag.screen, Color(p[1]), (x, y, 152, 160))
		pygame.draw.rect(self.Mag.screen, Color("#eaeaea"), (x+(152*0.5-40), y, 80, 50))
		pygame.draw.rect(self.Mag.screen, Color(p[1]), (x+84, y+7, 21, 40))
		pygame.draw.rect(self.Mag.screen, Color(p[0]), (x+5, y+142, 8, 8))
		pygame.draw.rect(self.Mag.screen, Color(p[0]), (x+139, y+142, 8, 8))
		pygame.draw.rect(self.Mag.screen, Color(self.transparent), (x+141, y+144, 6, 6))
		pygame.draw.rect(self.Mag.screen, Color(p[2]), (x+20, y+67, 110, 94))
		
	def draw_rainbow(self, pos):
		x, y = pos
		y = y - 180 + math.sin(time.time() * 0.5) * 80
		rows = 7
		pal = [(249, 65, 68),(243, 114, 44),(248, 150, 30),(249, 199, 79),(144, 190, 109),(67, 170, 139),(87, 117, 144)]
		for i in range(rows):
			r,g,b = pal[i][0],pal[i][1],pal[i][2]
			pygame.draw.rect(self.Mag.screen, Color(r,g,b), (x, (y+160*i)+math.sin(i*8)*60, 1280, 320))

	def draw_pi(self, pos):
		x, y = pos
		# green pcb, metal, black chip, yellow rings, 
		pal = [(22,135,92), (159,143,143), (48, 42, 56), (243, 208, 104)]
		pygame.draw.rect(self.Mag.screen, Color(pal[0]), (x,y,250,200))


	def draw_fake_game(self, pos):
		x, y = pos
		s = self.Mag.screen
		pal = [(128,128,128),(192,192,192),(200,255,200)]
		max_z = 24
		for z in range(max_z):
			pygame.draw.rect(s, self.get_shifted_color(0), (x,y-z, 256, 8))

	def get_shifted_color(self, id):
		# FIXME shiftuj
		return Color(self.palette[self.pal_shift + id])