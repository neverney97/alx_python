# creating a list of the arguments
argv = ["Hello", "Holberton", "School", 98, "Battery", "street"]

for i, argv in enumerate(argv, start=1):
    print("{}: {}".format(i, argv))
