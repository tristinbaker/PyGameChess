from pieces.piece import *

class Bishop(Piece):

	def __init__(self, xcor, ycor, white):
		self.xcor = xcor
		self.ycor = ycor
		self.alive = True
		self.rect = pygame.Rect(xcor*CELLWIDTH, ycor*CELLHEIGHT, CELLWIDTH, CELLHEIGHT)
		self.white = white
		image_name = "white_bishop.png" if self.white else "black_bishop.png"
		self.image = pygame.image.load('images/' + image_name)
		self.image = pygame.transform.rotozoom(self.image, 0, 1.5)

