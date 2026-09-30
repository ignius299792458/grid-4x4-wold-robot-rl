import pygame

from grid_4x4_robot.config import BG_COLOR, WINDOW_SIZE
from grid_4x4_robot.grid import draw_grid
from grid_4x4_robot.robot import Robot


def create_window():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

    pygame.display.set_caption("4x4 Grid World and Robot")

    return screen, pygame.time.Clock()


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True


def update():
    pass


def draw(screen):
    screen.fill(BG_COLOR)
    draw_grid(screen)
    robot.draw(screen)


robot = Robot(grid_x=0, grid_y=0)


def main():

    screen, clock = create_window()

    running = True
    while running:
        running = handle_events()

        update()

        draw(screen)

        pygame.display.flip()
        clock.tick(60)

    print("_____ Termination of environment _____")

    pygame.quit()
