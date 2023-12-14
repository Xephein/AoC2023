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
for seed in seeds:
    num = int(seed)
    for map in maps:
        var1 = map["map"].split("-to-")[0]
        var2 = map["map"].split("-to-")[1]
        p = 0
        while p < len(map[var2]):
            var1Bigger = num >= map[var1][p]
            var1Smaller = num < map[var1][p] + map["length"][p]
            if var1Bigger and var1Smaller:
                num = map[var2][p] + (num - map[var1][p])
                break
            p += 1
    locations.append(num)

print(min(locations))
# X(source)-to-Y(destination) map:
# destination start, source range start, range length

