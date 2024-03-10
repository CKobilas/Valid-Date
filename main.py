Month = int(input("Enter the month: "))
Day = int(input("Enter the day: "))
Year = int(input("Enter the year: "))

valid_date = True

if Day < 1 or Day > 31 or Month < 1 or Month > 12 or Year < 0:
    valid_date = False
elif Month == 2:  # February
    if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
        if Day > 29:
            valid_date = False
    elif Day > 28:
        valid_date = False
elif Month in [4, 6, 9, 11]:  # April, June, September, November
    if Day > 30:
        valid_date = False

if valid_date:
    print(str(Month) + "/" + str(Day) + "/" + str(Year) + " is a valid date.")
else:
    print(str(Month) + "/" + str(Day) + "/" + str(Year) + " is an invalid date.")
