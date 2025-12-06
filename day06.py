import pathlib
data_raw = (pathlib.Path(__file__).parent / "day6.txt").read_text().strip().split("\n")

from math import prod

## Part 1

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

## Part 2

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


from functools import reduce

# invert row<->cols
cols = ("".join(chars).strip() for chars in zip(*data_raw[:-1]))
# group numbers with empty columns as delimiters
number_groups = reduce(lambda grps, nbr: grps[:-1] + [grps[-1] + [int(nbr)]] if nbr else grps + [[]],
                       cols, [[]])
ops = (sum if op == "+" else prod for op in data_raw[-1].split())
print("part 2:", sum(op(numbers) for op, numbers in zip(ops, number_groups)))

# without reduce
# invert row<->cols
cols = ("".join(chars).strip() for chars in zip(*data_raw[:-1]))
# group numbers with explicit delimiter trick
number_groups = (map(int, numbers.split("&")) for numbers in "&".join(cols).split("&&"))
ops = (sum if op == "+" else prod for op in data_raw[-1].split())
print("part 2:", sum(op(numbers) for op, numbers in zip(ops, number_groups)))

# as a single expression (aka readability still counts)
print("part 2:",
      sum(op(numbers) for op, numbers in zip(
          (sum if op == "+" else prod for op in data_raw[-1].split()),
          (map(int, numbers.split("&")) for numbers in "&".join("".join(chars).strip() for chars in zip(*data_raw[:-1])).split("&&"))
)))

