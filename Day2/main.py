COLORS = {
    "red": 12,
    "green": 13,
    "blue": 14
    }

def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

def colorCheck(colorNum):
    for color in list(COLORS.keys()):
        if color in colorNum:
            number = int(colorNum.split(" " + color)[0])
            if COLORS[color] < number:
                return False
    return True

def dieCounter(colorNum, colorCount):
    color = colorNum.split(" ")[1]
    num = int(colorNum.split(" ")[0])
    if num > colorCount[color]:
        colorCount[color] = num
    return colorCount


content = readTXT("input.txt")

walk = []
for row in content:
    row = {"id": int(row.split(": ")[0].split(" ")[1]), "draws": row.split(": ")[1].split("; "), "toCount": True}
    result = True
    for i in range(0,len(row["draws"])):
        row["draws"][i] = row["draws"][i].split(", ")
        if result == True:
            for colorCombo in row["draws"][i]:
                result = colorCheck(colorCombo)
                if result == False:
                    row["toCount"] = False
                    continue
        else:
            continue

    walk.append(row)
        
answer1 = 0
answer2 = 0
for game in walk:
    currentDie = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for draws in game["draws"]:
        for colorCombo in draws:
            currentDie = dieCounter(colorCombo, currentDie)
    answer2 += currentDie["red"] * currentDie["green"] * currentDie["blue"]
    if game["toCount"] == False:
        continue
    else:
        answer1 += game["id"]

print(answer1)
print(answer2)