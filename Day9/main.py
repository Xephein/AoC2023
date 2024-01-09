import time

def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

def diffCalc(inpArray, deltas):
    currDiffs = []
    i = 0
    while i < len(inpArray):
        if i + 1 < len(inpArray):
            currDiffs.append(inpArray[i + 1] - inpArray[i])
        i += 1
    deltas.append(currDiffs)
    for x in currDiffs:
        if x != 0:
            diffCalc(currDiffs, deltas)
            break
    return deltas


content = readTXT("input.txt")

ans = []
ans2 = []
i = 0
while i < len(content):
    content[i] = [[int(x) for x in content[i].split(" ")]]
    deltas = diffCalc(content[i][0], [])
    for x in deltas:
        content[i].append(x)
    j = 1
    a = 0
    b = 0
    while j <= len(content[i]):
        a = a + content[i][-j][-1]
        b = content[i][-j][0] - b
        if j == len(content[i]):
            ans.append(a)
            ans2.append(b)
        j += 1
    i += 1

print(f"Q1: {sum(ans)}")
print(f"Q2: {sum(ans2)}")