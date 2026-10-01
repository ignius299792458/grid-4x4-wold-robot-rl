import pygame

from grid_nxn_world.config import (
    ROBOT_ANIMATION_SPEED,
    ROBOT_BODY_COLOR,
    ROBOT_HEAD_COLOR,
)


class Robot:
    def __init__(
        self,
        grid_size: int,
        cell_size: int,
        grid_x: int = 0,
        grid_y: int = 0,
    ):
        self._grid_size = grid_size
        self._cell_size = cell_size
        self._speed = ROBOT_ANIMATION_SPEED

        self.grid_x = grid_x
        self.grid_y = grid_y

        pixel_x, pixel_y = self._grid_to_pixel(grid_x, grid_y)

        self.pixel_x = float(pixel_x)
        self.pixel_y = float(pixel_y)

    @property
    def position(self) -> tuple[int, int]:
        return self.grid_x, self.grid_y

    def set_position(
        self,
        grid_x: int,
        grid_y: int,
        *,
        animate: bool = False,
    ) -> None:
        self.grid_x = self._clamp(grid_x)
        self.grid_y = self._clamp(grid_y)

        if not animate:
            pixel_x, pixel_y = self._grid_to_pixel(
                self.grid_x,
                self.grid_y,
            )

            self.pixel_x = float(pixel_x)
            self.pixel_y = float(pixel_y)

    def move(self, dx: int, dy: int) -> None:
        self.grid_x = self._clamp(self.grid_x + dx)
        self.grid_y = self._clamp(self.grid_y + dy)

    def reset(self, grid_x: int = 0, grid_y: int = 0) -> None:
        self.set_position(
            grid_x,
            grid_y,
            animate=False,
        )

    def update(self) -> None:
        target_x, target_y = self._grid_to_pixel(
            self.grid_x,
            self.grid_y,
        )

        self.pixel_x += (target_x - self.pixel_x) * self._speed

        self.pixel_y += (target_y - self.pixel_y) * self._speed

    def draw(self, surface: pygame.Surface) -> None:
        center_x = int(self.pixel_x)
        center_y = int(self.pixel_y)

        radius = max(4, self._cell_size // 10)
        body_size = radius * 3
        head_offset = max(6, self._cell_size // 10)

        pygame.draw.circle(
            surface,
            ROBOT_HEAD_COLOR,
            (
                center_x,
                center_y - head_offset,
            ),
            radius,
        )

        pygame.draw.rect(
            surface,
            ROBOT_BODY_COLOR,
            (
                center_x - body_size // 2,
                center_y,
                body_size,
                body_size,
            ),
            border_radius=max(
                2,
                self._cell_size // 20,
            ),
        )

    def _grid_to_pixel(
        self,
        grid_x: int,
        grid_y: int,
    ) -> tuple[int, int]:
        pixel_x = grid_x * self._cell_size + self._cell_size // 2

        pixel_y = grid_y * self._cell_size + self._cell_size // 2

        return pixel_x, pixel_y

    def _clamp(self, value: int) -> int:
        return max(
            0,
            min(self._grid_size - 1, value),
        )
