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
debug = False
if debug:
    data_raw = """7,3
7,1
11,1
11,7
9,7
9,5
2,5
2,3""".split()

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
    for vline in vlines:
        assert hline[0].y == hline[1].y
        assert vline[0].x == vline[1].x
        min_x = min(p.x for p in hline)
        max_x = max(p.x for p in hline)
        min_y = min(p.y for p in vline)
        max_y = max(p.y for p in vline)
        # lines shall not intersect
        assert not (min_x < vline[0].x < max_x and min_y < hline[0].y < max_y)
        if min_x <= vline[0].x <= max_x and min_y <= hline[0].y <= max_y:
            touches += 1
assert touches == len(lines)

def rect_contains_no_lines(p1, p2):
    min_x, max_x = min(p1.x, p2.x), max(p1.x, p2.x)
    min_y, max_y = min(p1.y, p2.y), max(p1.y, p2.y)
    for vline in vlines:
        # horizontally inside the rectangle and vertically not outside of the rectangle
        if min_x < vline[0].x < max_x and not ((vline[0].y >= max_y and vline[1].y >= max_y) or (vline[0].y <= min_y and vline[1].y <= min_y)):
            return False
    for hline in hlines:
        # vertically inside the rectangle and horizontally not outside of the rectangle
        if min_y < hline[0].y < max_y and not((hline[0].x >= max_x and hline[1].x >= max_x) or (hline[0].x <= min_x and hline[1].x <= min_x)):
            return False
    return True

size = lambda p1, p2: (abs(p1[0] - p2[0]) + 1) * abs((p1[1] - p2[1]) + 1)
rects_by_size = sorted(((p1, p2) for p1, p2 in combinations(points, 2)), key=lambda ps: size(*ps), reverse=True)

for p1, p2 in rects_by_size:
    if rect_contains_no_lines(p1, p2):
        print("part 2:", size(p1, p2))
        break
