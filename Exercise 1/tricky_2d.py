#!python
import random
import math

# This script takes in an x,y position and a distance
# and calculates a random point which falls that 
# distance from the original xy

# Let's start by collecting the data

start_x = input("Staring x position: ")
start_y = input("Staring y position: ")
distance = input("Distance to other point: ")

# Convert the inputs to numbers

start_x = float(start_x)
start_y = float(start_y)
distance = float(distance)


# Now we need to find the new xy position.  There
# are a few different ways to do this.  The one
# which I think is easiest to implement fairly is
# that we select a random angle between 0 and 360
# (or 0 to 2pi rads) and then calculate the position
# up that angle

# To generate the random number we need to look in the
# random package.  The two relevant bits are:
# 
# class Random(_random.Random)
#   Random(x=None)
#
#   Random number generator base class used by bound 
#   module functions.
#
#   Used to instantiate instances of Random to get 
#   generators that don't share state.

# So the random package defines a Random class (data type)
# which is then used to call methods.

# uniform(self, a, b)
#   Get a random number in the range [a, b) or [a, b] 
#   depending on rounding.

# There is then a uniform method which we can use to
# make a selection from a range we supply.

angle = random.Random().uniform(0,360)

# Now we've got the angle we can use conventional
# trigonometry to work out the x and y distances, 
# given that we know the hypotenuse distance.

# We need the angle to be in radians
angle_rad = math.radians(angle)

y_dist = distance * math.sin(angle_rad)
x_dist = distance * math.cos(angle_rad)

end_x = start_x + x_dist
end_y = start_y + y_dist

# Now we have all of the calculations done we can 
# print out the results.

print("Input Data\n==========")

print("Start X=",start_x, sep="")
print("Start Y=",start_y, sep="")
print("Distance=",distance,sep="")

print("\nCalculated Output\n=================")
print(f"Random angle={int(angle)}")
print(f"x dist={round(x_dist,1)}")
print(f"y dist={round(y_dist,1)}")
print(f"Final x={round(end_x,1)}")
print(f"Final y={round(end_y,1)}")



