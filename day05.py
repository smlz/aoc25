import pathlib
ranges, ids = (pathlib.Path(__file__).parent / "day05.txt").read_text().strip().split("\n\n")
ranges = [range(int(i), int(j) + 1) for i, j in (line.split("-") for line in ranges.split("\n"))]

print("part 1:", sum(any(int(i) in r for r in ranges) for i in ids.split("\n") if i.strip()))

ranges.sort(key=lambda r: r.start)
merged_ranges = [ranges[0]]
for r in ranges[1:]:
    last = merged_ranges[-1]
    if last.stop < r.start:         # no overlap
        merged_ranges.append(r)
    elif last.stop < r.stop:        # overlap, but not contained => extend
        merged_ranges[-1] = range(last.start, r.stop)
    
print("part 2:", sum(map(len, merged_ranges)))

