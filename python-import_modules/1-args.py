import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name from arguments
    num_args = len(argv)

    print("Number of argument{}: {}".format("s" if num_args != 1 else "", num_args))
    print(":")
    
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()
