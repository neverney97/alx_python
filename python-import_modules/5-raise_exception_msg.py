def raise_exception_msg(message):
    raise NameError()

    try:
        if message == "":
            raise NameError
    except NameError as ne:
        print(ne)
    else:
        print(message)