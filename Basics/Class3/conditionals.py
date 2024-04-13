# String IF statement
if "this" in "This text is this": #if u take away this then it dont print
    print("It is in there.")


# elif usage example. Note there can be unlimited amount of elif
number = 1
if number > 2:
    number -= 1
elif number < 2:
    number += 5
else:
    print("You are on your own")

print(number)
print()
# Most common simple use
number2 = int(input())
if number2 > 5:
    print("Do this")
else:
    print("Do another")
print()
#Multiple conditions in one if line
if number2 >= 5 and not (number2 <=1 or number2 == "Some text"):
    print("Do this")
else:
    print("Do another")
# Examples of and And or
# c1 = True and True #True
# c2 = True and False #False
# c3 = False and True #False
# c4 = False and False #False
#
# c5 = True or True #True
# c6 = True or False #True
# c7 = False or True #True
# c8 = False or False #False


user_input = int(input("What is your age: "))
if user_input <= 18:
    print("Here have some fun")
else:
    print("Nah Brah")

print("success case") if user_input <= 18 else print("Fail case")  #only for most simple things

