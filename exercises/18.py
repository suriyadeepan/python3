# Dictionary
alphabets = {}
# add key-value pair
alphabets['a'] = 'Amanda Seyfried'
alphabets['b'] = 'Brooklyn Decker'
alphabets['c'] = 'Charlize Theron'
alphabets['d'] = 'Diane Kruger'
print(alphabets)

# 1. anything can be a value
# 2. anything can be a key, EXCEPT A LIST
capitals = { 1 : ['india', 'delhi'], 2 : ['usa', 'new york'], 3 : ['china', 'beijing']}
print(capitals)
# THIS WONT WORK
# capitals = { ['india', 'delhi'] : 1, ['usa', 'new york'] : 2, ['china', 'beijing'] : 3}

# Check if a key is in dictionary
if 'e' in alphabets:
    print(alphabets['e'])
else:
    print(alphabets['d'])

# get keys as list
print(alphabets.keys())
# get values as list
print(alphabets.values())

# remove from dictionary
del alphabets['d']

# TODO
#   Read from 'tex8_mini.dat', as a list of words (from previous exercise)
#    Create a dictionary that maps 'word' to index
#   
#   Sample input  : ['anarchism', 'originated', 'as', 'a', 'term', 'of', 'abuse', 'first', 'used', 'against'] 
#   Sample output : { 1 : 'anarchism', 2 : 'originated', 3 : 'as', 4 : 'a', 5 : 'term', 6 : 'of', 7 : 'abuse', 8 : 'first', 9 : 'used', 10 : 'against' }


# Tuples
#   Immutable lists
t = (1,2,'three',['four',5,6],'seven', (8,9,'ten'))

# t[0] = 3 doesn't work
# but t[3][0] = 4 will work

t1 = t + (11,12,13) # creates a new tuple
