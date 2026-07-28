# print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

# input1 = input("Enter a number: ")
# input2 = input("Enter another number: ")
# input3 = input("Do you want to add, subtract, multiply, or divide these numbers? (only use symbols +,-,*,/): ")
# input4 = input("What is the temp outside (in Celsius)? ")

# if input3 == "+":
#     add = int(input1) + int(input2)
#     print(add)
# elif input3 == "-":
#     sub = int(input1) - int(input2)
#     print(sub)
# elif input3 == "*":
#     mul = int(input1) * int(input2)
#     print(mul)
# elif input3 == "/":
#     div = float(input1) / float(input2)
#     print(div)
# else:
#     print("Sorry we can't do that.")

# far = float(input4) * 9 / 5 + 32
# print(f"Temp outside in Fahrenheit: {far}")

mode = input("Select a mode (+, -, *, /, c2f): ")

if mode == "c2f":
    cel = float(input("Enter your temp in Celsius: "))
    far = cel * 9 / 5 + 32
    print(f"Temp outside in Fahrenheit is: {far}")

elif mode in ['+', '-', '*', '/']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if mode == "+":
        print(f"Result: {num1 + num2}")
    elif mode == "-":
        print(f"Result: {num1 - num2}")
    elif mode == "*":
        print(f"Result: {num1 * num2}")
    elif mode == "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Can't divide by zero!")

else:
    print("Error: Input is invalid!")