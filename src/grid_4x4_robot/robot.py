import pygame

from grid_4x4_robot.config import CELL_SIZE, ROBOT_COLOR


class Robot:
    def __init__(self, grid_x=0, grid_y=0):
        # Grid coordinates (0 to 3)
        self.grid_x = grid_x
        self.grid_y = grid_y

    def draw(self, surface):
        # Calculate pixel coordinates for the cell center
        center_x = self.grid_x * CELL_SIZE + CELL_SIZE // 2
        center_y = self.grid_y * CELL_SIZE + CELL_SIZE // 2
        radius = CELL_SIZE // 3

        pygame.draw.circle(surface, ROBOT_COLOR, (center_x, center_y), radius)
