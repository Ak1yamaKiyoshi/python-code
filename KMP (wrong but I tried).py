def kmp(string, substring, prefix=0, stringIndex=0):
    listOfMatches = []
    for x in range(len(string)):
        prefix = 0
        while prefix < len(substring):
            if substring[0:prefix] == string[stringIndex:stringIndex + prefix]:
                prefix += 1
                if substring == string[stringIndex:stringIndex + prefix]:
                    listOfMatches.append([stringIndex, stringIndex + prefix])
                if stringIndex >= len(string):
                    return listOfMatches
            else:
                stringIndex += prefix
                prefix = 0
        stringIndex += prefix


txt = "aasdasdasdaaasdasddfaa"

print(kmp(txt, "aa"))
