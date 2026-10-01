import pygame

from grid_nxn_world.config import (
    CELL_SIZE,
    GRID_SIZE,
    ROBOT_BODY_COLOR,
    ROBOT_HEAD_COLOR,
)


class Robot:
    def __init__(self, grid_x=0, grid_y=0):
        # Logical grid coordinates (0 to 3)
        self.grid_x = grid_x
        self.grid_y = grid_y

        # Visual pixel coordinates (initialized to starting cell center)
        self.pixel_x = float(grid_x * CELL_SIZE + CELL_SIZE // 2)
        self.pixel_y = float(grid_y * CELL_SIZE + CELL_SIZE // 2)

        # Animation speed factor (0.2 means 20% of remaining distance per frame)
        self.speed = 0.25

    @property
    def position(self) -> tuple[int, int]:
        """Return the current logical grid coordinates as (x,y)"""
        return (self.grid_x, self.grid_y)

    def reset(self, grid_x: int = 0, grid_y: int = 0):
        """Reset logical and visual position to specified grid coordinates"""
        self.grid_x = max(0, min(GRID_SIZE - 1, grid_x))
        self.grid_y = max(0, min(GRID_SIZE - 1, grid_y))

        # Instantly sync visual pixel position to target cell center
        target_x, target_y = self._grid_to_pixel(self.grid_x, self.grid_y)
        self.pixel_x = float(target_x)
        self.pixel_y = float(target_y)

    def move(self, dx, dy):
        """Update logical grid target coordinates."""
        self.grid_x = max(0, min(GRID_SIZE - 1, self.grid_x + dx))
        self.grid_y = max(0, min(GRID_SIZE - 1, self.grid_y + dy))

    def update(self):
        """Smoothly slide visual position toward the current target grid cell."""
        target_x = self.grid_x * CELL_SIZE + CELL_SIZE // 2
        target_y = self.grid_y * CELL_SIZE + CELL_SIZE // 2

        # Linear interpolation (LERP)
        self.pixel_x += (target_x - self.pixel_x) * self.speed
        self.pixel_y += (target_y - self.pixel_y) * self.speed

    def draw(self, surface):
        # Use integer pixel coordinates for rendering
        center_x = int(self.pixel_x)
        center_y = int(self.pixel_y)

        radius = CELL_SIZE // 10
        robot_body_size = radius * 3

        # Head
        pygame.draw.circle(surface, ROBOT_HEAD_COLOR, (center_x, center_y - 10), radius)
        # Body
        pygame.draw.rect(
            surface,
            ROBOT_BODY_COLOR,
            (
                center_x - (robot_body_size // 2),
                center_y - 1,
                robot_body_size,
                robot_body_size,
            ),
            border_radius=5,
        )

    def _grid_to_pixel(self, gx: int, gy: int) -> tuple[int, int]:
        """Helper to compute cell center pixel coordinates from grid index."""
        cx = gx * CELL_SIZE + CELL_SIZE // 2
        cy = gy * CELL_SIZE + CELL_SIZE // 2
        return cx, cy
