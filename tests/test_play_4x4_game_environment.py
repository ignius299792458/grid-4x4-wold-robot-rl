from play_4x4_world_game.environment import GridWorld4x4


def test_state_space():
    env = GridWorld4x4()

    assert env.states == tuple(range(16))

    assert env.is_terminal(0)
    assert env.is_terminal(15)

    assert not env.is_terminal(5)
    assert not env.is_terminal(10)
