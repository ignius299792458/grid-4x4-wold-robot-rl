import pygame

from grid_4x4_robot.config import CELL_SIZE, GRID_LINE_COLOR, GRID_SIZE, WINDOW_SIZE


def draw_grid(surface):
    for i in range(GRID_SIZE + 1):
        pos = i * CELL_SIZE
        # Vertical lines
        pygame.draw.line(surface, GRID_LINE_COLOR, (pos, 0), (pos, WINDOW_SIZE), 2)
        # Horizontal lines
        pygame.draw.line(surface, GRID_LINE_COLOR, (0, pos), (WINDOW_SIZE, pos), 2)
