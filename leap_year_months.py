def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def months(year, month):
    if month > 12 or month < 1:
        print("\nINVALID MONTH\n")
        exit()
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap(year):
        month_days[1] = 29
        month = month_days[month - 1]
        return month
    else:
        return month_days[month - 1]
year = int(input("\nEnter a year:\n"))
month = int(input("\nEnter your month:\n"))
print(f"\nNo of days in this month are: {months(year, month)}\n")