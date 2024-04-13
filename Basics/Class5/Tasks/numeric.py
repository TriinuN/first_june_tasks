# Numeric - Write a Python program that accepts a string and calculates the number of digits and letters.
# Use this to help to understand if character is numeric: https://www.w3schools.com/python/ref_string_isnumeric.asp
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

sample_string = "Python 3.2"
letters = 0
numbers = 0
for char in sample_string:
    if char.isnumeric():
        numbers += 1
    elif char.isalpha():
        letters += 1

print("Letters", letters)
print("Digits", numbers)

# Kuidas tegin mina:
# text = "I love dessert icing cotton candy cookie cookie caramels. 547380"
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# numbers = '1234567890'
#
# digit_count = sum(1 for char in text if char in numbers)
# letter_count = sum(1 for char in text if char.lower() in alphabet)
#
# print(f"Digits {digit_count}")
# print(f"Letters {letter_count}")