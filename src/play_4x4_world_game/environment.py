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


class GridWorld4x4:
    GRID_SIZE = 4
    STATES_CARDINALITY = GRID_SIZE * GRID_SIZE

    def __init__(self):
        self.states = tuple(range(self.STATES_CARDINALITY))
        self.terminal_states = frozenset({0, 15})

    def is_terminal(self, state: int) -> bool:
        """Return true if state is terminal"""
        return state in self.terminal_states

    def _validate_state(self, state: int) -> None:
        """Ensure state belongs to the environment"""
        if state not in self.states:
            raise ValueError(
                f"State {state} is outside"
                f"the valid value range 0-{self.STATES_CARDINALITY-1}"
            )
