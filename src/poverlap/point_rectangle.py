
from typing import TypeAlias


"""
Point Overlapping Rectangle

"""

# TYPE ALIASES

T_X: TypeAlias = int | float
T_Y: TypeAlias = int | float
T_W: TypeAlias = int | float
T_H: TypeAlias = int | float
T_POINT: TypeAlias = tuple[T_X, T_Y], list[T_X, T_Y]
T_POSITION: TypeAlias = T_POINT
T_SIZE: TypeAlias = tuple[T_W, T_H], list[T_W, T_H]

# DEFINE ALGORITHM

def point_rectangle(p: T_POINT, rect_pos: T_POSITION, rect_size: T_SIZE) -> bool:
    """Point Overlapping Rectangle

    Args:
        p (T_POINT): Point
        rect_pos (T_POSITION): Rectangle Position
        rect_size (T_SIZE): Rectangle Size

    Returns:
        bool: True if point Overlapping with Rect otherwise False
    """
    return (
        (p[0] >= rect_pos[0]) and 
        (p[0] <= rect_pos[0] + rect_size[0]) and 
        (p[1] >= rect_pos[1]) and 
        (p[1] <= rect_pos[1] + rect_size[1])
        )


def point_rectangle_add_area(p: T_POINT, rect_pos: T_POSITION, rect_size: T_SIZE, active_distance: float = 0.0) -> bool:
    """Point Overlapping Rectangle With Active Area Distance

    Args:
        p (T_POINT): Point
        rect_pos (T_POSITION): Rectangle Position
        rect_size (T_SIZE): Rectangle Size
        active_distance (float, optional): Area Distance Positive or Negative. Defaults to 0.0.

    Returns:
        bool: True if point Overlapping with Rect Active Area otherwise False
    """
    return (
        (p[0] + active_distance >= rect_pos[0]) and 
        (p[0] <= rect_pos[0] + rect_size[0] + active_distance) and 
        (p[1] + active_distance >= rect_pos[1]) and 
        (p[1] <= rect_pos[1] + rect_size[1] + active_distance)
        )



__dir__ = (
    "point_rectangle",
    "point_rectangle_add_area",
)


__author__ = "Tooraj"
__email__ = "booleansfunction@Gmail.com"
