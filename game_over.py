"""
Copyright (c) 2022-2026 Veratic Labs
Licensed under the Apache License, Version 2.0
"""

import pygame

class Gameover:
	def __init__(self,game):
		self.screen=game.screen
		self.screen_rect=self.screen.get_rect()
		self.bg_colour=(255,0,0)
		self.text_colour=(255,255,255)
		self.font=pygame.font.SysFont(None,75)
		self.content='Game Over'
		
		self.prep_text()
		self.over=False

	def prep_text(self):
		self.image=self.font.render(self.content,True,self.text_colour)
		self.rect=self.image.get_rect()
		self.rect.x=300-0.5*self.rect.width
		self.rect.y=300-0.5*self.rect.height

	def check_collision(self,game):
		for segment in game.body.snake[1:]:
			x_collision=game.head.x==segment.x
			y_collision=game.head.y==segment.y
			if x_collision and y_collision:
				self.over=True

	def draw(self):
		if self.over:
			self.bg=[self.rect.x,self.rect.y,self.rect.width,self.rect.height]
			pygame.draw.rect(self.screen,self.bg_colour,self.bg)
			self.screen.blit(self.image,self.rect)

	def stop_moving(self,game):
		if self.over:
			game.head.speed=0

	def update_gameover(self,game):
		self.check_collision(game)
		self.draw()
		self.stop_moving(game)
