names = 'Bruce Wayne,Arthur Curry,Martha Kent'
# replace ',' with newline character
print(names.replace(',','\n'))
# replace Kent with Wayne
#
# find the position of 'Kent' in names
print(names.find('Kent'))
# convert string to lowercase
print(names.lower())
# check if two strings are equal; ignore case
s1 = 'Hello'
s2 = 'hello'
print(s1.lower() == s2.lower())

print('Lengths : {0}, {1}'.format(len(s1),len(s2)))
# Print the lengths of names of your batch mates
