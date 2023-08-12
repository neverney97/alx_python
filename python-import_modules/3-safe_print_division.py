def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        pass 
    finally:
        if a == 0 or b == 0:
            print("{}: {}".format("Inside result", None))
        else:
            print("{}: {}".format("Inside result", result))

