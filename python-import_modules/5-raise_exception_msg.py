def raise_exception_msg(message="C is fun"):
    raise NameError()

    try:
        message
        raise_exception_msg(message)
    except NameError as ne:
        print(ne)