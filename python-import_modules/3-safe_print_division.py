def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        pass 
    finally:
        if b == 0:
            print("{}: {}".format("Inside result", None))
        elif result == 0:
            print("{}: {}".format("Inside result", 0.00))
        else:
            print("{}: {}".format("Inside result", result))

