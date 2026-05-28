"""
Copyright (c) 2022-2026 Ignaxus
Licensed under the Apache License, Version 2.0
"""

import pygame

class Segment:
	def __init__(self,game):
		self.screen=game.screen

		self.x=-100
		self.y=-100
		self.width=25
		self.height=25
		self.colour=(255,75,0)

	def draw_segment(self):
		self.rect=[self.x,self.y,self.width,self.height]
		pygame.draw.rect(self.screen,self.colour,self.rect)

class Body:
	def __init__(self,game):
		self.screen=game.screen
		self.snake=[]
		self.snake.append(game.head)

		self.moving=False

	def create_body(self,game):
		if game.food.eat:
			new_segment=Segment(game)
			self.snake.append(new_segment)

	def update_position(self,game):
		if game.moving and game.over.over==False:
			number=len(self.snake)
			tool=list(range(1,number))
			tool.reverse()
			for n in tool:
				self.snake[n].x=self.snake[n-1].x
				self.snake[n].y=self.snake[n-1].y

	def draw_body(self):
		for segment in self.snake[1:]:
			segment.draw_segment()

	def update_body(self,game):
		self.create_body(game)
		self.update_position(game)
		self.draw_body()

