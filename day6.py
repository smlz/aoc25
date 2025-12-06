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

ops = data_raw[-1].split()

res = 0
intermediate = 1 if ops[0] == "*" else 0
col = 0
for chars in zip(*data_raw[:-1]):
    s = "".join(chars).strip()
    if s:
        if ops[col] == "+":
            intermediate += int(s)
        else:
            intermediate *= int(s)
    else:
        res += intermediate
        col += 1
        intermediate = 1 if ops[col] == "*" else 0

if intermediate:
    res += intermediate
    
print("part 2:", res)