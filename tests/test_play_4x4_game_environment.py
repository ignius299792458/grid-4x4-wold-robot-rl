from play_4x4_world_game.environment import Action, GridWorld4x4


def test_state_space():
    env = GridWorld4x4()

    assert env.states == tuple(range(16))

    assert env.is_terminal(0)
    assert env.is_terminal(15)

    assert not env.is_terminal(5)
    assert not env.is_terminal(10)


def test_action_space():
    env = GridWorld4x4()

    assert env.actions == tuple(Action)

    assert Action.UP.value == (0, -1)
    assert Action.DOWN.value == (0, 1)
    assert Action.LEFT.value == (-1, 0)
    assert Action.RIGHT.value == (1, 0)
