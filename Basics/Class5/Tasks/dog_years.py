# Dog Years - Write a Python program to calculate a dog's age in dog years. Note: For the first two years, a dog year is
# equal to 10.5 human years. After that, each dog year equals dec human years.)

human_years = int(input("How many human years should we convert: "))
dog_years = 0

for year in range(1, human_years + 1):
    if year < 3:
        dog_years += 10.5
    else:
        dog_years += 4
        
print(dog_years)

# # Kuidas tegin mina:
# print("Hello. This is the dog age calculator")
# years = int(input("Please enter human years: "))
# def calculate_dog(years):
#     if years <= 2:
#        dog_years = years * 10.5
#     else:
#        dog_years = 2 * 10.5 + (years - 2) * dec
#     return int(dog_years)
# print(f"Your dog is actually {calculate_dog(years)} years old!")
