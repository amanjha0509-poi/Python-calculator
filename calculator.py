import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def inverse(x):
    if x == 0:
        return "Error: Division by zero"
    return 1 / x

print("Scientific Calculator")
print("----------------------")

while True:
    print("\nOperations:")
    print("1. +  (Addition)")
    print("2. -  (Subtraction)")
    print("3. *  (Multiplication)")
    print("4. /  (Division)")
    print("5. sin")
    print("6. cos")
    print("7. tan")
    print("8. inverse (1/x)")

    choice = input("Choose operation (1-8): ")

    try:
        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            elif choice == "4":
                print("Result:", divide(num1, num2))

        elif choice in ["5", "6", "7", "8"]:
            num = float(input("Enter number (angle in degrees for trig): "))

            if choice == "5":
                print("Result:", sine(num))
            elif choice == "6":
                print("Result:", cosine(num))
            elif choice == "7":
                print("Result:", tangent(num))
            elif choice == "8":
                print("Result:", inverse(num))

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    again = input("Do you want to continue? (y/n): ")
    if again.lower() != "y":
        print("Calculator closed.")
        break
