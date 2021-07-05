#!python
from pathlib import Path
import re

base_folder = Path("c:/Users/andrewss/Desktop/Introduction to Python/Python Intro Data/Mapping Stats")

for file in base_folder.iterdir():
    short_name = re.sub("_GRCm38.*$","",file.name)

    with open(file) as fh:
        for line in fh:
            hit = re.search("(\d+\.\d+)%.*aligned exactly 1 time",line)
            if hit is not None:
                print(short_name+"\t"+hit.groups()[0])
                break

