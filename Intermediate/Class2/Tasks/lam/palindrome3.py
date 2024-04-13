def reverse_string(text):
    return text[::-1]


my_list = ["rotor", "level", "radar", "mama"]

palindrome_words = filter(lambda x: x == reverse_string(x), my_list)
palindrome_list = list(palindrome_words)

print("Palindrome words:", palindrome_list)
