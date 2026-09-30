# run_dev.py
import sys
from pathlib import Path

import hupper

src_dir = Path(__file__).resolve().parent / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

if __name__ == "__main__":
    reloader = hupper.start_reloader("grid_4x4_robot.main.main")

    # Watch every file and asset inside the src/ folder
    reloader.watch_files([str(p) for p in src_dir.rglob("*") if p.is_file()])
