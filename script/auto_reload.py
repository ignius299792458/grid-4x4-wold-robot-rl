"""
Auto Reload

Cold-restarts the application when files inside src/ change.
"""

import sys
from pathlib import Path

import hupper

# Project directories
ROOT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT_DIR / "src"


# Make src/ importable
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


if __name__ == "__main__":
    print("♻️ Auto reload enabled")
    print(f"📁 Watching: {SRC_DIR}")

    reloader = hupper.start_reloader("grid_nxn_world.__main__.main")

    reloader.watch_files([str(path) for path in SRC_DIR.rglob("*") if path.is_file()])
