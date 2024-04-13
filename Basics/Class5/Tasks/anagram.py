# Anagram Checker:
# Create a function that checks if two given strings are anagrams of each other. Allow the user to input
# two strings and use the function to determine if they are anagrams.
def is_anagram(first, second):
    if sorted(first) == sorted(second):
        return True
    return False


text1 = input("Enter the first word: ")
text2 = input("Enter the second word: ")

if is_anagram(text1, text2):
    print("Anagram")
else:
    print("Not Anagram")








#text = "The quick brown fox jumps over the fence."
# print(sorted(text))
#
# if sorted('The quick brown fox jumps over the fence.') == sorted('The quick brown fox jumps over the fence.'):
#     print("Yes")
#
# text = "cba"
# print(sorted(text))
# if sorted('cba') == sorted('bac'):
#     print("Yes")