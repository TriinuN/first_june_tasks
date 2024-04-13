# Days - Write a Python program to convert a month name to a number of days.
# Expected Output:
# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December
# Input the name of Month: February
# No. of days: 28/29 days

months_dict = {'January':31 , 'February':28/29 , 'March':31 , 'April': 30, 'May':31 , 'June': 30, 'July':31,
               'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

user_month = input("What is the month name you want to know the amount of days to: ")
print(f"The amount of days for {user_month} is {months_dict[user_month]}")

#Kuidas ma tegin:
# def days_in_month(month_name):
#     month_days = {
#         "January": 31,
#         "February": "28/29",
#         "March": 31,
#         "April": 30,
#         "May": 31,
#         "June": 30,
#         "July": 31,
#         "August": 31,
#         "September": 30,
#         "October": 31,
#         "November": 30,
#         "December": 31
#     }
#     return month_days.get(month_name, "Invalid month name")
#
# def main():
#     print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
#     month_name = input("Input the name of Month: ")
#     days = days_in_month(month_name)
#     print("No. of days:", days, "days")
#
# if __name__ == "__main__":
#     main()