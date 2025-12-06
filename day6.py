import pathlib
data_raw = (pathlib.Path(__file__).parent / "day6.txt").read_text().strip().split("\n")

from math import prod

lines = (line.split() for line in data_raw)
res = 0
for *numbers, op in zip(*lines):
    if op == "+":
        res += sum(map(int, numbers))
    else:
        res += prod(map(int, numbers))

print("part 1:", res)

# quite readable
lines = (line.split() for line in data_raw)
print("part 1:",
      sum(sum(map(int, numbers)) if op == "+" else prod(map(int, numbers)) for *numbers, op in zip(*lines))) 