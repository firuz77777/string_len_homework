def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    s=""
    if len(s1) % 2 == 1:
        s = s + "[s1,"
    if len(s1) % 2 == 0:
        s = s 
    if len(s2) % 2 == 1:
        s = s + "s2,"
    if len(s2) % 2 == 0:
        s = s 
    if len(s3) % 2 == 1:
        s = s + "s3]"
    if len(s3) % 2 == 0:
        s = s + "]" 
    return s
print(main("ekd","poppo","fgrwui"))