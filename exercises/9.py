i=0
while i<5:
    print('i= {}'.format(i))
    i += 1 # i = i + 1

# continue
j = 0
while j<20:
    j += 1
    if j % 3 == 0: # not(i%3)
        continue # by pass remaining statements
    print('j= {}'.format(j))

# break
k = 0
while 1: # infinite loop
    print('k= {}'.format(k**2)) # k**2 = k^2 = k*k
    k += 1
    if k >= 10:
        print('End loop as k = {}'.format(k))
        break

# Choose a prime number greater than 10 and print 10 multiples of it. 
