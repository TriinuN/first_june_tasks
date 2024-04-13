# Vowels - Write a program that will determine the number of vowels in a given string.
# vowels = ['a', 'e', 'i', 'o', 'u']
# Using text generators like this: https://cupcakeipsum.com/ Get a text and just assign it to a string variable in the
# program.
vowels = 'aeiou'
text = ("See on palju palju luhem lause, see on katsetamiseks.")
amount_of_vowels = 0

for char in text:
    if char.lower() in vowels:
        amount_of_vowels += 1

print(f"Number of vowels in the text: {amount_of_vowels}")

#Janeku versioon
# text = input("Enter text to count vowels: ")
# #text = "This is text for fast test !!!"
# vowels = ['a', 'e', 'i', 'o', 'u']
# count = 0
# a = 0
# e = 0
# i = 0
# o = 0
# u = 0
# other = 0
#
# for char in text.lower():
#     if char in vowels:
#         count += 1
#     match char:
#         case "a":
#             a += 1
#         case "e":
#             e += 1
#         case "i":
#             i += 1
#         case "o":
#              o += 1
#         case "u":
#             u += 1
#         case _:
#             other += 1
#
#
#
# print(f'This text have {count} vowels')
# print(f'a = {a}\n'
#       f'e = {e}\n'
#       f'i = {i}\n'
#       f'o = {o}\n'
#       f'u = {u}\n'
#       f'other = {other}')


#Kuidas tegin mina:
# def check(string, vowels):
#     final = [each for each in string if each in vowels]
#     print(len(final))
#     print(final)
#
#
# string = "I love dessert icing cotton candy cookie cookie caramels."
# vowels = "AaEeIiOoUu"
# check(string, vowels)