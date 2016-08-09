# slicing : list[low:high:stride] (note : stride is optional)
ilist = [0,1,2,3,4,5,6,7,8,9] # also, ilist = list(range(10))

print(ilist[:5])
print(ilist[5:])
print(ilist[:]) # = ilist = ilist[::]
print(ilist[1:5])
print(ilist[3:7])

# stride
print(ilist[::2]) # 0,2,4,6,8
print(ilist[::3]) 
print(ilist[1::3]) 
print(ilist[1:7:3]) 
print(ilist[:7:3]) 

# get element by index
print(ilist[4])


# Try the above with mystr
mystr = 'el psy congroo'

print(mystr[:5])
print(mystr[5:])
print(mystr[:]) # = mystr = mystr[::]
print(mystr[1:5])
print(mystr[3:7])

# stride
print(mystr[::2]) # 0,2,4,6,8
print(mystr[::3]) 
print(mystr[1::3]) 
print(mystr[1:7:3]) 
print(mystr[:7:3]) 

# get element by index
print(mystr[4])

# now that you've mastered slicing, lets solve a few problems
# TODO : 
#   1. Create a list of your batch mates' names with first and last names separated by space. 
#       Sample Input : [ 'Yuno Gasai','Aru Akise','Yukiteru Amano,'Minene Uryu' ]
#       Output       : [ 'Yuno G', 'Aru A', 'Yuikiteru A', 'Minene U' ]
