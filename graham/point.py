from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def __lt__(self, other: Point) -> bool:
        return (self.y, self.x) < (other.y, other.x)

    def __sub__(self, p: Point) -> Point:
        return Point(self.x - p.x, self.y - p.y)

    def len2(self) -> int:
        return self.x * self.x + self.y * self.y


def ccw(p1: Point, p2: Point, p3: Point) -> int:
    '''Calculates z-coordinate of cross product of vectors p1p2 and p1p3'''
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

