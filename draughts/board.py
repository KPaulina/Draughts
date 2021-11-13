import pygame
from draughts.constants import BLACK, ROWS, WHITE, SQUARE_SIZE


class Board:

    def __init__(self):
        self.board = []
        self.selected_piece = False
        self.black_left = self.white_left = 12
        self.black_queens = self.white_queens = 0

    def draw_board(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

