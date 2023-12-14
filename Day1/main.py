NUMBERS = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}

def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

def textToNum(inputStr):
    for num in list(NUMBERS.keys()):
        inputStr = inputStr.replace(num, str(NUMBERS[num]))
    return inputStr

def getDigits(inputArray):
    digitArray = []
    for row in inputArray:
        tempString = ""
        row = textToNum(row)
        for letter in row:
            if letter.isnumeric():
                tempString += letter
        digitArray.append([int(tempString[0]), int(tempString[-1])])
    return digitArray

content = readTXT("input.txt")
digits = getDigits(content)

answer = 0
for row in digits:
    answer += 10 * row[0]
    answer += row[1]

print(answer)