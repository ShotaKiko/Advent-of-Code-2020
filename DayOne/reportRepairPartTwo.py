from expenseList import expenses
#ES NO BUENO O(n^2)!! but best I could come up with 
#O(n) space
def twentyTwentyThreeNumSum(array, targetSum):
    array.sort()
    for i in range(len(array) - 2):
        leftPointer = i + 1
        rightPointer = len(array) - 1
        while leftPointer < rightPointer:
            firstValue = array[i]
            secondValue = array[leftPointer]
            thirdValue = array[rightPointer]

            currentExpenseSum = firstValue + secondValue + thirdValue
            if currentExpenseSum == targetSum:
                print("The product is: ", firstValue * secondValue * thirdValue)
                expenseTriplet = [firstValue, secondValue, thirdValue]
                return expenseTriplet
            elif currentExpenseSum < targetSum:
                leftPointer += 1
            elif currentExpenseSum > targetSum:
                rightPointer -= 1
    print("No three num sum was found")

twentyTwentyThreeNumSum(expenses, 2020)
