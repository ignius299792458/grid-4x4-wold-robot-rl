"""
Policy

1. Equiprobable Random Policy: each action has equal distribution of chance

"""

from play_4x4_world_game.environment import Action, GridWorld4x4


class EquiprobableRandomPolicy:
    def __init__(self, env: GridWorld4x4):
        self._env = env
        self._action_probability = 1.0 / len(env.actions)

    def probability(self, state: int, action: Action) -> float:
        self._env.validate_state(state)
        self._env.validate_action(action)

        if self._env.is_terminal(state):
            return 0.0
        return self._action_probability
