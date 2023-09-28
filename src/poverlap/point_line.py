
from math import sqrt, dist
from typing import TypeAlias


"""
Point Overlapping Line

"""

# TYPE ALIASES

T_X: TypeAlias = int | float
T_Y: TypeAlias = int | float
T_POINT: TypeAlias = tuple[T_X, T_Y], list[T_X, T_Y]
T_LINE: TypeAlias = tuple[T_POINT, T_POINT], list[T_POINT, T_POINT]

# DEFINE ALGORITHM

_sqr = lambda x: x ** 2
_l2 = lambda line: _sqr(line[0][0] - line[1][0]) + _sqr(line[0][1] - line[1][1])


def calculate(p: T_POINT, line: T_LINE) -> float:
    """Calculate Point Line

    Args:
        p (T_POINT): Point
        line (T_LINE): Line

    Returns:
        float: Sqrt Distance
    """

    t = ((p[0] - line[0][0]) * (line[1][0] - line[0][0]) + (p[1] - line[0][1]) * (line[1][1] - line[0][1])) / _l2(line)
    t = max(0, min(1, t))

    return sqrt( dist(p, ( line[0][0] + t * (line[1][0] - line[0][0]), line[0][1] + t * (line[1][1] - line[0][1]) )) )


def point_line(p: T_POINT, line: T_LINE) -> bool:
    """Point Overlapping Line

    Args:
        p (T_POINT): Point
        line (T_LINE): Line

    Returns:
        bool: True if overlapping Point with Line otherwise False
    """
    return calculate(p, line) < 1.0 


def point_line_add_area(p: T_POINT, line: T_LINE, active_distance: float = 0.0) -> bool:
    """Point Overlapping Line With Active Area Distance

    Args:
        p (T_POINT): Point
        line (T_LINE): Line
        active_distance (float, optional): Area Distance Must be Positive. Defaults to 0.0.

    Returns:
        bool: True if overlapping Point in Line or Added Area otherwise False
    """
    return calculate(p, line) < 1.0 + sqrt(active_distance)


__dir__ = (
    "point_line",
    "point_line_add_area",
    "calculate",
)


__author__ = "Tooraj"
__email__ = "booleansfunction@Gmail.com"
