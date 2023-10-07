"""
    Interval Class
    @author Lehrman, Aidin
"""

from __future__ import annotations
import math

class Interval:
    def __init__(self, min: float=math.inf, max: float=-math.inf) -> None:
        self.min = min
        self.max = max

    def contains(self, x: float=0) -> bool:
        return self.min <= x and x <= self.max

    def surrounds(self, x: float=0) -> bool:
        return self.min < x and x < self.max
    
    def clamp(self, x: float=0) -> float:
        if x < self.min:
            return self.min
        if x > self.max: 
            return self.max
        return x

EMPTY: Interval = Interval(math.inf, -math.inf)
UNIVERSE: Interval = Interval(-math.inf, math.inf)