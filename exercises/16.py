import math

# round up
print(math.ceil(4.3))
# round off
print(math.floor(4.3))
# TODO : 
#   Sample io : (4.3 -> 4), (4.6->5)

# area of semi circle, given r = 2.3
r = 2.3
area = lambda x : 0.5 * math.pi * (r**2)
print('math.pi : {}'.format(math.pi))
print(area(r))

# TODO:
#   find volume of a sphere
#       V = (4/3) * pi * (r^3)

# TODO:
#   Find the roots of a quadratic expression using math.sqrt
#       x1 = {-b + sqrt( b^2 - 4ac )}/ (2a)
#       x2 = {-b - sqrt( b^2 - 4ac )}/ (2a)
