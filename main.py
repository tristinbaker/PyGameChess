from board import Board
from pygame_handler import PyGameHandler

screen = PyGameHandler()
board = Board()

screen.main_loop(board)