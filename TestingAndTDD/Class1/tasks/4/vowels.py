vowels = 'aeiou'
text = ("See on palju palju luhem lause, see on katsetamiseks.")
amount_of_vowels = 0

for char in text:
    if char.lower() in vowels:
        amount_of_vowels += 1

print(f"Number of vowels in the text: {amount_of_vowels}")