# import class from another file
from quote import Quote

# create an object of class Quote
q = Quote('The essence of good deeds and evil deeds is the same.'
        'They are both no more than a person\’s actions to make up for a defect in themselves.',
        'Gaku Yashiro', 491)
# try printing it
print(q)

# TODO
#   Read from 'quotes.list', into a list
#    Create a Quote object for each quote in list
#     Sort the list based on Quote.word_count
#      Print top 10 quotes 
