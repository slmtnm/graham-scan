from sys import argv
from graham import Point, convex_hull

if len(argv) < 2:
    print('Usage: python3 ./main.py <file-with-points>')
    exit(1)

with open(argv[1]) as f:
    points = [Point(*line.split()) for line in f]

for point in convex_hull(points):
    print(point)
