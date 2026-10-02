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


def test_valid_transitions():
    env = GridWorld4x4()

    assert env.transition(5, Action.RIGHT) == 6
    assert env.transition(5, Action.LEFT) == 4
    assert env.transition(5, Action.UP) == 1
    assert env.transition(5, Action.DOWN) == 9


def test_boundary_transitions():
    env = GridWorld4x4()

    assert env.transition(3, Action.RIGHT) == 3
    assert env.transition(7, Action.RIGHT) == 7
    assert env.transition(12, Action.LEFT) == 12
    assert env.transition(13, Action.DOWN) == 13


def test_transition_into_terminal_state():
    env = GridWorld4x4()

    assert env.transition(1, Action.LEFT) == 0
    assert env.transition(14, Action.RIGHT) == 15


def test_terminal_state_is_absorbing():
    env = GridWorld4x4()

    for action in env.actions:
        assert env.transition(0, action) == 0
        assert env.transition(15, action) == 15
