"""
Copyright (c) 2022-2026 Veratic Labs
Licensed under the Apache License, Version 2.0
"""

import pygame

class Score:
	def __init__(self,game):
		self.screen=game.screen
		self.screen_rect=self.screen.get_rect()

		self.score=0
		self.content='score'
		self.line_width=600
		self.line_height=10
		self.line_x=0
		self.line_y=100-self.line_height

		self.font=pygame.font.SysFont(None,50)
		self.colour=(0,0,0)

	def draw_content(self):
		self.content_image=self.font.render(self.content,True,self.colour)
		self.content_rect=self.content_image.get_rect()
		self.content_rect.midtop=self.screen_rect.midtop
		self.screen.blit(self.content_image,self.content_rect)

	def draw_score(self):
		score_str=str(self.score)
		self.score_image=self.font.render(score_str,True,self.colour)
		self.score_rect=self.score_image.get_rect()
		self.score_rect.midtop=self.content_rect.midbottom
		self.screen.blit(self.score_image,self.score_rect)

	def draw_line(self):
		self.line_rect=[self.line_x,self.line_y,self.line_width,self.line_height]
		pygame.draw.rect(self.screen,self.colour,self.line_rect)

	def update(self,game):
		if game.food.eat:
			self.score+=1

	def update_score(self,game):
		self.update(game)
		self.draw_line()
		self.draw_content()
		self.draw_score()
