# passportList = [
# "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
# "byr:1937 iyr:2017 cid:147 hgt:183cm",
# "",
# "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
# "hcl:#cfa07d byr:1929",
# "",
# "hcl:#ae17e1 iyr:2013",
# "eyr:2024",
# "ecl:brn pid:760753108 byr:1931",
# "hgt:179cm",
# "",
# "hcl:#cfa07d eyr:2025 pid:166559648",
# "iyr:2011 ecl:brn hgt:59in"
# ]

# emptyLine = "                                      "
from passList import inputList


def calcValidPassports(array):
    #print(passportList)
    passDict = {}
    validCount = 0
    for line in array:
        if line:
            # print("Line: ", line)
            fields = line.split(" ")
            # print("Fields: ",fields)
            
            for field in fields:
                subList = field.split(":")
                key = subList[0]
                value = subList[1]
                passDict[key] = value
                # print("Keys: ", key)

        else:
            if "byr" in passDict and "iyr" in passDict and "eyr" in passDict and "hgt" in passDict and "hcl" in passDict and "ecl" in passDict and "pid" in passDict:
                 validCount += 1
                 print("Dictionary:", passDict)
                 print("Count", validCount)
            passDict.clear()
            print("~~~~~~~~~~~~~~~~~~~~NEW~~~~~~~~~~~~~~~~~")
    print(validCount + 1) # + 1 because input doesnt end with an empty line so the last entry if valid will never get added to count



#calcValidPassports(passportList)
calcValidPassports(inputList)