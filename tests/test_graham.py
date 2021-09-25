from graham.point import Point
from graham.convex_hull import convex_hull

def test_three_one_line():
    points = [
        Point(0, 1),
        Point(1, 1),
        Point(2, 1),
    ]
    assert convex_hull(points) == [Point(0, 1), Point(2, 1)]

def test_hundreed_one_line():
    points = [Point(i, 1) for i in range(100)]
    assert convex_hull(points) == [Point(0, 1), Point(99, 1)]

def test_simple1():
    points = [
        Point(0, 0),
        Point(10, 0),
        Point(5, 5),
    ]
    assert convex_hull(points) == points

def test_simple2():
    points = [
        Point(7, 4),
        Point(0, 6),
        Point(8, 7),
        Point(3, 7),
        Point(3, 5),
    ]
    assert convex_hull(points) == [
        Point(7, 4),
        Point(8, 7),
        Point(3, 7),
        Point(0, 6),
        Point(3, 5),
    ]

def test_simple3():
    points = [
        Point(1, 0),
        Point(3, 3),
        Point(2, 2),
        Point(0, 0),
    ]
    assert convex_hull(points) == [
        Point(0, 0),
        Point(1, 0),
        Point(3, 3),
    ]
