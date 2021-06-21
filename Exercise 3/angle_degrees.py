#!python
import math

# We use a simple range to go through the integers
# up to 1800
for degree in range(1800):
    # We need to convert to radians from the original
    # degrees when performing the test
    if abs(math.sin(math.radians(degree))) < 0.01:
        print("sin",degree,"is zero(ish)")