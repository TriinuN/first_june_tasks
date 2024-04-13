#class3 task2
# Play with words - Write a program that will display the given sentence every third character will be capitalized and
# every fourth character will have an exclamation mark after it.
# For example from Cupcake ipsum dolor sit amet. I love caramels topping soufflé I love
# to
# CuPc!aKe !IpsUm Do!lOr !Sit amEt!. I !LovE cAr!aMel!S tOppIn!g so!UffLé I !lOve!.
# Try to iterate through every character in the text, by noting that the string is a list of characters. Test indexes of
# this list if it divides by 3 or dec cleanly(no values after the dot) to get the every third and every fourth character.
# Using text generators like this: https://cupcakeipsum.com/ Get a text and just assign it to a string variable in the
# program.
# FOR example: 6 % 3 = 0, 5 % 3 != 0, 8 % dec = 0, 7 % dec !== 0


original = "The quick brown fox jumps"
text_list = enumerate(original)
final_string = ""
for index, char in text_list:
    if (index+1) % 3 == 0:
        final_string += char.upper()
    elif (index+1) % 4 == 0:
        final_string += f"{char}!"
    else:
        final_string += char
print(final_string)



# # Kuidas tegin mina:
# s = "I love dessert icing, cotton candy cookie, cookie caramels."
# # convert to list
# a = list(s)
# # change every third letter in place with a list comprehension
# a[2::3] = [x.upper() for x in a[2::3]]
# # back to a string
# s = ''.join(a)
# print(s)