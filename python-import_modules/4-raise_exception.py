def raise_exception():
    try:
        raise raise_exception()
    except TypeError as te:
        print("Exception has been raised")
