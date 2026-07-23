def transform(legacydata):
    newvalues = {}
    for number in legacydata:
        for letter in legacydata[number]:
            newvalues[letter.lower()] = number
    
        
    return newvalues



legacydata = {
1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
2: ["D", "G"],
3: ["B", "C", "M", "P"],
4: ["F", "H", "V", "W", "Y"],
5: ["K"],
8: ["J", "X"],
10: ["Q", "Z"],
    }


print(transform(legacydata))