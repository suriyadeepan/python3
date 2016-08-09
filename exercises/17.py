# File Operations
#   Write to file
#       NOTE : NEVER USE file AS A VARIABLE
file_handle  = open('log.txt','w') # create a new file and opens it
file_handle.write('First line')
file_handle.write('Same line')
file_handle.write('\nSecond Line')
file_handle.close()
# open log.txt in gedit

# shorthand
with open('log.txt', 'a') as f: # notice 'a' : append
    f.write('\nMore lines') # 'w' will overwrite
    f.write('\nEven more lines') # no need to explicitly close file

# TODO
#   Write the names of your batch mates, followed by the lengths of their names, to a file, one per line.
#       format : Laina Walker, 11
#                Emma Kathrine, 12
#                ...

#   Read from file 'quotes.list'
with open('quotes.list','r') as f:
    content = f.read()

lines = content.split('\n')[:-1]
print(lines[:10],lines[-10:])
print(len(lines))

# TODO
#   Print top ten most liked quotes, line by line

# TODO 
#   Read from 'text8_mini.dat'; Extract content into a list of words
