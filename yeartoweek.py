days=int(input("Enter the total number of days you want to convert: "))

year = int(days/365)
remainder = days % 365
weeks = int(remainder / 7)
day = remainder % 7

print(f"{days} days = {year} year, {weeks} weeks and {day} day") 