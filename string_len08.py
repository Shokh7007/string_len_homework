def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    l=len(s)//2
    if len(s)%2==1:
        return s[l]
    else:
        return s[l-1:l+1]
print(main("diyora")) 