from collections import Counter
from itertools import combinations, chain
import pathlib
import re

##########
# PART 1 #
##########

def test_light_indicators(lights, toggles):
    for n in range(1, len(toggles) + 1):
        for comb in combinations(toggles, n):
            counts = Counter(chain(*comb))
            if all(on == (counts[i] % 2 == 1) for i, on in enumerate(lights)):
                return n
    raise Exception("No button combination found")

def process_line_part_1(line):
    lights, toggles, joltages = re.match(r"\[([\.#]+)\] ([ \d\(\),]+) \{([\d,]+)\}", line).groups()
    lights = [c == '#' for c in lights]
    toggles = tuple(tuple(int(n) for n in w[1:-1].split(',')) for w in toggles.split())
    return test_light_indicators(lights, toggles)
            

debug = False
if __name__ == '__main__':
    data_raw = (pathlib.Path(__file__).parent / "day10.txt").read_text().strip().split("\n")
    if debug:
        data_raw = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".strip().split("\n")

    print("part 1:", sum(process_line_part_1(line) for line in data_raw))
    
