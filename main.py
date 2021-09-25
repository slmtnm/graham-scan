from sys import argv
from graham.point import Point
from graham.convex_hull import convex_hull


def main():
    if len(argv) < 2:
        print('Usage: python3 ./main.py <file-with-points>')
        exit(1)

    with open(argv[1]) as f:
        points = [Point(*[int(c) for c in line.split()]) for line in f]

    for point in convex_hull(points):
        print(point)


if __name__ == '__main__':
    main()

