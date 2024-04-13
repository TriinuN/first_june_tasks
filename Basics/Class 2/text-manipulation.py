example_text = "blood type is Beer!"

# Length of the string  # lugemine algab alati 0st
lenght = len(example_text)
print(lenght)
print("")
# What is the index of this character(first one)
print(f"Position of letter 'y' in the text is {example_text.index('y')}")
print("")
# What is the amount of letters in this text
print(f"Amount of 'B' in the text is {example_text.count('B')}")
print("")
# What is the character at the index 6
print(f"The character at the index 6 is {example_text[6]}")
print("")
# What are the characters at the index range
print(f"The text in the range is' {example_text[6:13]}'")
print(f"The text in the range is {example_text[6:16]}")
print("")
# What are the every second character in the index range
print(f"The text in the range is' {example_text[6:13:2]}'")
print(f"The text in the range is' {example_text[::2]}'")
# text[fromIndextoIndex:step]
print("")
# String reversed
print(f"This is a reversed text {example_text[::-1]}")
print("")
# Upper/Lower case
print(example_text.lower())
print(example_text.upper())
print(example_text.capitalize())
