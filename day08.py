import pathlib
data_raw = (pathlib.Path(__file__).parent / "day08.txt").read_text().strip().split()

debug = False
if debug:
    data_raw = """162,817,812
        57,618,57
        906,360,560
        592,479,940
        352,342,300
        466,668,158
        542,29,236
        431,825,988
        739,650,466
        52,470,668
        216,146,977
        819,987,18
        117,168,530
        805,96,715
        346,949,466
        970,615,88
        941,993,340
        862,61,35
        984,92,344
        425,690,689""".split()


##########
# PART 1 #
##########
from itertools import combinations
from math import prod

dist = lambda boxes: sum((n1 - n2) * (n1 - n2) for n1, n2 in zip(*boxes))
boxes = [tuple(map(int, line.split(","))) for line in data_raw]
pairs_by_distance = sorted(combinations(boxes, 2), key=dist)

circuits = [{b} for b in boxes]  # as formulated in problem description
                                 # (also prevents edge cases later)

n = 10 if debug else 1000
for b1, b2 in pairs_by_distance[:n]:
    i1 = -1
    i2 = -1
    for i, c in enumerate(circuits):  # locate circuits for boxes
        if b1 in c:
            assert i1 == -1           # must not find the same box twice
            i1 = i
        if b2 in c:
            assert i2 == -1
            i2 = i
    assert i1 != -1 and i2!= -1       # must find both boxes

    if i1 != i2:    # not yet in the same circuit, thus merge circuits
        circuits[i1] |= circuits[i2]
        del circuits[i2]

    if debug:
        print("Boxes:", b1, "<->", b2, f"[Distance: {dist((b1, b2)):_}]")
        for circuit in sorted(circuits, key=len, reverse=True):
            print(len(circuit), circuit)
        print("***********")

print("part 1:", prod(sorted(map(len, circuits), reverse=True)[:3]))


##########
# PART 2 #
##########

# continue from where we stopped in part 1
for b1, b2 in sorted_by_distance[n:]:
    i1 = -1
    i2 = -1
    for i, c in enumerate(circuits):
        if b1 in c:
            i1 = i
        if b2 in c:
            i2 = i

    if i1 != i2:    # not yet in the same circuit, thus merge circuits
        circuits[i1] |= circuits[i2]
        del circuits[i2]

    if len(circuits) == 1:
        break

print("part 2:", b1[0] * b2[0])
