def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    if len(s1) > len(s2):
        a = len(s2)
    else :
        a = len(s1)
    return a