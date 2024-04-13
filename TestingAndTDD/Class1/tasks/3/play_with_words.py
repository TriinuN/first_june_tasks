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