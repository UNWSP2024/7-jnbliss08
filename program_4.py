# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 

import math

def main():
    coordinate1 = get_coordinate1()
    coordinate2 = get_coordinate2()
    dist = distance(coordinate1, coordinate2)
    print(f' The distance between points is: {dist}')

def get_coordinate1():
    while True:
        try:
            x = float(input('Enter first x coordinate: '))
            y = float(input('Enter first y coordinate: '))
            z = float(input('Enter first z coordinate: '))
            return (x, y, z)
        except ValueError:
            print('Please enter numeric values.')

def get_coordinate2():
    while True:
        try:
            x = float(input('Enter second x coordinate: '))
            y = float(input('Enter second y coordinate: '))
            z = float(input('Enter second z coordinate: '))
            return (x, y, z)
        except ValueError:
            print('Please enter numeric values.')

def distance(coordinate1, coordinate2):
    return math.sqrt((coordinate2[0] - coordinate1[0]) ** 2 +(coordinate2[1] - coordinate1[1]) ** 2 +(coordinate2[2] - coordinate1[2]) ** 2)

main()