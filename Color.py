"""
    Color
    @author Lehrman, Aidin
"""

from math import floor
from environment_variables import Vector3

class Color(Vector3):
    """ Color represented by Vector3 with '_x' (r), '_y' (g), and '_z' (b) values from [0, 1]
    """
    def __str__(self) -> str:
        return f'{{{self._x}, {self._y}, {self._z}}}'

    def to_rgb(self) -> list:
        """ Returns Color formated as list of length 3 with 
            '_x' ([0]), '_y' ([1]), and '_z' ([2]) values scaled to [0, 255]
        """
        _r: int = min(max(floor(self._x * 255), 0), 255) # [0, 255]
        _g: int = min(max(floor(self._y * 255), 0), 255) # [0, 255]
        _b: int = min(max(floor(self._z * 255), 0), 255) # [0, 255]
        return [_r, _g, _b]
