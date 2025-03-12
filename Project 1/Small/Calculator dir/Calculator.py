#Basic Caculator
print("Basic Calculator:")

firstNum = int(input("Enter your first number: "))
secondNum = int(input("Enter your second number: "))
operator = input("Enter your Operator (+, -, *, /): ")

if operator == '+':
    print("Answer: ", firstNum + secondNum)
elif operator == '-':
    print("Answer: ", firstNum - secondNum)
elif operator == '*':
    print("Answer: ", firstNum * secondNum)
elif operator == '/':
    print("Answer: ", firstNum / secondNum)
else:
    print("Invalid Operator!")