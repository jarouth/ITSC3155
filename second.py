def add(x, y):
    print(f"{x}+{y} equals {x+y}")

def subtract(x, y):
    print(f"{x}-{y} equals {x-y}")

def muliply(x, y):
    print(f"{x}*{y} equals {x*y}")

def divide(x, y):
    print(f"{x}/{y} equals {x/y}")

while (True):
    number1 = int(input("Please input the first number:"))
    number2 = int(input("Please input the second number:"))
    choice = int(input(
        "Please input \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for divison: \n "))
    if (choice == 1):
        add(number1, number2)
        break
    elif (choice == 2):
        subtract(number1, number2)
        break
    elif (choice == 3):
        muliply(number1, number2)
        break
    elif (choice == 4):
        divide(number1, number2)
        break
    else:
        print("You have input an invalid number, please retry")
