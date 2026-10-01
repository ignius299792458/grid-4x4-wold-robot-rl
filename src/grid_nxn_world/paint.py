"""
Paint.py

This module handles renddering
"""

from collections.abc import Callable

import pygame

from grid_nxn_world.config import BG_COLOR
from grid_nxn_world.events import handle_events
from grid_nxn_world.grid import Grid
from grid_nxn_world.robot import Robot


class Paint:
    """Internal Pygame rendering controller."""

    def __init__(
        self,
        grid: Grid,
        robot: Robot,
        title: str,
        fps: int,
    ):
        self._grid = grid
        self._robot = robot

        self._title = title
        self._fps = fps

        self._surface: pygame.Surface | None = None
        self._clock: pygame.time.Clock | None = None

    def render(
        self,
        robot_move: Callable[[int, int], None],
        robot_reset: Callable[[], None],
    ) -> bool:
        """
        Process input and render one frame.

        Returns False when the window is closed.
        """
        self._open()

        running = handle_events(
            robot_move=robot_move,
            robot_reset=robot_reset,
        )

        if not running:
            self.close()
            return False

        self._robot.update()

        self._draw()

        return True

    def close(self) -> None:
        pygame.quit()

        self._surface = None
        self._clock = None

    def _open(self) -> None:
        if self._surface is not None:
            return

        pygame.init()

        window_size = self._grid.pixel_size

        self._surface = pygame.display.set_mode((window_size, window_size))

        pygame.display.set_caption(self._title)

        self._clock = pygame.time.Clock()

    def _draw(self) -> None:
        assert self._surface is not None
        assert self._clock is not None

        self._surface.fill(BG_COLOR)

        self._grid.draw(
            surface=self._surface,
            active_cell=self._robot.position,
        )

        self._robot.draw(self._surface)

        pygame.display.flip()

        self._clock.tick(self._fps)
