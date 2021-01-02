import pygame
import sys
import math

class PyGameHandler:

	def __init__(self):
		pygame.init()
		self.width = 800
		self.height = 800
		self.window = pygame.display.set_mode([self.width, self.height])
		pygame.display.set_caption("Chess")
		self.screen = pygame.display.get_surface()

	def main_loop(self, board):
		selected = None
		while True:
			for event in pygame.event.get():
				pieces = board.get_pieces()
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						for i, piece in enumerate(pieces):
							if piece.collidepoint(event.pos):
								selected = i
								selected_offset_x = piece.x - event.pos[0]
								selected_offset_y = piece.y - event.pos[1]

				elif event.type == pygame.MOUSEBUTTONUP:
						if event.button == 1:
							selected = None

				elif event.type == pygame.MOUSEMOTION:
						if selected is not None:
							pieces[selected].x = self.roundup(event.pos[0] + selected_offset_x)
							pieces[selected].y = self.roundup(event.pos[1] + selected_offset_y)

			pygame.display.flip()
			board.print_text_board()
			board.print_board(self.screen)
			board.print_pieces(self.screen)

	def roundup(self, x):
		return int(math.ceil(x / 100)) * 100