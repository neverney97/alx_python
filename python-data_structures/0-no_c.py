# creating a function that removes characters c and C from a string.
def no_c(my_string):
    my_string.translate({ord(i): None for i in 'Cc'})

