import pathlib
data_raw = (pathlib.Path(__file__).parent / "day09.txt").read_text().strip().split()

##########
# PART 1 #
##########
from itertools import combinations

points = ((int(x), int(y)) for x, y in (line.split(",") for line in data_raw))
size = lambda p1, p2: (abs(p1[0] - p2[0]) + 1) * abs((p1[1] - p2[1]) + 1)
print("part 1:", max(size(p1, p2) for p1, p2 in combinations(points, 2)))
