def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

def mover(x, y, inflow):
    outflow = []
    char = content[x][y]
    for x in range(0, len(inflow)):
        outflow.append(MAPPING[char][x] + inflow[x])
    return tuple(outflow)


MAPPING = {"|": (1, 5),
           "-": (5, 1),
           "L": (-1, 1),
           "J": (-1, -1),
           "7": (1, -1),
           "F": (1, 1),
           }

DIRS = {"up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
        }

content = readTXT("input.txt")
minimap = [["." for y in content[0]] for x in content]

i = 0
pos = []
while i < len(content):
    j = 0
    while j < len(content[i]):
        if content[i][j] == "S":
            minimap[i][j] = "S"
            for k in DIRS.keys():
                abscis = DIRS[k][0]
                ordin = DIRS[k][1]
                char = MAPPING[content[i + abscis][j + ordin]]
                if (char[0] * abscis in [1, -1]) or (char[1] * ordin in [1, -1]):
                    pos.append([i + abscis, j + ordin, DIRS[k]])
                    minimap[i + abscis][j + ordin] = content[i + abscis][j + ordin]
        j += 1
    i += 1

MAPPING["-"] = (0, 0)
MAPPING["|"] = (0, 0)

steps = 1
while not ((pos[0][0] == pos[1][0]) and (pos[0][1] == pos[1][1])):
    steps += 1
    for i in range(0,len(pos)):
        move = mover(pos[i][0], pos[i][1], pos[i][2])
        pos[i][0] = pos[i][0] + move[0]
        pos[i][1] = pos[i][1] + move[1]
        minimap[pos[i][0]][pos[i][1]] = content[pos[i][0]][pos[i][1]]
        pos[i][2] = move

print(f"Q1: {steps}")

i = 0
insideTiles = 0
while i < len(minimap):
    j = 0
    outside = 1
    half = 0
    while j < len(minimap[i]):
        if minimap[i][j] in ["-", "F", "7"]:
            pass
        elif minimap[i][j] in MAPPING.keys():
            outside *= -1
        elif minimap[i][j] == '.' and outside == -1:
            insideTiles += 1
            minimap[i][j] = "I"
        j += 1
    i += 1

print(f"Q2: {insideTiles}")

toPrint = ""
for row in minimap:
    for char in row:
        toPrint += char
    toPrint += "\n"

# print(toPrint)