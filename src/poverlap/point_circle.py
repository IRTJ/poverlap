
from math import dist
from typing import TypeAlias


"""
Point Overlapping Circle

"""

# TYPE ALIASES

T_X: TypeAlias = int | float
T_Y: TypeAlias = int | float
T_POINT: TypeAlias = tuple[T_X, T_Y], list[T_X, T_Y]
T_POSITION: TypeAlias = T_POINT
T_RADIUS: TypeAlias = int |float

# DEFINE ALGORITHM

def circle_distance(p: T_POINT, circle_pos: T_POSITION, radius: T_RADIUS) -> float:
    """Distance Between Point and Circle

    Args:
        p (T_POINT): Point
        circle_pos (T_POSITION): Circle Position
        radius (T_RADIUS): Circle Radius

    Returns:
        float: distance point from circle
    """
    return dist(p, circle_pos) - radius


def point_circle(p: T_POINT, circle_pos: T_POSITION, radius: T_RADIUS) -> bool:
    """Point Overlapping Circle

    Args:
        p (T_POINT): Point
        circle_pos (T_POSITION): Center Position of Circle
        radius (T_RADIUS): Circle Radius

    Returns:
        bool: True if Point overlapping with Circle otherwise False
    """
    return dist(p, circle_pos) <= radius


def point_circle_add_area(p: T_POINT, circle_pos: T_POSITION, radius: T_RADIUS, active_distance: float = 0.0) -> bool:
    """Point Overlapping Circle With Active Area Distance

    Args:
        p (T_POINT): Point
        circle_pos (T_POSITION): Center Position of Circle
        radius (T_RADIUS): Circle Radius
        active_distance (float, optional): Area Distance Positive or Negative. Defaults to 0.0.

    Returns:
        bool: True if point Overlapping with Circle Active Area otherwise False
    """
    return dist(p, circle_pos) <= (radius + active_distance)





__dir__ = (
    "circle_distance",
    "point_circle",
    "point_circle_add_area",
)


__author__ = "Tooraj"
__email__ = "booleansfunction@Gmail.com"
