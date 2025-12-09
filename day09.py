import pathlib
data_raw = (pathlib.Path(__file__).parent / "day09.txt").read_text().strip().split()

##########
# PART 1 #
##########
from itertools import combinations

points = ((int(x), int(y)) for x, y in (line.split(",") for line in data_raw))
size = lambda p1, p2: (abs(p1[0] - p2[0]) + 1) * abs((p1[1] - p2[1]) + 1)
print("part 1:", max(size(p1, p2) for p1, p2 in combinations(points, 2)))


##########
# PART 2 #
##########
from collections import namedtuple
from itertools import pairwise, islice

Point = namedtuple('Point', ['x', 'y'])
points = [Point(int(x), int(y)) for x, y in (line.split(",") for line in data_raw)]
lines = [(p1, p2) for p1, p2 in pairwise(points)]
lines.append((points[-1], points[0]))
vlines = list(islice(lines, 0, None, 2))
hlines = list(islice(lines, 1, None, 2))

# Check for line intersections and/or contact points
touches = 0
for hline in hlines:
    h0, h1 = hline
    for vline in vlines:
        v0, v1 = vline
        assert h0.y == h1.y
        assert v0.x == v1.x
        min_x, max_x = min(h0.x, h1.x), max(h0.x, h1.x)
        min_y, max_y = min(v0.y, v1.y), max(v0.y, v1.y)
        # lines shall not intersect
        assert not (min_x < v0.x < max_x and min_y < h0.y < max_y)
        if min_x <= v0.x <= max_x and min_y <= h0.y <= max_y:
            touches += 1
assert touches == len(lines)

def rect_contains_no_lines(p1, p2):
    min_x, max_x = min(p1.x, p2.x), max(p1.x, p2.x)
    min_y, max_y = min(p1.y, p2.y), max(p1.y, p2.y)
    for vline in vlines:
        v0, v1 = vline
        # horizontally inside the rectangle and vertically not outside the rectangle
        if min_x < v0.x < max_x and not ((v0.y >= max_y and v0.y >= max_y) or (v0.y <= min_y and v0.y <= min_y)):
            return False
    for hline in hlines:
        h0, h1 = hline
        # vertically inside the rectangle and horizontally not outside the rectangle
        if min_y < h0.y < max_y and not((h0.x >= max_x and h1.x >= max_x) or (h0.x <= min_x and h1.x <= min_x)):
            return False
    return True

size = lambda p1, p2: (abs(p1[0] - p2[0]) + 1) * abs((p1[1] - p2[1]) + 1)
rects_by_size = sorted(((p1, p2) for p1, p2 in combinations(points, 2)), key=lambda ps: size(*ps), reverse=True)

for p1, p2 in rects_by_size:
    if rect_contains_no_lines(p1, p2):
        print("part 2:", size(p1, p2))
        break
