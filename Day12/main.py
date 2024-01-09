import re
import time

def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

content = readTXT("test.txt")

for row in range(0, len(content)):
    content[row] = [content[row].split(" ")[0], content[row].split(" ")[1]]
    content[row][1] = [int(x) for x in content[row][1].split(",")]

print(content)

variations = 0

for springs in range(0, len(content)):
    arrangement = content[springs][0]
    code = content[springs][1]
    if len(arrangement) == sum(code) + len(code) - 1:
        variations += 1
    else:
        arrangement = content[springs][0]
        islands = re.findall("[?#]+", arrangement)
        i = 0
        while i < len(islands):
            pass
        print(islands)


print(f"Q1: {variations}")