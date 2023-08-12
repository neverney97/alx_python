# creating a list of the arguments
if __name__ == "__main__":
    argv = ["Hello", "Holberton", "School", 98, "Battery", "street"]

    for i, argv in enumerate(argv, start=1):
        print("{}: {}".format(i, argv))
