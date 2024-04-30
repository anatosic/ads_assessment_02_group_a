"""
Simple Calculator
"""
# Provide your solution here

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
operator = input("choose a string operator (-, +, * or /): ")
def calculate(num1: int, num2:int, operator):
    print("calculate(" + num1 + ", " + num2 + ", " + operator)
def add(x, y):
    return x + y
result = add(x = num1, y = num2)
print(result)
def subtract(x, y):
    return x - y
result = subtract(x = num1, y = num2)
print(result)
def multiply(x, y):
    return x * y
result = multiply(x = num1, y = num2)
print(result)
def divide(x, y):
    return x / y
result = divide(x = num1, y = num2)
print(result)


while True:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    operator = input("choose a string operator (-, +, * or /): ")

    if num2 in calculate == 0:
        print("Division by 0 is not allowed.")
    elif operator != "-" or "+" or "*" or "/":
        print("Invalid operator.")
    elif operator == "+":
        print(add)
        break
    elif operator == "-":
        print(subtract)
        break
    elif operator == "*":
        print(multiply)
        break
    elif operator == "/":
        print(divide)
        break
print()
"""
Reverse Word
"""
# Provide your solution here

word = str(input("enter a word: "))
print(word [::-1])

def reversed_word(word):
    word = word.upper(0)

print()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")


