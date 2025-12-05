ranges = "655-1102,2949-4331,885300-1098691,1867-2844,20-43,4382100-4484893,781681037-781860439,647601-734894,2-16,180-238,195135887-195258082,47-64,4392-6414,6470-10044,345-600,5353503564-5353567532,124142-198665,1151882036-1151931750,6666551471-6666743820,207368-302426,5457772-5654349,72969293-73018196,71-109,46428150-46507525,15955-26536,65620-107801,1255-1813,427058-455196,333968-391876,482446-514820,45504-61820,36235767-36468253,23249929-23312800,5210718-5346163,648632326-648673051,116-173,752508-837824"

res = 0
for r in ranges.split(","):
    start, stop = r.split("-")
    for i in range(int(start), int(stop) + 1):
       s = str(i)
       if s[:len(s)//2] == s[len(s)//2:]:
           res += i
           
print("part 1:", res)

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

print("part 2:",
      sum(x for r in ranges.split(",") if len(s := r.split("-")) == 2
            for x in range(int(s[0]), int(s[1]) + 1)
                if any(y[:i] * (len(y) // i) == y for i in range(1, len(str(x)) // 2 + 1) if len(y := str(x)) % n == 0)
         )
     )
       



