import os

import pytest

# Force pygame to run in dummy/headless mode so no GUI window opens during tests
os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame

from grid_nxn_world.config import GRID_SIZE
from grid_nxn_world.robot import Robot
from grid_nxn_world.world import GridWorld


@pytest.fixture(autouse=True)
def init_game():
    pygame.init()
    yield
    pygame.quit()


def test_robot_initialization():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            robot = Robot(grid_x=i, grid_y=j)
            assert robot.position == (i, j)


def test_boundary_clamping_max():
    robot = Robot(grid_x=3, grid_y=3)

    # Try to move right -> (dx,dy) : (1,0)
    robot.move(1, 0)
    assert robot.position == (3, 3)

    # Try to move down -> (dx,dy) : (0,1)
    robot.move(0, 1)
    assert robot.position == (3, 3)


def test_boundary_clamping_min():
    robot = Robot(grid_x=0, grid_y=0)

    # Try to move left -> (dx,dy) : (-1,0)
    robot.move(-1, 0)
    assert robot.position == (0, 0)

    # Try to move up -> (dx,dy) : (0,-1)
    robot.move(0, -1)
    assert robot.position == (0, 0)


def test_grid_world_step_and_reset():
    world = GridWorld()
    assert world.robot.position == (0, 0)

    # Execute move right
    world.step(1, 0)
    assert world.robot.position == (1, 0)

    # Execute move down
    world.step(0, 1)
    assert world.robot.position == (1, 1)

    # Reset environment
    world.reset()
    assert world.robot.position == (0, 0)
