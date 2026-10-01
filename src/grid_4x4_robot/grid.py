import pygame

from grid_4x4_robot.config import (
    CELL_SIZE,
    GRID_LINE_COLOR,
    GRID_SIZE,
    HIGHLIGHT_COLOR,
    TEXT_COLOR,
    WINDOW_SIZE,
)

# Lazy font initialization
_font = None


def _get_font():
    global _font
    if _font is None:
        _font = pygame.font.SysFont("arial", 12)
    return _font


def draw_grid(surface: pygame.Surface, active_cell: tuple[int, int] = None):
    # 1. Draw Active Cell Highlight
    if active_cell is not None:
        gx, gy = active_cell
        highlight_rect = pygame.Rect(
            gx * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE
        )
        pygame.draw.rect(surface, HIGHLIGHT_COLOR, highlight_rect)

    # 2. Draw Grid Lines
    for i in range(GRID_SIZE + 1):
        pos = i * CELL_SIZE
        pygame.draw.line(surface, GRID_LINE_COLOR, (pos, 0), (pos, WINDOW_SIZE), 2)
        pygame.draw.line(surface, GRID_LINE_COLOR, (0, pos), (WINDOW_SIZE, pos), 2)

    # 3. Draw Coordinate Labels
    font = _get_font()
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            label = font.render(f"{col},{row}", True, TEXT_COLOR)
            surface.blit(label, (col * CELL_SIZE + 8, row * CELL_SIZE + 6))
