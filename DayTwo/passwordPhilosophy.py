from passwordsList import passwordList

smallSample = [
"1-3 a: abcde",
"1-3 b: cdefg",
"2-9 c: ccccccccc"
]

def findValidPasswordCount(array):
    validPasswordCount = 0
    
    for passwordEntry in array:        
        firstSplit = passwordEntry.split()
        # print("First", firstSplit)
        secondSplit = firstSplit[0].split("-")
        # print("Second", secondSplit)
        
        minOccur = int(secondSplit[0])
        maxOccur = int(secondSplit[1])
        # print(minOccur)
        # print(maxOccur)
        
        letterSplit = firstSplit[1].split(":")
        letterTarget = letterSplit[0]
        # print("Letter Target", letterTarget)

        actualPassword = firstSplit[2]
        print("Pass", actualPassword) 

        occurence = 0
        for char in actualPassword:
            if char == letterTarget:
                occurence += 1

        if occurence >= minOccur and occurence <= maxOccur:
            validPasswordCount += 1
    
    print("Valid Password Count:", validPasswordCount)

                

findValidPasswordCount(smallSample)
# findValidPasswordCount(passwordList)