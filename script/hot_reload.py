"""
Hot Reload

Runs the Pygame application while allowing changes inside src/
to be patched into the running process without restarting.
"""

import sys
from pathlib import Path

import jurigged

# Project root
ROOT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT_DIR / "src"

# Add src/ to Python path
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


# Enable hot reload for the source directory
jurigged.watch(str(SRC_DIR))


# Import application entry point
from grid_4x4_robot.main import main

if __name__ == "__main__":
    print("🔥 Hot reload enabled")
    print(f"📁 Watching: {SRC_DIR}")

    main()
