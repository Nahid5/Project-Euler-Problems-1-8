"""
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""
import math


def theXthTriangle(x):      #generate the xth triangle
    return int ((x*(x+1))/2)

'''
#the tester
triangle = 1
counter = 0
for x in range (1, theXthTriangle(triangle)+1):
    if (theXthTriangle(triangle) % x == 0):
        counter += 1

print (counter)
print (triangle)
'''

numberOfDivisors = 40       #first number to have this many divisors
triangle = 1        #starts at triangle with 1 and counts by 1
counter = 0
while (counter < numberOfDivisors):
    counter = 0
    for x in range(1, theXthTriangle(triangle) + 1):
        if (theXthTriangle(triangle) % x == 0):     #used to get the number of divisors
            counter += 1
    if (counter < numberOfDivisors):        #if the triangle used did not have the number of divisors we wanted, increase by 1 to test new triangle
        triangle += 1
    else:
        break

print (triangle)