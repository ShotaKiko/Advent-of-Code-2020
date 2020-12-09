from inputList import inputsList
#36845998
#533
weakSum = 36845998
weakIndex = inputsList.index(36845998)
print(weakIndex)
length = len(inputsList)

# sampleList = [ 35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576 ]
# weakSum = 127
# weakIndex = 14
# length = len(sampleList)

solutionList = None


def crackTheCode(array):
    for index in range(weakIndex):
        search = True
        num = array[index]
        contig = []
        indexIncrementor = 0
        while search == True:
            if not contig:
                # print("List Empty")
                contig.append(num)
                # print("INITIAL CONTIG", contig)
            elif sum(contig) > weakSum:
                break
            elif sum(contig) < weakSum:
                contig.append(array[index + 1 + indexIncrementor])
                indexIncrementor += 1
                # print("\nincremented", contig)
            elif sum(contig) == weakSum:
                print("CONTIG", contig)
                answer = contig.copy()
                answer.sort()
                print("Answer: ", answer)
                search = False
                solutionList = answer
    solutionList.sort()
    print("SOLUTION List", solutionList)
    smallest = solutionList[0]
    largest = solutionList[-1]
    print("ENCRyption sum: ", (smallest + largest))


# crackTheCode(sampleList)
crackTheCode(inputsList)