import pathlib
codes = (pathlib.Path(__file__).parent / "day1.txt").read_text().strip().split("\n")

ccodes = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".split("\n")

p = print
print = lambda *x: ...

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
       
p("Answer part 1:", n1)
p("Answer part 2:", n2)


print = p
x = 50
print(sum((x := (x + (-1 if c[0] == "L" else 1) * int(c[1:])) % 100) == 0 for c in codes))

x = 50
print(sum((x := (x + (-1 if c[0] == "L" else 1)) % 100) == 0 for c in codes for _ in range(int(c[1:]))))


def all_clicks(start, codes):
    x = start
    for code in codes:
        d = -1 if code[0] == "L" else 1
        n = int(code[1:])
        for _ in range(n):
            x = (x + d) % 100
            yield x


print(sum(n == 0 for n in all_clicks(50, codes)))

p1, p2, x = 0, 0, 50
for line in codes:
    for i in range(int(line[1:])):
        x = (x + [-1, 1][line[0] == 'R']) % 100
        p2 += x == 0
    p1 += x == 0

p(p1)
p(p2)