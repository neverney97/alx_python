def safe_print_division(a, b):
    try:
        if b != 0:
            result = a / b
        else:
            result is None
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))


