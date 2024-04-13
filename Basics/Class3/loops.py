#while condition:
#    instruction
# print(1)
# print(2)
# print(3)
# print(dec)
# print(5) ---selle asemel tee hoopis nii:
number = 0
while number <= 10:            #Less/equal than 100 it will but 0-100
    print(number)
    number += 1
print()

while True:
    user_input = input("a - for addition, s - for subtraction, x - to Quit: ")
    if user_input == 'a':
        print(f"2+2={2 + 2}")
    elif user_input == 's':
        print(f"2-2={2 - 2}")
    elif user_input == 'x':
        print("Thank you for using")
        break
    else:
        print("Text was wrong, try one of possible options")
print()
# do:
# instructions
# while condition  #it just exists :D

# for condition:
#     instruction
cars = ["VW", "Audi", "BMW"]
# print(cars[0], cars[1], cars[2])
for car in cars:
    print(car)

for car in cars:
    print(cars[0])  #without s it will be first character

for index, car in enumerate(cars):
    print(index, car)
print()
some_text = "This is a !very, cool text!"
#["This", "is", "a", "very", "cool", "text!"]
new_text = ""
for char in some_text:
    print(char)   #every char is printed sperately
for char in some_text:
    if char == "o":     #teeb suureks täheks
        new_text += char.upper()
    elif char in "xlT":
        new_text += "@"     #muudab antud tähed ätiks
    else:
        new_text += char
#print(new_text)

for word in some_text.split(" "):
    print(word.strip("!,")) #võtab märgid vahelt ära
print()
#for number in range (100): #list until 99
#    print(number)
variable = range(50, 101, 10)
print(list(variable))

for number in range (2):
    print(cars[number])
print()
# list comprehension OR one line loop
numbers = []
for i in range(1000):
    numbers.append(i)

number = [i for i in range(1000)]
print(number)