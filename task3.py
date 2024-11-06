#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

a = input("What is your a value in ax+b=c?")
b = input("What is your b value in ax+b=c?")
c = input("What is your c value in ax+b=c?")

a = int(a)
b = int(b)
c = int(c)

x = (c - b)/a
x = str(x)

print("Your x value is " + x)