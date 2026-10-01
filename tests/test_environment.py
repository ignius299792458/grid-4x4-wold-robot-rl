import os

import pytest

# Force pygame into headless mode during tests.
os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame

from grid_nxn_world.config import DEFAULT_CELL_SIZE, DEFAULT_GRID_SIZE
from grid_nxn_world.robot import Robot
from grid_nxn_world.world import GridWorld


@pytest.fixture(autouse=True)
def init_game():
    pygame.init()
    yield
    pygame.quit()


def test_robot_initialization():
    for x in range(DEFAULT_GRID_SIZE):
        for y in range(DEFAULT_GRID_SIZE):
            robot = Robot(
                grid_size=DEFAULT_GRID_SIZE,
                cell_size=DEFAULT_CELL_SIZE,
                grid_x=x,
                grid_y=y,
            )

            assert robot.position == (x, y)


def test_robot_boundary_clamping_max():
    max_position = DEFAULT_GRID_SIZE - 1

    robot = Robot(
        grid_size=DEFAULT_GRID_SIZE,
        cell_size=DEFAULT_CELL_SIZE,
        grid_x=max_position,
        grid_y=max_position,
    )

    # Move right beyond boundary.
    robot.move(1, 0)
    assert robot.position == (max_position, max_position)

    # Move down beyond boundary.
    robot.move(0, 1)
    assert robot.position == (max_position, max_position)


def test_robot_boundary_clamping_min():
    robot = Robot(
        grid_size=DEFAULT_GRID_SIZE,
        cell_size=DEFAULT_CELL_SIZE,
        grid_x=0,
        grid_y=0,
    )

    # Move left beyond boundary.
    robot.move(-1, 0)
    assert robot.position == (0, 0)

    # Move up beyond boundary.
    robot.move(0, -1)
    assert robot.position == (0, 0)


def test_grid_world_initialization():
    world = GridWorld()

    assert world.grid_size == DEFAULT_GRID_SIZE
    assert world.grid_cell_size == DEFAULT_CELL_SIZE
    assert world.robot_position == (0, 0)


def test_grid_world_robot_move_and_reset():
    world = GridWorld()

    # Move right.
    world.robot_move(1, 0)
    assert world.robot_position == (1, 0)

    # Move down.
    world.robot_move(0, 1)
    assert world.robot_position == (1, 1)

    # Reset robot.
    world.robot_reset()
    assert world.robot_position == (0, 0)


def test_grid_world_robot_set_position():
    world = GridWorld()

    world.robot_set_position(
        2,
        3,
        animate=False,
    )

    assert world.robot_position == (2, 3)


def test_grid_world_custom_size():
    world = GridWorld(
        grid_size=8,
        grid_cell_size=50,
    )

    assert world.grid_size == 8
    assert world.grid_cell_size == 50

    world.robot_set_position(
        7,
        7,
        animate=False,
    )

    assert world.robot_position == (7, 7)


def test_grid_world_invalid_robot_position():
    world = GridWorld(grid_size=4)

    with pytest.raises(ValueError):
        world.robot_set_position(4, 0)

    with pytest.raises(ValueError):
        world.robot_set_position(0, 4)

    with pytest.raises(ValueError):
        world.robot_set_position(-1, 0)


def test_grid_world_invalid_size():
    with pytest.raises(ValueError):
        GridWorld(grid_size=0)

    with pytest.raises(ValueError):
        GridWorld(grid_size=-1)
