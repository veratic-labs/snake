import pygame
import random

class Food:
	def __init__(self,game):
		self.screen=game.screen
		self.width=game.screen_width
		self.height=game.screen_height

		self.radius=12.5
		self.colour=(255,0,0)
		self.x=random.randint(0,23)*25+self.radius
		self.y=random.randint(4,19)*25+self.radius

		self.eat=False

	def append_initial_element(self):
		self.x_available=[]
		self.y_available=[]
		for x in range(0,24):
			x=x*25+self.radius
			self.x_available.append(x)
		for y in range(4,20):
			y=y*25+self.radius
			self.y_available.append(y)

	def append_body_element(self,game):
		self.x_values=[]
		self.y_values=[]
		for segment in game.body.snake:
			x=segment.x+self.radius
			y=segment.y+self.radius
			self.x_values.append(x)
			self.y_values.append(y)
		self.x_values=list(set(self.x_values))
		self.y_values=list(set(self.y_values))

	def adjust_list(self):
		for x in self.x_values:
			self.x_available.remove(x)
		for y in self.y_values:
			self.y_available.remove(y)

	def check_collision(self,game):
		x_collision=self.x==game.head.x+self.radius
		y_collision=self.y==game.head.y+self.radius
		if x_collision and y_collision:
			self.eat=True

	def update_position(self,game):
		self.x=random.choice(self.x_available)
		self.y=random.choice(self.y_available)

	def draw_food(self):
		self.circle=[self.x,self.y]
		pygame.draw.circle(self.screen,self.colour,self.circle,self.radius)

	def update_food(self,game):
		self.check_collision(game)
		if self.eat:
			self.append_initial_element()
			self.append_body_element(game)
			self.adjust_list()
			self.update_position(game)
		self.draw_food()