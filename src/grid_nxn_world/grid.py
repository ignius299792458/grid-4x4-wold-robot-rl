import pygame

from grid_nxn_world.config import (
    GRID_LINE_COLOR,
    HIGHLIGHT_COLOR,
    ROBOT_TRACE_COLOR,
    ROBOT_TRACE_POINT_RADIUS,
    TERMINAL_CELL_COLOR,
    TEXT_COLOR,
)


class Grid:
    def __init__(self, size: int, cell_size: int):
        self._size = size
        self._cell_size = cell_size
        self._font = None

    @property
    def size(self) -> int:
        return self._size

    @property
    def cell_size(self) -> int:
        return self._cell_size

    @property
    def pixel_size(self) -> int:
        return self._size * self._cell_size

    def draw(
        self,
        surface: pygame.Surface,
        active_cell: tuple[int, int] | None = None,
        terminal_cells: tuple[tuple[int, int], ...] = (),
        robot_trace: tuple[tuple[int, int], ...] = (),
    ) -> None:

        self._draw_active_cell(
            surface,
            active_cell,
        )

        self._draw_terminal_cells(
            surface,
            terminal_cells,
        )

        self._draw_robot_trace(
            surface,
            robot_trace,
        )

        self._draw_lines(surface)
        self._draw_coordinates(surface)

    def _draw_active_cell(
        self,
        surface: pygame.Surface,
        active_cell: tuple[int, int] | None,
    ) -> None:
        if active_cell is None:
            return

        x, y = active_cell

        rect = pygame.Rect(
            x * self._cell_size,
            y * self._cell_size,
            self._cell_size,
            self._cell_size,
        )

        pygame.draw.rect(surface, HIGHLIGHT_COLOR, rect)

    def _draw_lines(self, surface: pygame.Surface) -> None:
        for i in range(self._size + 1):
            position = i * self._cell_size

            pygame.draw.line(
                surface,
                GRID_LINE_COLOR,
                (position, 0),
                (position, self.pixel_size),
                2,
            )

            pygame.draw.line(
                surface,
                GRID_LINE_COLOR,
                (0, position),
                (self.pixel_size, position),
                2,
            )

    def _draw_coordinates(self, surface: pygame.Surface) -> None:
        font = self._get_font()

        for row in range(self._size):
            for column in range(self._size):
                label = font.render(
                    f"{column},{row}",
                    True,
                    TEXT_COLOR,
                )

                surface.blit(
                    label,
                    (
                        column * self._cell_size + 8,
                        row * self._cell_size + 6,
                    ),
                )

    def _draw_terminal_cells(
        self,
        surface: pygame.Surface,
        terminal_cells: tuple[tuple[int, int], ...],
    ) -> None:
        font = pygame.font.SysFont(
            "arial",
            max(16, self._cell_size // 5),
            bold=True,
        )

        for x, y in terminal_cells:
            rect = pygame.Rect(
                x * self._cell_size,
                y * self._cell_size,
                self._cell_size,
                self._cell_size,
            )

            # Terminal-cell background
            pygame.draw.rect(
                surface,
                TERMINAL_CELL_COLOR,
                rect,
            )

            # GOAL label
            label = font.render(
                "GOAL",
                True,
                TEXT_COLOR,
            )

            label_rect = label.get_rect(center=rect.center)

            surface.blit(
                label,
                label_rect,
            )

    def _draw_robot_trace(
        self,
        surface: pygame.Surface,
        robot_trace: tuple[tuple[int, int], ...],
    ) -> None:
        if not robot_trace:
            return

        points = [
            (
                x * self._cell_size + self._cell_size // 2,
                y * self._cell_size + self._cell_size // 2,
            )
            for x, y in robot_trace
        ]

        if len(points) >= 2:
            pygame.draw.lines(
                surface,
                ROBOT_TRACE_COLOR,
                False,
                points,
                3,
            )

        for point in points:
            pygame.draw.circle(
                surface,
                ROBOT_TRACE_COLOR,
                point,
                ROBOT_TRACE_POINT_RADIUS,
            )

    def _get_font(self) -> pygame.font.Font:
        if self._font is None:
            self._font = pygame.font.SysFont("arial", 12)

        return self._font
