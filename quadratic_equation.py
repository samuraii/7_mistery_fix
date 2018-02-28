from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    # Если дискриминант меньше нуля, то корней нет
    if discriminant < 0:
        return None, None

    # Вычисляем корни по формуле
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)

    # Если дискриминант равен нулю, то корень один
    # Иначе уравнение имеет два корня
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
