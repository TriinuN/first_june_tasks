# List Operations: Implement a function that takes a list of numbers as input and returns the sum, average, maximum,
# and minimum values. Use this function on a list entered by the user.
def stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return {"sum": total, "average": average, "maximum": maximum, "minimum": minimum}

user_list = []
for _ in range(5):
    user_input = int(input("Enter a number: "))
    user_list.append(user_input)

item = stats(user_list)

print(f"The total of provided numbers is {item['sum']} while average is {item['average']} while maximum is {item['maximum']} and1 minimum is {item['minimum']}")