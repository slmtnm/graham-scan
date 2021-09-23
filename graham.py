from __future__ import annotations
from typing import List, Callable, Tuple
from operator import itemgetter
from slope import Slope

class Point:
    def __init__(self, x, y):
        self.x, self.y = int(x), int(y)

    def __lt__(self, p: Point) -> bool:
        return self.y < p.y if self.y != p.y else self.x < p.x

    def __sub__(self, p: Point) -> Point:
        return Point(self.x - p.x, self.y - p.y)

    def __eq__(self, p: Point) -> Point:
        return self.x == p.x and self.y == p.y

    def __str__(self) -> str:
        return str((self.x, self.y))

    def len2(self) -> int:
        return self.x * self.x + self.y * self.y


def ccw(p1: Point, p2: Point, p3: Point) -> int:
    '''Calculates z-coordinate of cross product of vectors p1p2 and p1p3'''
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


class PolarComparable:
    def __init__(self, s: Slope, len: int):
        self.s = s
        self.len = len
    
    def __lt__(self, other: PolarComparable):
        return self.s < other.s if self.s != other.s else self.len < other.len


def polar_key(P: Point) -> Callable[[Point], Tuple[Slope, int]]:
    def key(p: Point):
        d = p - P
        return PolarComparable(Slope(d.x, d.y), d.len2())
    return key


def convex_hull(points: List[Point]) -> List[Point]:
    '''Calculates convex hull of given point list'''
    points = list(points)

    # find minimal point
    i, P = min(enumerate(points), key=itemgetter(1))
    points.pop(i)

    # sort by polar angle
    points.sort(key=polar_key(P))

    # construct convex hull
    stack = [P]
    for p in points:
        while len(stack) > 1 and ccw(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack
