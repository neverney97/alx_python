def safe_print_division(a, b):
    try:
        if ZeroDivisionError:
            result = None
        else:
            result = a/b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))


