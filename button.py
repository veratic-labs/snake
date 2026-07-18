"""
Copyright (c) 2022-2026 Veratic Labs
Licensed under the Apache License, Version 2.0
"""

import pygame

class Button:
	def __init__(self,game):
		self.screen=game.screen
		self.screen_rect=self.screen.get_rect()

		self.button_colour=[0,100,255]
		self.text_colour=[0,0,0]
		self.font=pygame.font.SysFont(None,48)

		self.content='RESTART'
		self.prep_text()

		self.restart=False

	def prep_text(self):
		self.image=self.font.render(self.content,True,self.text_colour,self.button_colour)
		self.image_rect=self.image.get_rect()
		self.image_rect.x=0
		self.image_rect.y=0
		self.width=self.image_rect.width
		self.height=self.image_rect.height

	def draw(self):
		self.screen.blit(self.image,self.image_rect)

	def operating_mouse_down(self,mouse_pos):
		if mouse_pos[0]<self.width and mouse_pos[1]<self.height:
			self.restart=True

