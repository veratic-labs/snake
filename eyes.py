"""
Copyright (c) 2022-2026 Veratic Labs
Licensed under the Apache License, Version 2.0
"""

import pygame

class Eyes:
	def __init__(self,head):
		self.screen=head.screen

		self.radius=3
		self.colour=(0,0,0)

		self.x_1=head.x+head.width-2*self.radius
		self.y_1=head.y+4*self.radius
		self.x_2=head.x+head.width-2*self.radius
		self.y_2=head.y+6*self.radius

	def update_up_position(self,head):
		self.x_1=head.x+2*self.radius
		self.y_1=head.y+2*self.radius
		self.x_2=head.x+6*self.radius
		self.y_2=head.y+2*self.radius

	def update_down_position(self,head):
		self.x_1=head.x+2*self.radius
		self.y_1=head.y+head.height-2*self.radius
		self.x_2=head.x+6*self.radius
		self.y_2=head.y+head.height-2*self.radius

	def update_right_position(self,head):
		self.x_1=head.x+head.width-2*self.radius
		self.y_1=head.y+2*self.radius
		self.x_2=head.x+head.width-2*self.radius
		self.y_2=head.y+6*self.radius

	def update_left_position(self,head):
		self.x_1=head.x+2*self.radius
		self.y_1=head.y+2*self.radius
		self.x_2=head.x+2*self.radius
		self.y_2=head.y+6*self.radius

	def update_position(self,head):
		if head.moving_up:
			self.update_up_position(head)
		if head.moving_down:
			self.update_down_position(head)
		if head.moving_right:
			self.update_right_position(head)
		if head.moving_left:
			self.update_left_position(head)

	def draw_eyes(self):
		self.circle_1=[self.x_1,self.y_1]
		pygame.draw.circle(self.screen,self.colour,self.circle_1,self.radius)
		self.circle_2=[self.x_2,self.y_2]
		pygame.draw.circle(self.screen,self.colour,self.circle_2,self.radius)

	def update_eyes(self,head,game):
		if game.moving:
			self.update_position(head)
		self.draw_eyes()
