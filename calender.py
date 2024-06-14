# python code to find the month
"""def find_month_name(month):
    if month < 1 or month > 12:
        return "Invalid input. Please enter a number between 1 and 12."
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return month_names[month-1]

month = int(input("Enter a month (1-12): "))
month_name = find_month_name(month)

print(f"The month {month} is {month_name}.")"""
# python code to find the month range
"""def find_month_range(month):
    if month < 1 or month > 12:
        return "Invalid input. Please enter a number between 1 and 12."
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    start_date = 1
    end_date = 31
    if month in [1, 3, 5, 7, 8, 10, 12]:
        end_date = 31
    elif month == 2:
        end_date = 28
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    end_date = 29
                else:
                    end_date = 28
            else:
                end_date = 29
    else:
        end_date = 30
    return f"The month of {month_names[month-1]} has {end_date} days."

month = int(input("Enter a month (1-12): "))
year = int(input("Enter a year: "))
month_range = find_month_range(month)

print(month_range)
"""
#leap year
"""
import calendar

def is_leap_year(year):
    return calendar.isleap(year)

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year
    """
l = [4,5,22,23,37,30,51,65,11,8,9,18,26,44,12,62,55,24,31,49,54,25,46,40,19]
sorted_l = sorted(l)
print(sorted_l)