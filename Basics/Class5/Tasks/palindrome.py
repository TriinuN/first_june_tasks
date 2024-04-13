# Palindrome Checker: Create a function that checks if a given string is a palindrome
# (reads the same backward as forward).
# Use this function to check whether a user-inputted string is a palindrome.
# kuulilennuteetunneliluuk

def reverse_string(text):
    return text[::-1]

check_text = input("Check if this is a palindrome: ")

if check_text == reverse_string(check_text):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

