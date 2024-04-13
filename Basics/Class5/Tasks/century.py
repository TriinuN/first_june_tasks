# Century - Introduction The first century spans from the year 1 up to and including the year 100, the second century -
# from the year 101 up to and including the year 200, etc. Task Given a year, print the century it is in.
# The year would be passed by user input

year = int(input("Enter a year: "))

if year < 1:
    print("Nice! You are not even in a first century yet!")
else:
    print(f"You are in the {((year-1)//100) + 1} century")

# Kuidas tegin mina:
# # Get the year from the user
# year = int(input("Enter a year: "))
#
# # Calculate the century
# century = (year - 1) // 100 + 1
#
# # Print the result
# print(f"The century of the year {year} is {century}.")