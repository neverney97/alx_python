def safe_print_division(a, d):
    return a/b

a = int(input())
b = int(input())

try:
    result = safe_print_division(a, b)
except ZeroDivisionError:
    print("None")
finally:
    print("{}: {}".format("Inside result", result))
    print("{} / {} = {}".format(a, b, result))

