
from typing import TypeAlias


"""
Point Overlapping Polygon

"""

# TYPE ALIASES

T_X: TypeAlias = int | float
T_Y: TypeAlias = int | float
T_POINT: TypeAlias = tuple[T_X, T_Y], list[T_X, T_Y]
T_POSITION: TypeAlias = T_POINT
T_POLYGON: TypeAlias = tuple[T_POSITION], list[T_POSITION]

# DEFINE ALGORITHM

_is_inside = lambda point, vp1, vp2: (
        ((vp1[1] > point[1] ) != (vp2[1] > point[1])) and
        (point[0] < (vp2[0] - vp1[0]) * (point[1] - vp1[1]) / (vp2[1] - vp1[1]) + vp1[0])
        )


def point_polygon(p: T_POINT, poly: T_POLYGON) -> bool:
    """_summary_

    Args:
        p (T_POINT): Point
        poly (T_POLYGON): Polygon Positions

    Returns:
        bool: True if Point overlapping Polygon otherwise False
    """

    length = len(poly)

    lookup = tuple(
        True
        for i in range(0, length)
        if _is_inside(p, poly[i], poly[i - 1] if i != 0 else poly[length - 1])
        )

    return len(lookup) % 2 != 0





__dir__ = (
    "point_polygon",
)


__author__ = "Tooraj"
__email__ = "booleansfunction@Gmail.com"
