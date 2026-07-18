"""
Snake game
A snake game written in Python using Pygame.

Copyright (c) 2022-2026 Veratic Labs
Licensed under the Apache License, Version 2.0
"""

#import modulus
import sys
import pygame
import time
from head import Head
from food import Food
from body import Body
from game_over import Gameover
from score import Score
from button import Button

#class control the game
class Game:
	def __init__(self):
		self.create_surface()

		self.head=Head(self)
		self.food=Food(self)
		self.body=Body(self)
		self.over=Gameover(self)
		self.score=Score(self)
		self.button=Button(self)

		self.moving=False
		self.initial_time=time.time()
		self.time_interval=0.1

	def create_surface(self):
		pygame.init()
		self.logo=pygame.image.load('logo.png')
		pygame.display.set_icon(self.logo)
		self.screen_width=600
		self.screen_height=500
		self.screen=pygame.display.set_mode((self.screen_width,self.screen_height))
		pygame.display.set_caption('贪吃蛇')
		self.bg_colour=(230,230,230)

	def check_moving(self):
		final_time=time.time()
		if final_time>=self.initial_time+self.time_interval:
			self.moving=True
			self.initial_time=final_time
		else:
			self.moving=False
	
	def check_event(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				self.head.operating_keydown_event(event)
			elif event.type==pygame.MOUSEBUTTONDOWN:
				mouse_pos=pygame.mouse.get_pos()
				self.button.operating_mouse_down(mouse_pos)

	def restart_game(self):
		if self.button.restart:
			self.head=Head(self)
			self.food=Food(self)
			self.body=Body(self)
			self.over=Gameover(self)
			self.score=Score(self)
			self.button=Button(self)

	def update_screen(self):
		self.screen.fill(self.bg_colour)
		self.check_moving()
		self.food.update_food(self)
		self.body.update_body(self)
		self.head.update_head(self)
		self.over.update_gameover(self)
		self.score.update_score(self)
		self.button.draw()
		self.food.eat=False
		
	def run_game(self):
		while True:
			self.check_event()
			self.restart_game()
			self.update_screen()
			pygame.display.flip()

