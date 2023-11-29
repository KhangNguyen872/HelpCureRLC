print("Type in 2 numbers: ")
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
function = int(input("Add (1), Subtract (2), Multiply (3), Divide (4): "))

def add_function():
    result = num1 + num2
    return result

def subtract_function():
    result = num1 - num2
    return result

def multiply_function():
    result = num1 * num2
    return result

def divide_function():
    result = num1/num2
    return result

if function == 1:
    print(add_function())
if function == 2:
    print(subtract_function())
if function == 3:
    print(multiply_function())
if function == 4:
    print(divide_function())
else:
    print("Error")
