def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        result 
    finally:
        if result == 0:
            print("{}: {}".format("Inside result", None))
        else:
            print("{}: {}".format("Inside result", result))

