#!python
import math

# A script which calculates the distance and angle 
# between two points on a 2D plane.

# Start by seting the coordinates
x1 = 10
y1 = 10

x2 = 23
y2 = 36

# Calculate the distance between them.  This is a simple
# pythagorean calculation sqrt(x**2 + y**2)

hypotenuse = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))

# Calculate the angle.  Since this is a right sided 
# triangle and we know all of the lengths we can use
# any of sin/cos/tan to do the calculation.
#
# We'll use tan(x) = opposite/adjacent where opposite
# is change in y and adjacent is change in x, so the
# actual calculation is going to be atan(o/a)

angle = math.atan((y2-y1) / (x2-x1))

# From the documentation:
# >>> help(math.atan)
# Help on built-in function atan in module math:
#
# atan(x, /)
#     Return the arc tangent (measured in radians) of x.
#
#     The result is between -pi/2 and pi/2.
#
# So the result we get back is in radians, not degrees.  To 
# convert it we'll need to use another function from math.
#
# >>> help(math.atan)
# Help on built-in function atan in module math:
#
# atan(x, /)
#     Return the arc tangent (measured in radians) of x.
#
#     The result is between -pi/2 and pi/2.

angle = math.degrees(angle)


# Now we've done all of the calculations we can print the result

print ("Point1 x=",x1," y=",y1,sep="")
print ("Point2 x=",x2," y=",y2,sep="")

print ("Distance from p1 to p2 is",round(hypotenuse,2))
print ("Angle between p1 and p2 is",round(angle,2),"degrees")
