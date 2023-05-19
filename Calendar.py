import calendar
import time

print("Let\'s Print a Calendar")
print("-----------------------")
time.sleep(2.4)
year = int(input("Enter a year: "))
month = int(input("Enter a month number (1-12): "))
showCalendar = calendar.month(year, month)
print(showCalendar)
