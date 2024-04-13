# Calculator 2.0 - Create a calculator that would ask user for first number, action, second number, than do the action,
# display the result, ask user if he would like to do more actions: if yes, start the program again. if no, terminate the
# program. (Calculator should handle at least +-/*)
print("Welcome to calculator 2.0")

while True:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    action = input("select the action to do: \n"
                   "a- Add \n"
                   "s- Subtract \n"
                   "m- Multiply \n"
                   "d- Divide \n"
                   ":")

    if action == "a":
        print(f"The sum of these numbers is", number1 + number2)
    elif action == "s":
        print(f"The subtraction result of these numbers is", number1 - number2)
    elif action == "d":
        print(f"The division result of these numbers is", number1 / number2)
    elif action == "m":
        print(f"The multiplication result of these numbers is", number1 * number2)
    is_again = input("Would you like to do one more? Y or N: ")
    if is_again == "Y":
        continue
    break

# Kuidas tegin mina:
# print("Hello to calculator 2.0")
#
# def calculator():
#     number1_input = int(input("Please enter a number1: "))
#     number2_input = int(input("Please enter a number2: "))
#     user_input = input("a - for addition, s - for subtraction, u - for dividing, t - for multiplication, x - to Quit: ")
#
#     if user_input == "a":
#         print(f"{number1_input} + {number2_input} = {number1_input + number2_input}")
#     elif user_input == 's':
#         print(f"{number1_input} - {number2_input} = {number1_input - number2_input}")
#     elif user_input == 'u':
#         if number2_input != 0:
#             print(f"{number1_input} / {number2_input} = {number1_input / number2_input}")
#         else:
#             print("Cannot divide by zero!")
#     elif user_input == 't':
#         print(f"{number1_input} * {number2_input} = {number1_input * number2_input}")
#     elif user_input == 'x':
#         print("Thank you for using")
#         return
#     else:
#         print("Text was wrong, try one of the possible options")
#
#     action_input = input("Would you like to start again? Enter 'y' for Yes, 'n' for No: ")
#     if action_input == 'y':
#         calculator()
#     elif action_input == 'n':
#         print("Thank you for using")
#
# calculator()