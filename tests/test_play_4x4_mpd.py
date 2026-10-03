"""
Test:
    if written play_4x4_world_game/environment.py
    is holding Markov Decision Process or not
"""

from play_4x4_world_game.environment import Action, GridWorld4x4


def test_state_space():
    env = GridWorld4x4()

    assert env.states == tuple(range(16))
    assert env.terminal_states == frozenset({0, 15})


def test_state_position_mapping():
    env = GridWorld4x4()

    assert env.state_to_position(0) == (0, 0)
    assert env.state_to_position(5) == (1, 1)
    assert env.state_to_position(6) == (2, 1)
    assert env.state_to_position(15) == (3, 3)


def test_env_step():
    env = GridWorld4x4()

    # lower bound  (wall test)
    next_state, reward, terminated = env.step(0, Action.LEFT)
    assert next_state == 0
    assert reward == 0.0  # since terminal state
    assert terminated is True

    # normal
    next_state, reward, terminated = env.step(3, Action.DOWN)  # 3 -> down -> 7
    assert next_state == 7
    assert reward == -1.0
    assert terminated is False

    # normal boundry test (wall testing)
    next_state, reward, terminated = env.step(3, Action.RIGHT)  # 3 -> right -> 3
    assert next_state == 3
    assert reward == -1.0
    assert terminated is False

    # upper bound (wall testing)
    next_state, reward, terminated = env.step(15, Action.DOWN)
    assert next_state == 15
    assert reward == 0.0
    assert terminated is True


def test_env_3_steps_MDP():
    env = GridWorld4x4()

    first_state = 1
    first_action = Action.DOWN  # from 1 -> down -> 5
    next_state, reward, terminated = env.step(first_state, first_action)
    assert next_state == 5
    assert reward == -1.0
    assert terminated is False

    second_state = next_state  # 5 -> right -> 6
    second_action = Action.RIGHT
    next_state, reward, terminated = env.step(second_state, second_action)
    assert next_state == 6
    assert reward == -1.0
    assert terminated is False

    last_state = next_state  # 6 -> up -> 2
    last_action = Action.UP
    next_state, reward, terminated = env.step(last_state, last_action)
    assert next_state == 2
    assert reward == -1.0
    assert terminated is False
