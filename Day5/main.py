import re

def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

content = readTXT("hell.txt")

k = 0
coordinates = []
while k < len(content):
    a = re.findall(".+-to-.+", content[k])
    if a != []:
        a = a[0].split(" map:")[0]
        tempDict = {"map": a,
                    "destinations": [],
                    "sources": [],
                    "ranges": [],
                    }
        while k + 1 < len(content) and content[k + 1] != '':
            k += 1
            row = content[k].split(" ")
            tempDict["destinations"].append(row[0])
            tempDict["sources"].append(row[1])
            tempDict["ranges"].append(row[2])
        coordinates.append(tempDict)
    elif "seeds: " in content[k]:
        seeds = content[k].split("seeds: ")[1].split(" ")
    k += 1

maps = []
i = 0
while i < len(coordinates):
    mapName = coordinates[i]["map"]
    sourcName = mapName.split("-to-")[0]
    destName = mapName.split("-to-")[1]
    maps.append({"map": mapName, 
                destName: [],
                sourcName: [],
                "length": []
                })
    j = 0
    while j < len(coordinates[i]["destinations"]):
        dest = int(coordinates[i]["destinations"][j])
        sourc = int(coordinates[i]["sources"][j])
        rang = int(coordinates[i]["ranges"][j])
        maps[i][destName].append(dest)
        maps[i][sourcName].append(sourc)
        maps[i]["length"].append(rang)
        j += 1
    i += 1

locations = []
l = 0

seeds2 = []
l = 0
while l < len(seeds):
    if l % 2 == 0:
        seeds2.append({
            "start": int(seeds[l]),
            "end": int(seeds[l]) + int(seeds[l + 1]) - 1,
        })
    l += 1

print(seeds2)

seedsToCheck = seeds2.copy()
i = 0
while i < len(seedsToCheck):
    seedsToCheck[i]["difference"] = 0
    i += 1

i = 0
while i < len(maps):
    sourceName = maps[i]["map"].split("-to-")[0]
    destinationName = maps[i]["map"].split("-to-")[1]
    j = 0
    while j < len(seedsToCheck):
        k = 0
        while k < len(maps[i][sourceName]):
            compareTo = maps[i][sourceName]
            lengths = maps[i]["length"]
            connedDest = maps[i][destinationName]
            if seedsToCheck[j]["start"] < compareTo[k] and \
                seedsToCheck[j]["end"] > compareTo[k]:
                seedsToCheck.append({"start": compareTo[k],
                                    "end": seedsToCheck[j]["end"],
                                    "difference": 0
                                    })
                seedsToCheck[j]["end"] = compareTo[k] - 1

            if seedsToCheck[j]["start"] >= compareTo[k] and \
                seedsToCheck[j]["end"] < compareTo[k] + lengths[k]:
                seedsToCheck[j]["difference"] = connedDest[k] - compareTo[k]
            k += 1
        j += 1
    l = 0
    while l < len(seedsToCheck):
        seedsToCheck[l]["start"] += seedsToCheck[l]["difference"]
        seedsToCheck[l]["end"] += seedsToCheck[l]["difference"]
        seedsToCheck[l]["difference"] = 0
        l += 1
    i += 1

answers = []
for x in seedsToCheck:
    answers.append(x["start"])


for seed in seeds:
    num = int(seed)
    for mapl in maps:
        var1 = mapl["map"].split("-to-")[0]
        var2 = mapl["map"].split("-to-")[1]
        p = 0
        while p < len(mapl[var2]):
            var1Bigger = num >= mapl[var1][p]
            var1Smaller = num < mapl[var1][p] + mapl["length"][p]
            if var1Bigger and var1Smaller:
                num = mapl[var2][p] + (num - mapl[var1][p])
                break
            p += 1
    locations.append(num)
    l += 1
print(f"Q1: {min(locations)}")
print(f"Q2: {min(answers)}")


# X(source)-to-Y(destination) map:
# destination start, source range start, range length