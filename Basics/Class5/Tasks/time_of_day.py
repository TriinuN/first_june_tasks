# Time of day - Write a program to based on current time of day would return a word Morning, Day, Evening or Night.
# Expected Output:
# Input time in 24 hour format: 13
# Day
# hint: use datetime library. To get current time you will need to
# from datetime import datetime
# current_hour = datetime.now().hour
# 7:00 to 11:59 is morning
# 12:00 to 18:59 is afternoon
# 17:00pm to 21:59 is evening
# 22:00 to 00:59 is night
# 1:00 to 6:59 is early morning.

from datetime import datetime

current_hour = datetime.now().hour

if current_hour < 5:
    print("Night")
elif current_hour < 10:
    print("Morning")
elif current_hour < 18:
    print("Day")
elif current_hour < 22:
    print("Evening")
elif current_hour < 24:
    print("Night")


#Kuidas mina tegin:
# from datetime import datetime
#
# current_hour = datetime.now().hour
#
# print("Current hour is ",current_hour)
#
# if 7 <= current_hour <= 11:
#     print("It is morning")
# elif 12 <= current_hour <= 18:
#     print("It is afternoon")
# elif 19 <= current_hour <= 21:
#     print("It is evening")
# elif 22 <= current_hour <= 23 or 0 <= current_hour <= 1:
#     print("It is night")
# else:
#     print("It is early morning")