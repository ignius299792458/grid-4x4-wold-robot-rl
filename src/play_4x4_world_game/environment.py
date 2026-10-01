"""
RL environment

This module defines the mathematical 4x4 gridworld:

    - state space
    - terminal states
    - action space
    - transition dynamics
    - rewards

Rendering does not belong here.
"""

from enum import Enum


class Action(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
    def dx(self) -> int:
        return self.value[0]

    @property
    def dy(self) -> int:
        return self.value[1]


class GridWorld4x4:
    GRID_SIZE = 4
    STATES_CARDINALITY = GRID_SIZE * GRID_SIZE

    def __init__(self):
        self.states = tuple(range(self.STATES_CARDINALITY))
        self.terminal_states = frozenset({0, 15})
        self.actions = tuple(Action)

    def transition(self, state: int, action: Action) -> int:
        """
        Return the next state produced by taking action in state.

        Movement is deterministic.

        If the action would leave the grid,
        the agent remains in the same state.
        """
        self._validate_state(state)
        self._validate_action(action)

        # if terminal state
        if self.is_terminal(state):
            return state

        x, y = self._state_to_position(state)
        next_x = x + action.dx
        next_y = y + action.dy

        if not self._is_valid_position(next_x, next_y):
            return state

        return self._position_to_state(next_x, next_y)

    def _state_to_position(self, state: int) -> tuple[int, int]:
        """Convert state number to (x, y) grid coordinates."""
        x = state % self.GRID_SIZE
        y = state // self.GRID_SIZE

        return x, y

    def _position_to_state(self, x: int, y: int) -> int:
        """Convert (x, y) grid coordinates to state number."""
        return x + self.GRID_SIZE * y

    def is_terminal(self, state: int) -> bool:
        """Return True if state is terminal."""
        self._validate_state(state)
        return state in self.terminal_states

    # ----------------------------------------
    # VALIDATES
    # ----------------------------------------

    def _is_valid_position(self, x: int, y: int) -> bool:
        """Return True if position lies inside the grid."""
        return 0 <= x < self.GRID_SIZE and 0 <= y < self.GRID_SIZE

    def _validate_state(self, state: int) -> None:
        """Ensure state belongs to the environment."""
        if state not in self.states:
            raise ValueError(
                f"State {state} is outside "
                f"the valid value range 0-{self.STATES_CARDINALITY - 1}."
            )

    def _validate_action(self, action: Action) -> None:
        """Ensure action belongs to the action space."""
        if not isinstance(action, Action):
            raise ValueError(f"{action!r} is not a valid Action.")
