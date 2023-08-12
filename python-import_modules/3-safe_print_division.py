def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        if b == 0:
            result = None
        print("Inside result: {}".format(result))


