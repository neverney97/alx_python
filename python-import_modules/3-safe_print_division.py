def safe_print_division(a, d):
    try:
        result = a/b
    except ZeroDivisionError:
        result =  None
    finally:
        print("{}: {}".format("Inside result", result))
        print("{} / {} = {}".format(a, b, result))

