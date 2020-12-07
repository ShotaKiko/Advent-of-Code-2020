from expenseList import expenses
# O(n) time and O(n) space
def twentyTwentyTwoNumSum(array,targetSum): 
    expensesDict = {}
    for expense in array:
        remainder = targetSum - expense
        if remainder in expensesDict:
            print("The product is: ", remainder * expense)
            return[remainder * expense]
        else:
            expensesDict[expense] = True
    print("No two expenses matched target sum")

twentyTwentyTwoNumSum(expenses, 2020)