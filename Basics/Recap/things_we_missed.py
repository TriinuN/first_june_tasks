print("Hello World!")

variable1 = 15
variable2 = "String value test test test test test as test!"
variable3 = 15.5363
variable4 = True

# integer(int), float, string(str), boolean(bool), None, undefined
int(variable3)
float(variable1)

print(type(variable1)) # Getting a type of a variable
print(type(variable2))
print(type(variable3))
print(type(variable4))


len(variable2)
new_words = [] #initiate empty list
for word in variable2.split():  #iterate thought words
    new_words.append(word.strip('e')) # append list with striped e from start and end of words
new_words = ' '.join(new_words) # Converting list to text
print(new_words)

list_variable = [{}, {}, {}]
dictionary = {'key': [{'key': [{}, {}]}]}
#
# user_choice = input("Choose one of the following: a;fgdsg \n")
#
# # 0, '', null, undefined, [], {} = Falsy
# # 1, ' ', [0], {"key":"value"} = Truthy
#
# if user_choice:
#     print("This happens")
#
# if user_choice:
#     print("do True case things")
# elif user_choice == "potato":
#     print("Latvian gold")
# else:
#     print("do whatever for not accounted cases")
#
# iterable_text = "fkfyifiu"
# for letter in iterable_text:
#     print(letter)
#
# while True:
#     number = int(input("aeta"))
#     if number <5:
#         break
# # while True:     infinity loop
# #     print("potato")


def function_name(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)


function_name(1,2,3,4,5,6,7,8,9)

