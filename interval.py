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

EMPTY: Interval = Interval(math.inf, -math.inf)
UNIVERSE: Interval = Interval(-math.inf, math.inf)