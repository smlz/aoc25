import pathlib
codes = (pathlib.Path(__file__).parent / "day01.txt").read_text().strip().split("\n")

x = 50
n1 = 0
n2 = 0
for l, line in enumerate(codes, 1):
    amt = ((-1) if line[0] == "L" else 1) * int(line[1:])
        
    # part 2
    if amt > 0:
        n2 += (x + amt) // 100
    elif amt < 0:
        n2 += abs(amt) // 100
        if x < abs(amt) % 100:
            n2 += 1
    else:
        raise ValueError(f"Not moving in any direction (Line {l}: {line})")
    
    x = (x + amt) % 100
    
    # part 1
    if x == 0:
        n1 += 1
       
print("part 1:", n1)
print("part 2:", n2)


# Brute-force one-liners using generator expressions and walrus operator
x = 50
print("part 1:", sum((x := (x + (-1 if c[0] == "L" else 1) * int(c[1:])) % 100) == 0 for c in codes))

x = 50
print("part 2:", sum((x := (x + (-1 if c[0] == "L" else 1)) % 100) == 0 for c in codes for _ in range(int(c[1:]))))


# generator function
def all_clicks(start, codes):
    x = start
    for code in codes:
        d = -1 if code[0] == "L" else 1
        n = int(code[1:])
        for _ in range(n):
            x = (x + d) % 100
            yield x


print(sum(n == 0 for n in all_clicks(50, codes)))
