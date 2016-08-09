class Quote(object):

    def __init__(self, text, author, likes):
        self.text = text
        self.author = author
        self.likes = likes

    def __str__(self):
        return '{0}\n~ {1}\n\nLiked by {2} people\n'.format(self.text,self.author,self.likes)

    def word_count(self):
        # TODO
        # fill this up
        return
