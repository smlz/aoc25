import pathlib
data_raw = (pathlib.Path(__file__).parent / "day4.txt").read_text().strip().split("\n")

# add margin of empty fields around playing field in order to prevent edge cases. like literally.
line_length = len(data_raw[0]) + 2
data = []
data.append("." * line_length)
for line in data_raw:
    data.append("." + line + ".")
data.append("." * line_length)

nbr = 0
for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) -1):
        if data[i][j] == "@":
            if sum(data[i + ii][j + jj] == "@" for ii in range(-1, 2) for jj in range(-1, 2)) < 5:
                nbr +=1

print("part 1:", nbr)

# using generator expressions
print("part 1:",
      sum(sum(data[i + ii][j + jj] == "@" for ii in range(-1, 2) for jj in range(-1, 2)) < 5 
          for i in range(1, len(data) - 1)
          for j in range(1, len(data[i]) -1) if data[i][j] == "@"
          )
      )


# convert line strings to list of characters to make the mutable
data = [list(line) for line in data]

nbr = 0
runs = 0
changes = True
while changes:
    runs += 1
    changes = False
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) -1):
            if data[i][j] == "@":
                if sum(data[i + ii][j + jj] == "@" for ii in range(-1, 2) for jj in range(-1, 2)) < 5:
                    nbr +=1
                    data[i][j] = "."
                    changes = True
print("part 2:", nbr)
print("runs:", runs)

# print final map
for line in data:
    print("".join(line))
