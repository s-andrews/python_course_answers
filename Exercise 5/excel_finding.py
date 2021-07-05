#!python
from pathlib import Path

starting_dir = Path.home()

for excel in starting_dir.rglob("*.xlsx"):
    size = excel.stat().st_size
    print(f"{size}\t{str(excel)}")