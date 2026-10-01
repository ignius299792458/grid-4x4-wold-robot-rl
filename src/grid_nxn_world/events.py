from collections.abc import Callable

import pygame


def handle_events(
    robot_move: Callable[[int, int], None],
    robot_reset: Callable[[], None],
) -> bool:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False

        if event.type != pygame.KEYDOWN:
            continue

        if event.key == pygame.K_UP:
            robot_move(0, -1)

        elif event.key == pygame.K_DOWN:
            robot_move(0, 1)

        elif event.key == pygame.K_LEFT:
            robot_move(-1, 0)

        elif event.key == pygame.K_RIGHT:
            robot_move(1, 0)

        elif event.key == pygame.K_r:
            robot_reset()

    return True
