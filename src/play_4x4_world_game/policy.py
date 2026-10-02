"""
Policy

1. Equiprobable Random Policy:
   each action has equal probability.
"""

from abc import ABC, abstractmethod

from play_4x4_world_game.environment import Action, GridWorld4x4


class Policy(ABC):
    """Abstract policy contract."""

    def __init__(self, env: GridWorld4x4):
        self._env = env

    @abstractmethod
    def probability(
        self,
        state: int,
        action: Action,
    ) -> float:
        """
        Return π(a | s):
        probability of taking action a in state s.
        """
        raise NotImplementedError


class EquiprobableRandomPolicy(Policy):
    def __init__(self, env: GridWorld4x4):
        super().__init__(env)

        self._action_probability = 1.0 / len(self._env.actions)

    def probability(
        self,
        state: int,
        action: Action,
    ) -> float:
        self._env.validate_state(state)
        self._env.validate_action(action)

        if self._env.is_terminal(state):
            return 0.0

        return self._action_probability
