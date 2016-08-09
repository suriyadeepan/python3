# Functions
#  cube(a) : return a*a*a
def cube(a):
    return a*a*a

a = 3.0
print('Cube of {0} is {1}'.format(a,cube(a)))

# find the area of a circle
def area_of_circle(r):
    pi = 3.14
    return pi * r * r # or pi * (r**2)

r = 7.0
print('Area of circle with radius {0} is {1}'.format(r,area_of_circle(r)))

# positional arguments
#   find the area of a rectangle
def area_of_rect(a,b):
    return a*b
a,b = 2,3
print('Area of rectangle with dimensions {0}x{1} is {2}'.format(a,b,area_of_rect(a,b)))

# TODO
#   Given a domain name and number of pages, return a list of urls of given format.
#   sample input : 'www.example.com', 5
#   sample output : [  'www.example.com/?page=1',
#                      'www.example.com/?page=2',
#                      'www.example.com/?page=3',
#                      'www.example.com/?page=4',
#                      'www.example.com/?page=5'  ]
def get_urls(domain, page_count):
    # write your code here
    return

# Default arguments
#   power function (base, radix)
def pow(b,r=2):
    return b**r

x = pow(2)
y = pow(2,3)
z = pow(2,r=4)
print('x (2^2) : {0}, y (2^3) : {1}, z (2^4) : {2}'.format(x,y,z)) 

# A Special function : lambda => substitute a variable with an expression
#   Write cube, area_of_circle, area_of_rect, pow as lambda
lamb_cube = lambda x : x**3
lamb_circ_area = lambda x : 3.14 * (x**2)
lamb_rect_area = lambda x,y : x*y
lamb_pow = lambda x,y : x**y

print(lamb_cube(2))
print(lamb_circ_area(2))
print(lamb_rect_area(2,3))
print(lamb_pow(2,3))

# long or not
lornot = lambda x : len(x) > 10
print(lornot('hello world!')) 

# TODO
# 2. Write a lambda function that'll return True for odd numbers 
# 3. Wrap the previously written lambda in a function to return a list of odd numbers from a list of numbers
