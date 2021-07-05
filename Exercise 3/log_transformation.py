#!python
import random
import math

# Build a 10 row list of lists
# We start with an empty list
linear_data = []

# We want to go through 10 times so we use a range
# but we don't actually need to know which iteration
# we're at so we use _ instead of a variable name to
# stop us getting warnings from our IDE about unused 
# variables.
# We append on an empty list to the starting list.
for _ in range(10):
    linear_data.append([])

# Now populate the 2D structure with random values 
# between 1 and 1,000,000

# Make an instance of the Random() data type (a random)
# number generator.  We need this so we can call the 
# methods we need.
r = random.Random()

# Iterate through the top level list
for x in range(10):
    # We need 10 values in each second level list
    for _ in range(10):
        linear_data[x].append(r.randint(1,1000000))

# Now we're going to build a second data structure from the
# first where all of the values are log transformed

log_data = []

# Iterate through the top level
for x in range(10):
    log_data.append([])
    # Iterate through the second level
    for y in range(10):
        log_data[x].append(round(math.log(linear_data[x][y]),1))

# Now print out the result. 
for i in range(len(log_data)):
    for j in range(len(log_data[i])):
        if j==0:
            print("") # Get a newline
        print(log_data[i][j]," ", end="")






