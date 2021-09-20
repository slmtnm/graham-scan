from __future__ import annotations
from typing import List
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def __lt__(self, p: Point) -> bool:
        return self.y < p.y if self.y != p.y else self.x < p.x

    def __sub__(self, p: Point) -> Point:
        return Point(self.x - p.x, self.y - p.y)

    def __str__(self) -> str:
        return '({}, {})'.format(self.x, self.y)

    def dot(self, p: Point) -> float:
        return self.x * p.x + self.y * p.y

    def normalized(self) -> Point:
        len = sqrt(self.x * self.x + self.y * self.y)
        if len == 0:
            return Point(0, 0)
        return Point(self.x / len, self.y / len)


def ccw(p1: Point, p2: Point, p3: Point) -> float:
    '''Calculates z-coordinate of cross product of vectors p1p2 and p1p3'''
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


class Graham:
    def __init__(self, points: List[Point]) -> None:
        self.points = points

    def convex_hull(self) -> List[Point]:
        # lowest point
        P = min(self.points)

        # actually, there is no need to exclude P from self.points,
        # because after meeting P, any subsequent turn will be 'right' turn
        # and P will be popped from stack

        # sort by polar angle with Ox
        self.points.sort(
            key=lambda p: (p - P).normalized().dot(Point(1, 0)),
            reverse=True
        )

        stack = [P]
        for p in self.points:
            while len(stack) > 1 and ccw(stack[-2], stack[-1], p) <= 0:
                stack.pop()
            stack.append(p)

        return stack
