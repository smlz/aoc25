import pathlib
data_raw = (pathlib.Path(__file__).parent / "day07.txt").read_text().strip()

lines = data_raw.split("\n")

positions = {lines[0].index("S")}
nbr = 0

for line in lines[1:]:
    for pos in list(positions):
        if line[pos] == "^":
            positions.remove(pos)
            positions.add(pos - 1)
            positions.add(pos + 1)
            nbr += 1

print("part 1:", nbr)


positions = {lines[0].index("S")}
beam_counts = [1 if c == "S" else 0 for c in lines[0]]

for line in lines[1:]:
    for pos in list(positions):
        if line[pos] == "^":
            positions.remove(pos)
            positions.add(pos - 1)
            positions.add(pos + 1)

            beam_counts[pos - 1] += beam_counts[pos]
            beam_counts[pos + 1] += beam_counts[pos]
            beam_counts[pos] = 0

print("part 2:", sum(beam_counts))
