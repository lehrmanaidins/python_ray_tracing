"""
    Vector3 and Point3 Classes
    @author Lehrman, Aidin
"""

from __future__ import annotations
from typing import Union
import math

class Vector3:
    """ Vector3 Class
    
    Args:
        _x, _y, _z (floats): _x, _y, and _z values of the Vector3
        (Each entered as seperate argument)
            or
        vector (Vector3): Creates second Vector3 with same values as argument Vector3
        (Only need 1 argument)

    Returns:
        
    """
    def __init__(self, *args: Union[int, float, Vector3]) -> None:
        if len(args) == 1:
            try:
                self._x: float = args[0]._x
                self._y: float = args[0]._y
                self._z: float = args[0]._z
            except TypeError:
                pass
        elif len(args) == 3:
            try:
                self._x: float = args[0]
                self._y: float = args[1]
                self._z: float = args[2]
            except TypeError:
                pass
        else:
            raise TypeError

    def __str__(self) -> str:
        return f'[{self._x}, {self._y}, {self._z}]'

    def __add__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            _x: float = self._x + value
            _y: float = self._y + value
            _z: float = self._z + value
            return Vector3(_x, _y, _z)
        elif isinstance(value, Vector3):
            _x: float = self._x + value._x
            _y: float = self._y + value._y
            _z: float = self._z + value._z
            return Vector3(_x, _y, _z)
        else:
            raise TypeError

    def __iadd__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            self._x += value
            self._y += value
            self._z += value
            return self
        elif isinstance(value, Vector3):
            self._x += value._x
            self._y += value._y
            self._z += value._z
            return self
        else:
            raise TypeError

    def __sub__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            _x: float = self._x - value
            _y: float = self._y - value
            _z: float = self._z - value
            return Vector3(_x, _y, _z)
        elif isinstance(value, Vector3):
            _x: float = self._x - value._x
            _y: float = self._y - value._y
            _z: float = self._z - value._z
            return Vector3(_x, _y, _z)
        else:
            raise TypeError

    def __isub__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            self._x -= value
            self._y -= value
            self._z -= value
            return self
        elif isinstance(value, Vector3):
            self._x -= value._x
            self._y -= value._y
            self._z -= value._z
            return self
        else:
            raise TypeError

    def __mul__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            _x: float = self._x * value
            _y: float = self._y * value
            _z: float = self._z * value
            return Vector3(_x, _y, _z)
        elif isinstance(value, Vector3):
            _x: float = self._x * value._x
            _y: float = self._y * value._y
            _z: float = self._z * value._z
            return Vector3(_x, _y, _z)
        else:
            raise TypeError

    def __imul__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            self._x *= value
            self._y *= value
            self._z *= value
            return self
        elif isinstance(value, Vector3):
            self._x *= value._x
            self._y *= value._y
            self._z *= value._z
            return self
        else:
            raise TypeError

    def __truediv__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            try:
                _x: float = self._x / value
                _y: float = self._y / value
                _z: float = self._z / value
                return Vector3(_x, _y, _z)
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        elif isinstance(value, Vector3):
            try:
                _x: float = self._x / value._x
                _y: float = self._y / value._y
                _z: float = self._z / value._z
                return Vector3(_x, _y, _z)
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        else:
            raise TypeError

    def __itruediv__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            try:
                self._x /= value
                self._y /= value
                self._z /= value
                return self
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        elif isinstance(value, Vector3):
            try:
                self._x /= value._x
                self._y /= value._y
                self._z /= value._z
                return self
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        else:
            raise TypeError

    def __floordiv__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            try:
                _x: float = self._x // value
                _y: float = self._y // value
                _z: float = self._z // value
                return Vector3(_x, _y, _z)
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        elif isinstance(value, Vector3):
            try:
                _x: float = self._x // value._x
                _y: float = self._y // value._y
                _z: float = self._z // value._z
                return Vector3(_x, _y, _z)
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        else:
            raise TypeError

    def __ifloordiv__(self, value: Union[int, float, Vector3]) -> Vector3:
        if isinstance(value, Union[int, float]):
            try:
                self._x //= value
                self._y //= value
                self._z //= value
                return self
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        elif isinstance(value, Vector3):
            try:
                self._x //= value._x
                self._y //= value._y
                self._z //= value._z
                return self
            except ZeroDivisionError:
                return Vector3(0, 0, 0)
        else:
            raise TypeError

    def length_squared(self) -> float:
        """ Calculates sq(length) of Vector3
        """
        return (self._x ** 2) + (self._y ** 2) + (self._z ** 2)

    def length(self) -> float:
        """ Retruns sqrt(length_squared)
        """
        return math.sqrt(self.length_squared())


class Point3(Vector3):
    """ Point Class is used for readability (It is a Vector3, just different name)
    """
    def __str__(self) -> str:
        return f'({self._x}, {self._y}, {self._z})'


def dot(a: Vector3, b: Vector3) -> float:
    """ Dot product of two Vector3's
    """
    if not (isinstance(a, Vector3) or isinstance(b, Vector3)):
        raise TypeError
    return (a._x * b._x) + (a._y * b._y) + (a._z * b._z)

def cross(a: Vector3, b: Vector3) -> Vector3:
    """ Cross product of two Vector3's
    """
    if not (isinstance(a, Vector3) or isinstance(b, Vector3)):
        raise TypeError
    return Vector3(a._y * b._z - a._z * b._y,
                   a._z * b._x - a._x * b._z,
                   a._x * b._y - a._y * b._x)

def unit_vector(a: Vector3) -> Vector3:
    """ Returns Vector3 with same direction as argument Vector3, but with magnitude of 1
    """
    if not isinstance(a, Vector3):
        raise TypeError
    return a / a.length()
