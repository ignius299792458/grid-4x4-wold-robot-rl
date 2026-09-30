import pygame


def handle_events(robot):
    """Processes window and keyboard events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("move : up")
                robot.move(0, -1)
            elif event.key == pygame.K_DOWN:
                print("move : down")
                robot.move(0, 1)
            elif event.key == pygame.K_LEFT:
                print("move : left")
                robot.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                print("move : right")
                robot.move(1, 0)

    return True
