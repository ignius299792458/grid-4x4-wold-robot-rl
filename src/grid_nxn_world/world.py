"""
Public facade for the NxN rendering world.

External code should interact with GridWorld only.

GridWorld exposes:
    grid_*   -> grid information
    robot_*  -> robot control
    render*  -> rendering control

RL concepts do not belong here.
"""

from grid_nxn_world.config import (
    DEFAULT_CELL_SIZE,
    DEFAULT_FPS,
    DEFAULT_GRID_SIZE,
    DEFAULT_WINDOW_TITLE,
)
from grid_nxn_world.grid import Grid
from grid_nxn_world.paint import Paint
from grid_nxn_world.robot import Robot


class GridWorld:
    def __init__(
        self,
        grid_size: int = DEFAULT_GRID_SIZE,
        grid_cell_size: int = DEFAULT_CELL_SIZE,
        robot_start_position: tuple[int, int] = (0, 0),
        render_fps: int = DEFAULT_FPS,
        render_title: str | None = None,
    ):
        self._validate_grid_size(grid_size)
        self._validate_grid_cell_size(grid_cell_size)

        self._grid_size = grid_size
        self._grid_cell_size = grid_cell_size

        self._robot_start_position = robot_start_position

        self._validate_grid_position(*robot_start_position)

        self._grid = Grid(
            size=self._grid_size,
            cell_size=self._grid_cell_size,
        )

        self._robot = Robot(
            grid_size=self._grid_size,
            cell_size=self._grid_cell_size,
            grid_x=robot_start_position[0],
            grid_y=robot_start_position[1],
        )

        if render_title is None:
            render_title = (
                f"{self._grid_size}x" f"{self._grid_size} " f"{DEFAULT_WINDOW_TITLE}"
            )

        self._paint = Paint(
            grid=self._grid,
            robot=self._robot,
            title=render_title,
            fps=render_fps,
        )

    # -------------------------
    # Grid
    # -------------------------

    @property
    def grid_size(self) -> int:
        return self._grid_size

    @property
    def grid_cell_size(self) -> int:
        return self._grid_cell_size

    @property
    def grid_pixel_size(self) -> int:
        return self._grid.pixel_size

    # -------------------------
    # Robot
    # -------------------------

    @property
    def robot_position(self) -> tuple[int, int]:
        return self._robot.position

    def robot_set_position(
        self,
        x: int,
        y: int,
        *,
        animate: bool = False,
    ) -> None:
        self._validate_grid_position(x, y)

        self._robot.set_position(
            x,
            y,
            animate=animate,
        )

    def robot_move(
        self,
        dx: int,
        dy: int,
    ) -> None:
        self._robot.move(dx, dy)

    def robot_reset(self) -> None:
        self._robot.reset(*self._robot_start_position)

    # -------------------------
    # Rendering
    # -------------------------

    def render(self) -> bool:
        """
        Render one frame.

        Usage:

            while world.render():
                pass
        """
        return self._paint.render(
            robot_move=self.robot_move,
            robot_reset=self.robot_reset,
        )

    def render_close(self) -> None:
        self._paint.close()

    # -------------------------
    # Validation
    # -------------------------

    def _validate_grid_position(
        self,
        x: int,
        y: int,
    ) -> None:
        if not (0 <= x < self._grid_size and 0 <= y < self._grid_size):
            raise ValueError(
                f"Grid position ({x}, {y}) "
                f"is outside the "
                f"{self._grid_size}x"
                f"{self._grid_size} grid."
            )

    @staticmethod
    def _validate_grid_size(
        size: int,
    ) -> None:
        if size <= 1:
            raise ValueError("grid_size must be greater than 1.")

    @staticmethod
    def _validate_grid_cell_size(
        cell_size: int,
    ) -> None:
        if cell_size <= 0:
            raise ValueError("grid_cell_size must be greater than 0.")

    def grid_set_terminal_positions(
        self,
        positions: tuple[tuple[int, int], ...],
    ) -> None:
        for x, y in positions:
            self._validate_grid_position(x, y)

        self._paint.set_terminal_cells(positions)

    def robot_trace_clear(self) -> None:
        self._paint.robot_trace_clear()

    def robot_trace_add(self) -> None:
        self._paint.robot_trace_add(self.robot_position)

    def render_load_goal_sound(
        self,
        path: str,
    ) -> None:
        self._paint.load_goal_sound(path)

    def render_play_goal_sound(self) -> None:
        self._paint.play_goal_sound()
