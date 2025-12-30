import pathlib
ranges = (pathlib.Path(__file__).parent / "day02.txt").read_text().strip()

res = 0
for r in ranges.split(","):
    start, stop = r.split("-")
    for i in range(int(start), int(stop) + 1):
       s = str(i)
       if s[:len(s)//2] == s[len(s)//2:]:
           res += i
           
print("part 1:", res)

# Zen of Python: readability counts
print("part 1:",
      sum(x for r in ranges.split(",") if len(s := r.split("-")) == 2
            for x in range(int(s[0]), int(s[1]) + 1) if (s := str(x))[:len(s)//2] == s[len(s)//2:]
         )
     )

res = 0
for r in ranges.split(","):
    start, stop = r.split("-")
    for x in range(int(start), int(stop) + 1):
       s = str(x)
       for i in range(1, len(s) // 2 + 1):
           if s == (s[:i] * (len(s) // i)):
               res += x
               break
       
print("part 2:", res)

# even more zen
print("part 2:",
      sum(x for r in ranges.split(",") if len(s := r.split("-")) == 2
            for x in range(int(s[0]), int(s[1]) + 1)
                if any(y[:i] * (len(y) // i) == y for i in range(1, len(str(x)) // 2 + 1) if len(y := str(x)) % i == 0)
         )
     )
       



