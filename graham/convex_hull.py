from __future__ import annotations
from typing import List, Tuple
from operator import itemgetter
from .slope import Slope
from .point import Point, ccw


def convex_hull(points: List[Point]) -> List[Point]:
    '''Calculates convex hull of given point list'''
    points = list(points)

    # find minimal point
    i, P = min(enumerate(points), key=itemgetter(1))
    points.pop(i)

    # sort by polar angle
    def key(p: Point) -> Tuple[Slope, int]:
        d = p - P
        return (Slope(d.x, d.y), d.len2())
    points.sort(key=key)

    # construct convex hull
    stack = [P]
    for p in points:
        while len(stack) > 1 and ccw(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack

