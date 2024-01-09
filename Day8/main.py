import re

def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

def gcd(a,b):
    if a == b:
        return a
    elif a == 0 or b == 0:
        return a + b
    elif a > b:
        answer = gcd(a % b, b)
    else:
        answer = gcd(a, b % a)
    return answer

def lcm(a,b):
    return int(abs(a) * (abs(b) / gcd(a,b)))

content = readTXT("liljoe.txt")

sequence = []
mapping = {}
i = 0
while i < len(content):
    if i == 0:
        for char in content[i]:
            if char == "L":
                sequence.append(0)
            elif char == "R":
                sequence.append(1)
    elif content[i] != '':
        mapping[content[i].split(" = ")[0]] = (content[i].split(" = ")[1].split(", ")[0][1:],
                                               content[i].split(" = ")[1].split(", ")[1][:-1]
                                            )
    i += 1

position = "AAA"
arrived = False
steps = 0
while not arrived:
    for direction in sequence:
        steps += 1
        position = mapping[position][direction]
        if position == "ZZZ":
            arrived = True
            break

print(f"Q1: {steps}")

starters = [[x, 0, 0, 0, 0, 0] for x in mapping.keys() if x[-1] == "A"]
print(starters)

arrived = False
steps2 = 0
while not arrived:
    for direction in sequence:
        steps2 += 1
        i = 0
        while i < len(starters):
            starters[i][0] = mapping[starters[i][0]][direction]
            i += 1
        j = 0
        while j < len(starters):
            if starters[j][0][-1] == "Z":
                if starters[j][1] == 0:
                    starters[j][1] = steps2
                elif starters[j][2] == 0:
                    starters[j][2] = steps2
                elif starters[j][3] == 0:
                    starters[j][3] = steps2
                # arrived = True
            j += 1
    if steps2 >= 100000:
        arrived = True
print(starters)

print(f"Q2: {steps2}")

leastCM = 0
i = 0
while i < len(starters):
    if leastCM == 0:
        leastCM = lcm(starters[i][1], starters[i + 1][1])
    elif i + 1 < len(starters):
        leastCM = lcm(leastCM, starters[i + 1][1])
    i += 1

print(f"Least Common Multiple: {leastCM}")