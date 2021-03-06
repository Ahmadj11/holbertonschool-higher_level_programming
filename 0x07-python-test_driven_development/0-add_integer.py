#!/usr/bin/python3
""" Add integers """


def add_integer(a, b=98):
    """ Add integers

    Args:
        a (int): [Mandatory int to pass in]
        b (int): [Optional int to pass in]
    Returns:
        int: [Sum of a and b]
    """
    try:
        if isinstance(a, int):
            pass
        elif isinstance(a, float):
            a = round(int(a), 0)
        else:
            raise TypeError
    except Exception:
        raise TypeError("a must be an integer")

    try:
        if isinstance(b, int):
            pass
        elif isinstance(b, float):
            b = round(int(b), 2)
        else:
            raise TypeError
    except Exception:
        raise TypeError("b must be an integer")

    return a + b
