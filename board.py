import pygame
import numpy as np

from settings import *
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.king import King
from pieces.queen import Queen

class Board:

	def __init__(self):
		self.board = self.initialize_board()
		self.pieces = self.initialize_pieces()

	def initialize_board(self):
		board = np.zeros((8,8),dtype=int)
		board[1::2,::2] = 1
		board[::2,1::2] = 1
		return board

	def initialize_pieces(self):
		pieces = []
		for i in range(len(PAWNS)):
			for j in range(len(PAWNS[i])):
				if PAWNS[i][j] == 2:
					pieces.append(Pawn(j, i, ISBLACK))
				if PAWNS[i][j] == 1:
					pieces.append(Pawn(j, i, ISWHITE))
		for i in range(len(BISHOPS)):
			for j in range(len(BISHOPS[i])):
				if BISHOPS[i][j] == 2:
					pieces.append(Bishop(j, i, ISBLACK))
				if BISHOPS[i][j] == 1:
					pieces.append(Bishop(j, i, ISWHITE))
		for i in range(len(KNIGHTS)):
			for j in range(len(KNIGHTS[i])):
				if KNIGHTS[i][j] == 2:
					pieces.append(Knight(j, i, ISBLACK))
				if KNIGHTS[i][j] == 1:
					pieces.append(Knight(j, i, ISWHITE))
		for i in range(len(ROOKS)):
			for j in range(len(ROOKS[i])):
				if ROOKS[i][j] == 2:
					pieces.append(Rook(j, i, ISBLACK))
				if ROOKS[i][j] == 1:
					pieces.append(Rook(j, i, ISWHITE))
		for i in range(len(KINGS)):
			for j in range(len(KINGS[i])):
				if KINGS[i][j] == 2:
					pieces.append(King(j, i, ISBLACK))
				if KINGS[i][j] == 1:
					pieces.append(King(j, i, ISWHITE))
		for i in range(len(QUEENS)):
			for j in range(len(QUEENS[i])):
				if QUEENS[i][j] == 2:
					pieces.append(Queen(j, i, ISBLACK))
				if QUEENS[i][j] == 1:
					pieces.append(Queen(j, i, ISWHITE))
		return pieces

	def get_pieces(self):
		rects = []
		for piece in self.pieces:
			rects.append(piece.get_rect())
		return rects

	def print_text_board(self):
		print(self.board)

	def print_board(self, screen):
		xcor = 0
		ycor = -100
		for row in self.board:
			ycor += 1 * CELLHEIGHT
			xcor = 0
			for col in row:
				rect = pygame.Rect(xcor, ycor, CELLWIDTH, CELLHEIGHT)
				if col == 1:
					pygame.draw.rect(screen, BROWN, rect)
				else:
					pygame.draw.rect(screen, WHITE, rect)
				xcor += 1 * CELLWIDTH

	def print_pieces(self, screen):
		for piece in self.pieces:
			piece.draw(screen)