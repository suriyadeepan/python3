# List comprehension
#   [MAP]
#   build a list of 10 perfect squares
#       [ 1,4,9,16,25,36,49,64,81,100 ]
sq_list = [ i**2 for i in range(1,11) ]
print('List of perfect squares : {}'.format(sq_list))

# list of areas of circle if radius varies from 1 to 10
# using lambda : area = lambda x : 3.14 * (x**2)

# using a function
def area(r):
    pi = 3.14
    return pi * r * r

ca_list = [ area(x) for x in range(1,11) ]
print('Area variation : {}'.format(ca_list))

# Using condition to filter out elements from list
#   [FILTER]
#   Given : list of [ movie, rating ]
#       Filter out movie names that are rated less than 8
movie_list = [ ['Jagten',8.3], ['Memento',8.5], ['There will be Blood',8.1], ['Prestige',8.5], ['Dawn of the Dead',7.4], 
        ['300',7.7], ['Watchmen',7.7], ['Sucker Punch',6.1], ['Primer',7], ['Upstream Color',6.8], ['Time Crimes',7.2] ]
f_movie_list = [ movie[0] for movie in movie_list if movie[1] > 8 ]
print('Filtered list of movies : {}'.format(f_movie_list))

# TODO
#   [1] Given a list of words, return a list of words containing 'cat'
words = ['advocate', 'filibuster', 'allocate', 'closure', 'vacate', 'synthesis', 'syndicate', 'catalog', 'caught']
#   [2] Convert cat in each string, to UPPERCASE
#           output : ['advoCATe', 'filibuster', 'alloCATe', 'closure', 'vaCATe', 'synthesis', 'syndiCATe', 'CATalog', 'caught']
