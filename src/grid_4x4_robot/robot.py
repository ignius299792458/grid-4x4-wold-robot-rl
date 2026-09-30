import pygame

from grid_4x4_robot.config import (
    CELL_SIZE,
    GRID_SIZE,
    ROBOT_BODY_COLOR,
    ROBOT_HEAD_COLOR,
)


class Robot:
    def __init__(self, grid_x=0, grid_y=0):
        # Grid coordinates (0 to GRID_SIZE - 1)
        self.grid_x = grid_x
        self.grid_y = grid_y

    def move(self, dx, dy):
        """Move robot by (dx, dy) while remaining strictly within board boundaries."""
        print(f"current position: grid_x: {self.grid_x}, grid_y: {self.grid_y}")

        # print(f"grid_x : max(0, min({GRID_SIZE - 1}, {self.grid_x + dx}))") # reverse

        # print(f"grid_x : min({GRID_SIZE - 1}, max(0, {self.grid_x + dx}))")
        self.grid_x = min(GRID_SIZE - 1, max(0, self.grid_x + dx))

        # print(f"grid_y : max(0, min({GRID_SIZE - 1}, {self.grid_y + dx}))") # reverse

        # print(f"grid_y : min({GRID_SIZE - 1}, max(0, {self.grid_y + dy}))")
        self.grid_y = min(GRID_SIZE - 1, max(0, self.grid_y + dy))
        print(f"next position: grid_x: {self.grid_x}, grid_y: {self.grid_y}\n")

    def draw(self, surface):
        # Calculate pixel coordinates for current cell center
        center_x = self.grid_x * CELL_SIZE + CELL_SIZE // 2
        center_y = self.grid_y * CELL_SIZE + CELL_SIZE // 2

        # Proportion dimensions relative to CELL_SIZE
        radius = CELL_SIZE // 10  # 10px
        body_size = radius * 3  # 30px

        # Offsets for balanced centering
        head_center_y = center_y - (radius + 2)
        body_top_y = center_y - 2
        body_left_x = center_x - (body_size // 2)

        # 1. Head
        pygame.draw.circle(surface, ROBOT_HEAD_COLOR, (center_x, head_center_y), radius)

        # 2. Body
        pygame.draw.rect(
            surface,
            ROBOT_BODY_COLOR,
            (body_left_x, body_top_y, body_size, body_size),
            border_radius=5,
        )
