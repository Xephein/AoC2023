def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

content = readTXT("input.txt")
altContent = []
i = 0
while i < len(content):
    content[i] = content[i].split(": ")
    content[i][1] = content[i][1].strip()
    altContent.append(content[i].copy())
    content[i][1] = content[i][1].split(" ")
    j = 0
    while j < len(content[i][1]):
        if content[i][1][j] == '':
            content[i][1].pop(j)
            j -= 1
        else:
            content[i][1][j] = int(content[i][1][j])
        j += 1
    i += 1

i = 0
while i < len(altContent):
    newString = ""
    j = 0
    while j < len(altContent[i][1]):
        if altContent[i][1][j].isdigit():
            newString += altContent[i][1][j]
        j += 1
    altContent[i][1] = int(newString)
    i += 1

altContent = {altContent[0][0]: altContent[0][1],
              altContent[1][0]: altContent[1][1]
              }

inputs = {}
for x in content:
    inputs[x[0]] = x[1]

factors = []
i = 0
while i < len(inputs["Time"]):
    ways = 0
    t = inputs["Time"][i]
    for x in range(0,t):
        if x * (t - x) > inputs["Distance"][i]:
            ways += 1
    factors.append(ways)
    i += 1

answer = 1
for x in factors:
    answer *= x

answer2 = 0

y = 0
for x in range(0, altContent["Time"]):
    if x * (altContent["Time"] - x) > altContent["Distance"]:
        y = x
        break

answer2 = altContent["Time"] + 1 - 2 * y
print(f"Q1: {answer}")
print(f"Q2: {answer2}")