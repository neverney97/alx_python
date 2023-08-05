for i in range(10):
    for j in range(i + 1, 90):
        print("{:02d}".format(i) + ", " + "{:02d}".format(j), end="\n" if i == 8 and j == 9 else ", ")
