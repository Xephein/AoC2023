import time

def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

def expansion(universe, galaxies, expansion):
    expansion -= 1
    # Iterate over rows in universe
    rowC = len(universe)
    for y in range(1, rowC + 1):
        if '#' not in universe[-y]:
            for i in range(0, len(galaxies)):
                if galaxies[i][1] > rowC - y:
                    galaxies[i][1] += expansion
    # Iterate over columns in universe
    colC = len(universe[0])
    for x in range(1, colC + 1):
        if '#' not in [row[-x] for row in universe]:
            for j in range(0, len(galaxies)):
                if galaxies[j][0] > colC - x:
                    galaxies[j][0] += expansion

    return galaxies

def stepCount(galaxies):
    steps = 0
    for x in galaxies:
        for y in galaxies:
            steps += abs(y[0] - x[0]) + abs(y[1] - x[1])
    return int(steps / 2)

content = readTXT("input.txt")

galaxies = []
galaxy2 = []
for row in range(0, len(content)):
    for char in range(0, len(content[row])):
        if content[row][char] == '#':
            galaxies.append([char, row])
            galaxy2.append([char, row])



galaxies = expansion(content, galaxies, 2)
steps = stepCount(galaxies)

galaxy2 = expansion(content, galaxy2, 1000000)
steps2 = stepCount(galaxy2)

print(f"Q1: {steps}")
print(f"Q2: {steps2}")