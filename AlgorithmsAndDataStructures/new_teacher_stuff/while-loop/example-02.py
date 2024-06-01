# 1 Accept input from user
# 2 If the input is equal to "exit", program should terminate and print out provided input and Done
# 3 If the input is equal to "exit-no-print", program terminate without printing out anything
# 4 If the input is equal to "no-print", program moves to next loop iteration without printing anything
# 5 If the input is different then "exit", "exit-no-print" and "no-print", program repeats
user_input = ""
while user_input != "exit":     # is not exit
    user_input = input("Provide input: ")
    if user_input == "exit-no-print":   # 3
        break
    if user_input == "no-print":    # 4
        continue
    print(user_input)   # 2
else:   # 2
    print("Done.")
