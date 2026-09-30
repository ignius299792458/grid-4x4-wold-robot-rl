import sys

import pygame

from grid_4x4_robot.config import BG_COLOR, WINDOW_SIZE
from grid_4x4_robot.grid import draw_grid
from grid_4x4_robot.robot import Robot

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("4x4 Grid World Robot")
clock = pygame.time.Clock()

# Instantiate robot at top-left cell (0, 0)
# robot = Robot(grid_x=0, grid_y=0)


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        # Draw environment & entities
        draw_grid(screen)
        # robot.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
