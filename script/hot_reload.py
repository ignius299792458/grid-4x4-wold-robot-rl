"""
Hot Reload

Runs the GridWorld application while allowing Python source
changes inside src/ to be patched into the running process.
"""

import sys
from pathlib import Path

import jurigged

# Project directories
ROOT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT_DIR / "src"


# Make src/ importable
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


# Watch source code for live changes
jurigged.watch(str(SRC_DIR))


from grid_nxn_world.paint import main

if __name__ == "__main__":
    print("🔥 Hot reload enabled")
    print(f"📁 Watching: {SRC_DIR}")

    main()
