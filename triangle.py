def is_triangle(a, b, c):
    """
    Checks whether three values can form a valid triangle.
    :param a: side a
    :param b: side b
    :param c: side c
    :return: True if valid triangle, False otherwise
    """

    # All sides must be positive
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Triangle inequality rule
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False

    return True
