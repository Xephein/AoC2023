
def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

def checkForSymbol(sN, cont, row, col, rowUp, colUp):
    symb = None
    for x in range(-1,2):
        for y in range(-1,2):
            if ((row + x) >= 0 and (row + x) < rowUp) and (col + y) >= 0 and col + y < colUp:
                if cont[row + x][col + y].isdecimal() == False and cont[row + x][col + y] != ".":
                    sN = True
                    symb = {"symbol": cont[row + x][col + y], "symbI": int(row + x), "symbJ": int(col + y)}
            y += 1
        x += 1
    return [sN, symb]

content = readTXT("input.txt")
rowNum = len(content)
colNum = len(content[0])


answer = 0
gearArr = []

i = 0
while i < rowNum:
    j = 0
    while j < colNum:
        currNum = 0
        if content[i][j].isdecimal():
            symbNeighbor = False
            while content[i][j].isdecimal():
                if symbNeighbor == False:
                    symbolStuff = checkForSymbol(symbNeighbor, content, i, j, rowNum, colNum)
                    # Get info on whether number had symbol neighbor
                    symbNeighbor = symbolStuff[0]
                    if symbNeighbor:
                        symbInfo = symbolStuff[1]

                currNum *= 10
                currNum += int(content[i][j])
                if j + 1 < colNum:
                    j += 1
                else:
                    break
            if symbNeighbor == True:
                answer += currNum
                if symbInfo["symbol"] == "*":
                    registered = False
                    gearC = 0
                    while gearC < len(gearArr):
                        if gearArr[gearC]["i"] == symbInfo["symbI"] and gearArr[gearC]["j"] == symbInfo["symbJ"]:
                            gearArr[gearC]["numbers"].append(currNum)
                            registered = True
                        gearC += 1
                    if registered == False:
                        gearArr.append({"i": symbInfo["symbI"], "j": symbInfo["symbJ"], "numbers": [currNum]})
        j += 1
    i += 1

prodSum = 0
for asterisk in gearArr:
    nums = asterisk["numbers"]
    if len(nums) == 2:
        prodSum += (nums[0] * nums[1])

print(answer)
print(prodSum)