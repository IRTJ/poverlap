
from math import dist
from typing import TypeAlias


"""
Point Overlapping Point

"""

# TYPE ALIASES

T_X: TypeAlias = int | float
T_Y: TypeAlias = int | float
T_POINT: TypeAlias = tuple[T_X, T_Y], list[T_X, T_Y]


# DEFINE ALGORITHM

def point_distance(pa: T_POINT, pb: T_POINT) -> float:
    """Distance Between Tow Points

    Args:
        pa (T_POINT): Point 1
        pb (T_POINT): Point 2

    Returns:
        float: distance of points
    """
    return dist(pa, pb)


def point_point(pa: T_POINT, pb: T_POINT) -> bool:
    """Point Overlapping Point With Position Algorithm

    Args:
        pa (T_POINT): Point 1
        pb (T_POINT): Point 2

    Returns:
        bool: True x1 position and y1 position must equal x2 and y2 otherwise False
    """
    return (pa[0] == pb[0]) and (pa[1] == pb[1])


def point_point_add_area(pa: T_POINT, pb: T_POINT, active_distance: float = 0.0) -> bool:
    """Point Overlapping Point With Check Distance Algorithm

    Args:
        pa (T_POINT): Point 1
        pb (T_POINT): Point 2
        active_distance (float): default [0.0] Must be Positive Number - Distance of Point1 Trigger True Must be Positive Number

    Returns:
        bool: True distance between tow points smaller equal than active_distance otherwise False
    """
    return dist(pa, pb) <= active_distance


__dir__ = (
    "point_distance",
    "point_point",
    "point_point_add_area",
)


__author__ = "Tooraj"
__email__ = "booleansfunction@Gmail.com"
