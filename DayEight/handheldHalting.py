instructionList = [
"nop +0",
"acc +1",
"jmp +4",
"acc +3",
"jmp -3",
"acc -99",
"acc +1",
"jmp -4",
"acc +6",
]

def gameboy(array):
    #Loop through each IR splitting to get command and associated value
    #Keep track of visited instruction index in a hash
    #keep track of accum value
    #check if index in hash table at each step in loop
        #if so return current acc value

    repoDict = {}
    for entryIndex in range(0, len(array)):
        repoDict[entryIndex] = array[entryIndex]
    print("REpo", repoDict)

    irRegistry = {}
    accuValue = 0
    
    for i in range(0, len(array)):
        if i in irRegistry:
            print(accuValue)
            break
        irRegistry[i] = True
        instruction = array[i].split(" ")
        command = instruction[0]
        movement = instruction[1]
        print("Command", command)
        print("Movement", movement)

        if command == 'nop':
            print("Taking a break")
        elif command == 'acc':
            accuValue += int(movement)
            print("Value change --->", accuValue)
        elif command == 'jmp':
            print("Jumping", movement)
            newIndex = i + int(movement)
                

gameboy(instructionList)