from inputList import inputsList
from inputList import preambleNum

#Preamble for sample is 5 numbers ----127 here
samplePreamble = 5
sampleList = [ 35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576 ]


def timeToHack(array, preamble):
    collection = []
    weakLink = []
    for index in range(len(array)):
        number = array[index]
        
        if index <= (preamble - 1):
            print("Still in the preamble numbers\n")
            collection.append(number)
        
        else:
            print("\nCurrent Collection", collection)
            sumWindow = collection.copy()
            sumWindow.sort()
            print("SumWindow", sumWindow)
            collectionLength = len(collection)
            print("length", collectionLength)
            
            left = 0
            right = collectionLength - 1
            targetSum = number
            status = True

            while status == True:
                print("\nwindow at Left", sumWindow[left])
                print("window at Right", sumWindow[right])
                currentSum = sumWindow[left] + sumWindow[right]
                if currentSum == targetSum:
                    print("Sum found for this number: ", number)
                    break
                elif left == right:
                    print("The weakest link is the number: ", number)
                    status == False
                    weakLink.append(number)
                    break
                elif currentSum > targetSum:
                    right -= 1
                elif currentSum < targetSum:
                    left += 1
            #adjustment of window
            collection.pop(0)
            collection.append(number)
            print("\n\nNEW collection: ", collection)
            print("THE WEAK LINK: ", weakLink)

# timeToHack(sampleList, samplePreamble)
timeToHack(inputsList, preambleNum)