# list of integers
# Note : DONOT USE 'list' AS NAME OF YOUR VARIABLE
ilist = [ 1,2,3,4,5,6 ]
# print odd numbers
for item in ilist: # item is an arbitrary name
    if item % 2: # or (item % 2 != 0)
        print(item)

# list of strings
slist = ['Freedom', 'and', 'the', 'future', 'of', 'the', 'internet']
# replace 'e' with 3, 'o' with 0
for word in slist: # again word is user defined
    print(word.replace('e','3').replace('o','0'))

# list can hold data of different types
hlist = [1, 'two', 3, 'four', 5]
print('hybrid list : {}'.format(hlist))

# a list can even hold another list as one of its elements
mlist = [ 'six', 7, [ 'eight', 9, 'ten'], 11, 'twelve']
print(mlist)
# more nesting
nlist = [ hlist, mlist, True, 'and more' ]
print(nlist)

# add to list
yalist = [ 'i', 'am', 'running' ]
print(yalist)
yalist.append('out')
print(yalist)
yalist.extend( ['of', 'words'] )
print(yalist)
sublist = ['now', 'iam', 'done' ]
yalist = yalist + sublist
print(yalist)

# convert list to string
#   delimiter.join(list)
yastring = ' '.join(yalist)
print(yastring)
# convert string back to list
#   using ' ' as delimiter
print(yastring.split(' '))

# insert into list
#   list.insert(index, element)
# TODO : insert '.' to indicate sentence completion, print as string

# find index of element in list
idx_of_am = yalist.index('am')
print('"am" is at position {}, in yalist'.format(idx_of_am))


# TODO : Print the batch mates' names which are longer than yours
