import pathlib
ranges, ids = (pathlib.Path(__file__).parent / "day5.txt").read_text().strip().split("\n\n")
ranges = (line.split("-") for line in ranges.split("\n"))
ranges = [range(int(i), int(j) + 1) for i, j in ranges]

print("part 1:", sum(any(int(i) in r for r in ranges) for i in ids.split("\n") if i.strip()))

ranges.sort(key=lambda r: r.start)
old_r = range(0, 0)
new_ranges = []
for r in ranges:
    if old_r.stop < r.start:                  # no overlap
        new_ranges.append(old_r)
        old_r = r
    elif old_r.stop < r.stop:                 # overlap, but not contained
        old_r = range(old_r.start, r.stop)    # extend old range
    # else:                                     contained, thus throw away
    
# append last range
new_ranges.append(old_r)

print("part 2:", sum(map(len, new_ranges)))

