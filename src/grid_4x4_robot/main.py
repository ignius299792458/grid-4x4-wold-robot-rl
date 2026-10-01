import pygame

from grid_4x4_robot.config import GRID_SIZE, WINDOW_SIZE
from grid_4x4_robot.events import handle_events
from grid_4x4_robot.world import GridWorld


def create_window():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption(f"{GRID_SIZE}x{GRID_SIZE} GridWorld-X-Robot")
    return screen, pygame.time.Clock()


def main():
    world = GridWorld()
    screen, clock = create_window()

    running = True
    while running:
        running = handle_events(world)

        world.update()

        world.draw(screen)

        pygame.display.update()
        clock.tick(60)

    print("_____ Termination of environment _____")
    pygame.quit()


if __name__ == "__main__":
    main()
