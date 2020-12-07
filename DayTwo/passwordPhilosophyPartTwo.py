from passwordsList import passwordList

smallSample = [
"1-3 a: abcde",
"1-3 b: cdefg",
"2-9 c: ccccccccc"
]

# XOR (a and not b) or (not a and b)
def findValidPasswordCount(array):
    validPasswordCount = 0
    
    for passwordEntry in array:        
        firstSplit = passwordEntry.split()
        # print("First", firstSplit)
        secondSplit = firstSplit[0].split("-")
        # print("Second", secondSplit)
        
        minIndex = int(secondSplit[0])
        maxIndex = int(secondSplit[1])
        # print(minIndex)
        # print(maxIndex)
        
        letterSplit = firstSplit[1].split(":")
        letterTarget = letterSplit[0]
        # print("Letter Target", letterTarget)

        actualPassword = firstSplit[2]
        # print("Pass", actualPassword) 

        firstValid = False
        secondValid = False

        if actualPassword[minIndex - 1] == letterTarget:
            firstValid = True
        if actualPassword[maxIndex - 1] == letterTarget:
            secondValid = True
        
        if (firstValid and not secondValid) or (secondValid and not firstValid):
            validPasswordCount += 1

        
    
    print("Valid Password Count:", validPasswordCount)

                

# findValidPasswordCount(smallSample)
findValidPasswordCount(passwordList)