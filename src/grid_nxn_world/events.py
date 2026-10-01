import pygame

from grid_nxn_world.world import GridWorld


def handle_events(world: GridWorld):
    """Processes window and keyboard events for GridWorld"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                world.step(0, -1)
            elif event.key == pygame.K_DOWN:
                world.step(0, 1)
            elif event.key == pygame.K_LEFT:
                world.step(-1, 0)
            elif event.key == pygame.K_RIGHT:
                world.step(1, 0)
            elif event.key == pygame.K_r:  # reset : Key - "r"
                world.reset()

    return True
