from settings import *
import pygame

class Piece:

	def __init__(self, xcor, ycor, white):
		self.xcor = xcor
		self.ycor = ycor
		self.alive = True
		self.rect = pygame.Rect(xcor*CELLWIDTH, ycor*CELLHEIGHT, CELLWIDTH, CELLHEIGHT)
		self.white = white
		self.image = pygame.image.load('images/black_pawn.png')

	def move(self, xcor, ycor):
		self.xcor = xcor
		self.ycor = ycor

	def draw(self, screen):
		#color = (255, 140, 80) if self.white else (0, 0, 0)
		#pygame.draw.rect(screen, color, self.rect)
		screen.blit(self.image, self.rect)

	def get_rect(self):
		return self.rect

