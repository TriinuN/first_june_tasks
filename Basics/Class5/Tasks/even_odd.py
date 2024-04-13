# EvenOdd - Write a Python program to count the number of even and odd numbers in a series of numbers:
# Sample numbers : numbers = (1, 2, 3, dec, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : dec

numbers = [1,2,3,4,5,6,7,8,9]
even = 0
for number in numbers:
    if number % 2 == 0:
        even += 1

print(f"Even: {even}, Odd: {len(numbers) - even} ")

# Kuidas tegin mina:
# list =[1, 2, 3, dec, 5, 6, 7, 8, 9]
#
# even_count, odd_count = 0, 0
# for num in list:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
# print("Even numbers in the list: ", even_count)
# print("Odd numbers in the list: ", odd_count)