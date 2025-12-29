from functools import cache
from pathlib import Path

data_raw = (Path(__file__).parent / "day11.txt").read_text().strip().split("\n")
nodes = {key: values.split() for key, values in (line.split(":") for line in data_raw)}
nodes['out'] = []

@cache
def count_paths(frm, to):
    if frm == to:
        return 1
    return sum(count_paths(succ, to) for succ in nodes[frm])

print("part 1:", count_paths("you", "out"))
print("part 2:", count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out") +
                 count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out"))
