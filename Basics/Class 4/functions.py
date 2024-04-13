# Simple function, no return, no parameters
def test_function():
    print("Hello from the function!")


# Simple function, returns sum of 2+2, no parameters
def calculator():
    sum_of_two = 2+2
    return sum_of_two
    # a print functions that will never run as it is unreachable
    print("Hello from the function!")


# Complex function, no parameters, returns value
def conditional():
    if 5 < 3:
        return "Yes"
    else:
        return "No"


# takes parameter, returns value, default value
def better_conditional(number=19):
    if number == "Nothing":
        return "bla bla bla"
    if number < 18:
        return "Go Home!!"
    return "You can come in!!" #Else: is not needed


# Simple function, has parameters, returns value
def calculator_two(number1, number2=6): #esimese taha ei saa panna nr, tuleb panna teisele
    result = number1 + number2 #You can also just write return number1 + number2
    return result


#test_function()
#result = calculator()
#value = conditional()
#print(value)
#number99 = 99
#number7 = 7
#result = calculator_two(99, 7)
#print(result)
print(better_conditional())