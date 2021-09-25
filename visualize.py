import plotly.graph_objects as go
from graham.point import Point
from graham.convex_hull import convex_hull
from sys import argv

if len(argv) < 2:
    print('Usage: python3 ./main.py <file-with-points>')
    exit(1)

with open(argv[1]) as f:
    points = [Point(*[int(c) for c in line.split()]) for line in f]

result_points = convex_hull(points)
result_points.append(result_points[0])  # close contour

fig = go.Figure()

xs = sorted(map(lambda p: p.x, points))
ys = sorted(map(lambda p: p.y, points))

fig.update_xaxes(range=[xs[0], xs[-1]])
fig.update_yaxes(range=[ys[0], ys[-1]])

xs, ys = [p.x for p in points], [p.y for p in points]
result_xs, result_ys = [p.x for p in result_points], [
    p.y for p in result_points]

fig.add_scatter(x=xs, y=ys, mode='markers', marker={'color': 'blue'})
fig.add_scatter(x=result_xs, y=result_ys, marker={'color': 'red'})
fig.update_layout(width=800, height=800)
fig.show()
