import sys
print(sys.argv)
def main():
    argv = sys.argv[1:]  # Exclude the script name from arguments
    num_args = len(argv)

    print("{}: {}".format(argv.index, num_args))
    print(":")
    
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()
