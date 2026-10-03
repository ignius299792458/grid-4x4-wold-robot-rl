import matplotlib.pyplot as plt

ACTION_SYMBOLS = {
    "UP": "↑",
    "DOWN": "↓",
    "LEFT": "←",
    "RIGHT": "→",
}


def render_policy_and_values(values: dict[int, float], best_actions: dict[int, tuple]):
    fig, ax = plt.subplots(figsize=(6, 6))

    grid_size = 4

    # Draw empty grid
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_xticks(range(grid_size + 1))
    ax.set_yticks(range(grid_size + 1))
    ax.grid(True)
    ax.invert_yaxis()
    ax.set_aspect("equal")

    # Remove tick labels
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    for state in range(16):
        x = state % grid_size
        y = state // grid_size

        value_text = f"{values[state]:.1f}"

        if state in (0, 15):
            action_text = "T"
        else:
            symbols = [ACTION_SYMBOLS[action.name] for action in best_actions[state]]
            action_text = "/".join(symbols)

        # Write state id
        ax.text(
            x + 0.08,
            y + 0.20,
            f"s={state}",
            fontsize=9,
        )

        # Write value
        ax.text(
            x + 0.5,
            y + 0.45,
            value_text,
            ha="center",
            va="center",
            fontsize=11,
        )

        # Write best action(s)
        ax.text(
            x + 0.5,
            y + 0.78,
            action_text,
            ha="center",
            va="center",
            fontsize=14,
        )

    plt.title("Greedy Policy and State Values")
    plt.show()
