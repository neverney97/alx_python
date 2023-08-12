# creating a list of the arguments
if __name__ == "__main__":
    argv = []

    for i, argv in enumerate(argv, start=1):
        if i == 0:
            print("0 arguments")
        else:
            print("{}: {}".format(i, argv))
            
