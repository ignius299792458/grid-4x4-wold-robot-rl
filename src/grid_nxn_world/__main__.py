"""
Development entry point for grid_nxn_world.

Run with:

    python -m grid_nxn_world
"""

from grid_nxn_world.world import GridWorld


def main() -> None:
    world = GridWorld()

    try:
        while world.render():
            pass

    finally:
        world.render_close()


if __name__ == "__main__":
    main()
