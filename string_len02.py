def main(a):
    """
    A string type variable is given. Return True if its length is even. Return False if its length is odd.
    Args:
        a: string
    Returns:
        True or False
    """
    w = len(a)
    if w % 2 == 0:
        q = True
    if w % 2 == 1:
        q = False
    return q