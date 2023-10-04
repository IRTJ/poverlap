# **POVERLAP**


POverlap or Point Overlap is pure python library For Check Overlapping or Colliding 2D Point With Any 2D Shape. And Work Everywhere.

# Installation

Install library like other library use `pip` package manager.

```bash
pip install poverlap
```

```shell
py -m pip install poverlap
```

## Usage

First Importing `poverlap` Package

```python
import poverlap
```

then use any function you needed

```python
point_a = (10, 200)
point_b = (30, 100)

pdp: float = poverlap.point_distance(point_a, point_b)

pop: bool = poverlap.point_point(point_a, point_b)
pop_area: bool = poverlap.point_point_add_area(point_a, point_b, 5.5)

```

## Some Detail

All Overlapping Point Algorithm in One File and Any File Fully NoDepended Can Use One File From `poverlap` in your app without need anything else.

__TypeAliases Mean:__
```python
# in point_point.py
T_X: TypeAlias = int | float
T_Y: TypeAlias = int | float
T_POINT: TypeAlias = tuple[T_X, T_Y], list[T_X, T_Y]

# added in point_line.py
T_LINE: TypeAlias = tuple[T_POINT, T_POINT], list[T_POINT, T_POINT]

# added in point_rectangle.py
T_W: TypeAlias = int | float
T_H: TypeAlias = int | float
T_POSITION: TypeAlias = T_POINT
T_SIZE: TypeAlias = tuple[T_W, T_H], list[T_W, T_H]

# added in point_circle.py
T_RADIUS: TypeAlias = int |float

# added in point_polygon.py
T_POLYGON: TypeAlias = tuple[T_POSITION], list[T_POSITION]
```

Some of Function Name Ended With `_add_area()` like `point_point_add_area()` this means u can Use for Bigger or Some Bigger and Smaller Area for Detection Overlapping.


[SourceCode](https://github.com/IRTJ/poverlap)

## License


[MIT](https://github.com/IRTJ/poverlap/blob/main/License)
