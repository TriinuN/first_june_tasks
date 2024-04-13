# Write a program that would ask user to input text and print the amount of times the first character of user
# entered text is repeated.
Question = str(input("What is programming?"))
answer = 'Programming is the mental process of thinking up instructions to give to a machine (like a computer).'

print(f"Amount of letter 'o' in the text is {answer.count('o')}")


print(f"The amount of {answer[0]} in the provided answer is: {answer.count(answer[0])}")