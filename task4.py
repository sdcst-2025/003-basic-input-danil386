#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

h = input("What is your cone's height?")
r = input("What is your cone's radius?")

h = float(h)
r = float(r)

import math
sa = (math.pi * r)*(r + (((h**2)+(r**2))**0.5))
sa = str(sa)

print("Your cone's surface are is " + sa)