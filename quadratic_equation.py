from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        return (int(root1), int(root2))
