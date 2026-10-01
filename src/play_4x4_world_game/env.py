from grid_nxn_world import GridWorld

env = GridWorld()


def main() -> None:

    try:
        while env.render():
            pass

    finally:
        env.render_close()


if __name__ == "__main__":
    main()
