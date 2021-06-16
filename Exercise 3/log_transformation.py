#!python
import random
import math

# Build a 10 row list of lists

linear_data = []

for _ in range(10):
    linear_data.append([])

# Now populate it with random values between 1 and 1,000,000
r = random.Random()

for x in range(10):
    for _ in range(10):
        linear_data[x].append(r.randint(1,1000000))

# Now we're going to build a second data structure from the
# first where all of the values are log transformed

log_data = []
for x in range(10):
    for y in range(10):
        if y==0:
            log_data.append([])

        log_data[x].append(round(math.log(linear_data[x][y]),1))

# Now print out the result
for i in range(len(log_data)):
    print(log_data[i])






