# vanilla sorting
mystr = 'freedom and the future of the internet'
mylist= mystr.split(' ')
mylist.sort() # inplace or mylist = sorted(mylist)
print(mylist)

# sorting using custom key
#   lets try sorting based on length of words
print(sorted(mylist,key=len)) # or mylist.sort(key=len)
#   what if i need it in decending order
print(sorted(mylist,key=len,reverse=True)) # or mylist.sort(key=len, reverse=True)

# using user defined function as key
#   Define key with lambda; very handy here
yalist = [ ['apple', 4], ['oragne',7], ['mango',23], ['potato',1], ['banana',19] ]
yalist.sort(key= lambda x : x[1], reverse=True)
print(yalist)

# alternative
def get_count(item):
    return item[1]

yalist.sort(key= get_count)
print(yalist)

# Sort the list of names of your batchmates based on the 2rd character in the name
