
from typing import TypeAlias


"""
Point Overlapping Triangle

"""

# TYPE ALIASES

T_X: TypeAlias = int | float
T_Y: TypeAlias = int | float
T_POINT: TypeAlias = tuple[T_X, T_Y], list[T_X, T_Y]
T_POSITION: TypeAlias = T_POINT

# DEFINE ALGORITHM

_sign = lambda p1, p2, p3: (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


def point_triangle(p: T_POINT, a: T_POSITION, b: T_POSITION, c: T_POSITION) -> bool:
    """_summary_

    Args:
        p (T_POINT): Point
        a (T_POSITION): A Position Triangle
        b (T_POSITION): B Position Triangle
        c (T_POSITION): C Position Triangle

    Returns:
        bool: True if Point overlapping With Triangle otherwise False
    """

    d = (_sign(p, a, b), _sign(p, b, c), _sign(p, c, a))

    return not (any(i < 0 for i in d) and any(j > 0 for j in d))



__dir__ = (
    "point_triangle",
)


__author__ = "Tooraj"
__email__ = "booleansfunction@Gmail.com"
