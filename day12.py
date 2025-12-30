import re
from collections import namedtuple
from pathlib import Path

data_raw = (Path(__file__).parent / "day12.txt").read_text().strip().split("\n\n")

shapes = [shape.split("\n")[1:] for shape in data_raw[:-1]]
shape_sizes = [sum(c == "#" for line in shape for c in line) for shape in shapes]

Area = namedtuple("Area", ("width", "length", "presents"))
areas = [Area(int(width), int(length), tuple(map(int, presents.split()))) for width, length, presents in
              (re.match(r"(\d+)x(\d+): ([\d ]*)", line).groups() for  line in data_raw[-1].split("\n"))]

fit_count = 0
not_fit_count = 0
to_be_analyzed_count = 0
for area in areas:
    if (area.width // 3) * (area.length // 3) >= sum(area.presents):
        fit_count += 1
    elif sum(shape_sizes[i] * count for i, count in enumerate(area.presents)) > area.width * area.length:
        not_fit_count += 1
    else:
        print("unknown:", area)
        to_be_analyzed_count += 1

assert fit_count + not_fit_count + to_be_analyzed_count == len(areas)

if to_be_analyzed_count == 0:
    print("part 1:", fit_count)
