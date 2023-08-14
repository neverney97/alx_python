# creating a function that removes characters c and C from a string.
def no_c(my_string):
    print(my_string.translate({ord(i): '' for i in 'Cc'}))
