import pygame
from eyes import Eyes

class Head:
	def __init__(self,game):
		self.screen=game.screen

		self.colour=(255,75,0)
		self.width=25
		self.height=25
		self.speed=25
		self.x=400
		self.y=300

		self.moving_up=False
		self.moving_down=False
		self.moving_right=True
		self.moving_left=False

		self.eyes=Eyes(self)
	
	def cross(self,game):
		if self.x==0-self.width:
			self.x=600-self.width
		if self.x==600:
			self.x=0
		if self.y==100-self.height:
			self.y=500-self.height
		if self.y==500:
			self.y=100

	def update_position(self,game):
		if game.moving:
			game.body.moving=True
			if self.moving_up:
				self.y-=self.speed
			if self.moving_down:
				self.y+=self.speed
			if self.moving_right:
				self.x+=self.speed
			if self.moving_left:
				self.x-=self.speed
			self.cross(game)
		
	def operating_keydown_event(self,event):
		if event.key==pygame.K_RIGHT and self.moving_left==False:
			self.moving_right=True
			self.moving_up=False
			self.moving_down=False
			self.moving_left=False

		elif event.key==pygame.K_LEFT and self.moving_right==False:
			self.moving_right=False
			self.moving_up=False
			self.moving_down=False
			self.moving_left=True

		elif event.key==pygame.K_UP and self.moving_down==False:
			self.moving_right=False
			self.moving_up=True
			self.moving_down=False
			self.moving_left=False

		elif event.key==pygame.K_DOWN and self.moving_up==False:
			self.moving_right=False
			self.moving_up=False
			self.moving_down=True
			self.moving_left=False

	def draw_head(self):
		self.rect=[self.x,self.y,self.width,self.height]
		pygame.draw.rect(self.screen,self.colour,self.rect)

	def update_head(self,game):
		self.update_position(game)
		self.draw_head()
		self.eyes.update_eyes(self,game)
