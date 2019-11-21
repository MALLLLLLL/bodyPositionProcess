import math


def get_angle(d1, d2, d3):
    """ Get the angle bewteen point d1, d2, d3
        Use Cosine theorem
        input: tuple or list of the three coordinate
        output: the degree of ∠d1d2d3
    """
    x1, y1, x2, y2, x3, y3 = d1[0], d1[1], d2[0], d2[1], d3[0], d3[1]
    a = math.sqrt((x1-x2)**2+(y1-y2)**2)
    b = math.sqrt((x3-x2)**2+(y3-y2)**2)
    c_2 = ((x1-x3)**2+(y1-y3)**2)
    cos = (a**2 + b**2 - c_2) / (2 * a * b)
    return math.acos(cos) / math.pi * 180


def get_distance(d1, d2, d3):
    """ Get the distance between dot d1 and line d2-d3
        input: tuple or list of the three coordinate
        output: the distance between dot d1 and line d2-d3
    """
    x1, y1, x2, y2, x3, y3 = d1[0], d1[1], d2[0], d2[1], d3[0], d3[1]
    distance = abs((y2 - y3) * x1 - (x2 - x3) * y1 + (x2 * y3) - (y2 * x3)) / math.sqrt((y2 - y3) ** 2 + (x2 - x3) ** 2)
    return distance