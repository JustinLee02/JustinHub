userInput = 'y'
result = 0
def my_operator(num1, num2, useroperator):
    if useroperator == '+':
        return num1 + num2
    elif useroperator == '-':
        return num1 - num2
    elif useroperator == '*':
        return num1 * num2
    else :
        return num1 / num2


firstNum = int(input("What's the fisrt number?: "))
while userInput == 'y':
    print("+\n-\n*\n/")
    userOperator = input("Pick an operation: ")
    secondNum = int(input("What's the next number?: "))
    firstNum = my_operator(firstNum,secondNum,userOperator)
    print(firstNum)
    userInput = input(f"Type 'y' to continue calculating with {firstNum}, or type 'n' to restart a new calculation ")