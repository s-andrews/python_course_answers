#!python
import math

for degree in range(360):
    if abs(math.tan(math.radians(degree))) < 0.01:
        print("sin",degree,"is zero(ish)")