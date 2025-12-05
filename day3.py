import pathlib
lines = (pathlib.Path(__file__).parent / "day3.txt").read_text().strip().split("\n")

res = 0
for line in lines:
    numbers = [int(x) for x in line]
    first = max(numbers[:-1])
    idx = numbers.index(first)
    second = max(numbers[numbers.index(first) + 1:])
    #print(second)
    #print(f"{nbr=}")
    res += 10 * first + second

print("part 1:", res)

print("part 1:",
      sum((first := max(numbers[:-1])) * 10 + max(numbers[numbers.index(first) + 1:])
            for line in lines if (numbers := [int(x) for x in line])
         )
     )

5322532524412431424224553433255235332456444432543425324265123263732352855273513551554412243351423435

res = 0
for line in lines:
    numbers = [int(x) for x in line]
    idx = 0
    for i in range(11, -1, -1):
        digit = max(numbers[idx:(len(numbers) - i)])
        idx = idx + numbers[idx:].index(digit) + 1
        res += digit * 10**i

print("part 2:", res)
#part 2: 175053592950232


print("part 2:",
      sum(sum(digit * 10**(11-i) for i in range(12) if (digit := max(numbers[idx:(len(numbers) - 11 + i)])) >= 0 and (idx := idx + numbers[idx:].index(digit) + 1) >= 0)
          for line in lines if (numbers := [int(x) for x in line]) and not (idx := 0)
         )
     )
