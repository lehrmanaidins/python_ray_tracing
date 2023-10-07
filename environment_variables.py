"""
    Vector3, Point3, and Ray3 Classes
    @author Lehrman, Aidin
"""

from __future__ import annotations
from random import random, uniform
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
    
    def negate(self) -> Vector3:
        return Vector3(-self._x, -self._y, -self._z)
    
    def unit_vector(self, unit: float=1) -> Vector3:
        return self / self.length() * unit
    
    def to_list(self) -> list:
        """ Returns Vector3 formated as list of length 3 with 
            '_x' ([0]), '_y' ([1]), and '_z' ([2]) values scaled to [0, 1]
        """
        return [self._x, self._y, self._z]
    
    def is_near_zero(self) -> bool:
        s: float = 1e-8
        return (abs(self._x) < s) and (abs(self._y) < s) and (abs(self._z) < s)


class Point3(Vector3):
    """ Point Class is used for readability (It is a Vector3, just different name)
    """
    def __str__(self) -> str:
        return f'({self._x}, {self._y}, {self._z})'


def dot(vector1: Vector3, vector2: Vector3) -> float:
    """ Dot product of two Vector3's
    """
    if not (isinstance(vector1, Vector3) or isinstance(vector2, Vector3)):
        raise TypeError
    return (vector1._x * vector2._x) + (vector1._y * vector2._y) + (vector1._z * vector2._z)

def cross(vector1: Vector3, vector2: Vector3) -> Vector3:
    """ Cross product of two Vector3's
    """
    if not (isinstance(vector1, Vector3) or isinstance(vector2, Vector3)):
        raise TypeError
    return Vector3(vector1._y * vector2._z - vector1._z * vector2._y,
                   vector1._z * vector2._x - vector1._x * vector2._z,
                   vector1._x * vector2._y - vector1._y * vector2._x)

def unit_vector(vector: Vector3, unit: float=1) -> Vector3:
    """ Returns Vector3 with same direction as argument Vector3, but with magnitude of 1
    """
    if not isinstance(vector, Vector3):
        raise TypeError
    return vector / vector.length() * unit

def random_vector3() -> Vector3:
    return Vector3(random(), random(), random())

def random_vector3(min: float, max: float) -> Vector3:
    return Vector3(uniform(min, max), uniform(min, max), uniform(min, max))

def random_in_unit_sphere() -> Vector3:
    while True:
        p: Vector3 = random_vector3(-1, 1)
        if p.length_squared() < 1:
            return p
        
def random_unit_vector3() -> Vector3:
    return unit_vector(random_in_unit_sphere())

def random_on_hemisphere(normal: Vector3) -> Vector3:
    on_unit_sphere: Vector3 = random_unit_vector3()
    if dot(on_unit_sphere, normal) > 0:
        return on_unit_sphere
    else:
        return on_unit_sphere * -1
    
def reflect(v: Vector3, n: Vector3) -> Vector3:
    return v - (n * dot(v, n) * 2)


class Ray3:
    """ Ray3 is made up of two parts; a point in 3D space, and a vector in a direction
    
    Args:
        origin (Point3): Origin point of the ray
        direction (Vector3): Direction the ray is pointing towards

    Returns:
        3D Ray from Point3 'origin' in direction 'direction' with infinite magnitude
    
    """
    def __init__(self, origin: Point3, direction: Vector3) -> None:
        if not (isinstance(origin, Vector3) and isinstance(direction, Vector3)):
            raise TypeError
        self.origin = origin
        self.direction = direction

    def __str__(self) -> str:
        return f'{str(self.origin)} -> {str(self.direction)}'

    def point_at(self, distance: Union[int, float]) -> Point3:
        """ Returns point that is on ray 't' distance from ray's origin
        :t: Distance from origin
        :t type: float or int
        :returns: Point3 on ray 't' distnace from origin
        :rtype: Point3
        """
        if not (isinstance(distance, float) or isinstance(distance, int)):
            raise TypeError
        return self.origin + (self.direction.unit_vector() * distance)