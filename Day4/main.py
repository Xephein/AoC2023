def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

content = readTXT("input.txt")

i = 0
answer = 0

while i < len(content):

    content[i] = content[i].split(": ")
    content[i] = {"id": content[i][0].split(" ")[1],
                "winning": content[i][1].split(" | ")[0],
                "numbers": content[i][1].split(" | ")[1],
                "copies": 1,
                "wins": 0
                }
    content[i]["winning"] = content[i]["winning"].split(" ")
    content[i]["numbers"] = content[i]["numbers"].split(" ")
    
    winningCount = content[i]["winning"].count("")
    numbersCount = content[i]["numbers"].count("")
    j = 0
    while j < winningCount:
        content[i]["winning"].remove("")
        j += 1
    j = 0
    while j < numbersCount:
        content[i]["numbers"].remove("")
        j += 1

    value = 0
    for winner in content[i]["winning"]:
        if winner in content[i]["numbers"]:
            content[i]["wins"] += 1
            if value == 0:
                value += 1
            else:
                value *= 2
    answer += value
    # next line
    i += 1

numberOfCards = 0
i = 0
while i < len(content):
    for j in range(0, content[i]["wins"]):
        content[i + j + 1]["copies"] += 1 * content[i]["copies"]
    numberOfCards += content[i]["copies"]
    i += 1


print(answer, numberOfCards)
