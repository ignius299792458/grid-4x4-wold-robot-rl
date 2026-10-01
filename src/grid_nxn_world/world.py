"""
GridWorld:

This encapsulates the world state, robot instance, step executions,
reset triggers, and rendering in one clean place—making
it extremely modular and ready for RL environment wrappers
if needed in the future
"""

import pygame

from grid_nxn_world.config import BG_COLOR
from grid_nxn_world.grid import draw_grid
from grid_nxn_world.robot import Robot


class GridWorld:
    def __init__(self):
        self.robot = Robot(grid_x=0, grid_y=0)

    def step(self, dx: int, dy: int):
        """Execute a movement action in the grid world."""
        print(f"from : {self.robot.grid_x}, {self.robot.grid_y}")
        self.robot.move(dx, dy)
        print(f"to : {self.robot.grid_x}, {self.robot.grid_y}")

    def update(self):
        """Update environmental animations and entities."""
        self.robot.update()

    def draw(self, surface: pygame.Surface):
        """Render background grid and environment entities."""
        surface.fill(BG_COLOR)
        draw_grid(surface=surface, active_cell=(self.robot.grid_x, self.robot.grid_y))
        self.robot.draw(surface)

    def reset(self):
        """Reset the environment state back to initial conditions."""
        self.robot.reset(0, 0)
