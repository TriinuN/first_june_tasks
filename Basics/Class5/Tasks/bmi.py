# BMI - Write program that calculates body mass index (bmi = weight / (height*height)). Weight(kg) and height(meters)
# would be passed by user input.

weight = float(input("What is your weight in kg: "))
height = float(input("What is your height in m: "))

bmi = weight / (height ** 2)
if bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("You are normal")
elif bmi <= 30:
    print("You are overweight")
else:
    print("You are obese")

# Kuidas tegin mina:
# w = float(input("Please enter your weight in kg: "))
# h = float(input("Please enter your height in m: "))
#
# def bodymassindex(height, weight):
#     return round((weight / height**2),2)
# BMI = bodymassindex(h, w)
# print('Your BMI is: ', BMI)
#
# if BMI <= 18.5:
#     print("Underweight")
# elif BMI <= 25.0:
#     print("Normal")
# elif BMI <= 30.0:
#     print("Overweight")
# elif BMI > 30:
#     print("Obese")
# else:
#     print("Try again.")
# print("Thanks for using this! :) ")
#
#
# # # Võimalus nr2 bmi arvutamiseks ilma võrdluseta
# #
# # # 1st input: enter height in meters e.g: 1.65
# # height = input("Enter your height in m: ")
# # # 2nd input: enter weight in kilograms e.g: 72
# # weight = input("Enter your weight in kg: ")
# # w = int(weight)
# # h = float(height)
# # bmi = (w / h**2)
# # new_bmi = int(bmi)
# # print(new_bmi)
