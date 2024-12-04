def check_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


data_to_test = [1800, 2020, 2012, 1999]
expected_results = [False, True, True, False]
for i in range(len(data_to_test)):
    year = data_to_test[i]
    print(f"Checking year {year}: ", end="")
    output = check_leap_year(year)
    if output == expected_results[i]:
        print("Test passed")
    else:
        print("Test failed")


def check_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_given_month(year, month):
    if not (1 <= month <= 12):
        return None

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and check_leap_year(year):
        return 29
    return days_in_months[month - 1]


years_test = [1800, 2020, 2008, 1995]
months_test = [2, 2, 12, 9]
expected_results = [28, 29, 31, 30]
for i in range(len(years_test)):
    year = years_test[i]
    month = months_test[i]
    print(f"Year {year}, Month {month}: ", end="")
    output = days_in_given_month(year, month)
    if output == expected_results[i]:
        print("Test passed")
    else:
        print("Test failed")


def check_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_given_month(year, month):
    if not (1 <= month <= 12):
        return None

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and check_leap_year(year):
        return 29
    return days_in_months[month - 1]


def calculate_day_of_year(year, month, day):
    if not (1 <= month <= 12 and 1 <= day <= days_in_given_month(year, month)):
        return None

    total_days = sum(days_in_given_month(year, m) for m in range(1, month)) + day
    return total_days


print(calculate_day_of_year(1992, 3, 15))
print(calculate_day_of_year(2024, 10, 1))
print(calculate_day_of_year(2005, 5, 20))
print(calculate_day_of_year(2012, 12, 31))
print(calculate_day_of_year(2000, 2, 29))
print(calculate_day_of_year(2021, 8, 16))
print(calculate_day_of_year(2020, 4, 31))
print(calculate_day_of_year(2020, 0, 15))
print(calculate_day_of_year(2020, 13, 1))


def is_number_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for i in range(1, 30):
    if is_number_prime(i + 2):
        print(i + 2, end=" ")


def convert_liters_to_mpg(liters):
    miles_in_100km = 100000 / 1609.344
    gallons = liters / 3.785411784
    return miles_in_100km / gallons


def convert_mpg_to_liters(miles):
    km_per_gallon = miles * 1.609344
    return (100 / km_per_gallon) * 3.785411784


print(convert_liters_to_mpg(4.2))
print(convert_liters_to_mpg(8.0))
print(convert_liters_to_mpg(11.0))
print(convert_mpg_to_liters(50.5))
print(convert_mpg_to_liters(40.0))
print(convert_mpg_to_liters(35.7))


def check_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


print(check_triangle(7, 10, 12))
print(check_triangle(2, 3, 5))
print(check_triangle(6, 6, 6))
print(check_triangle(15, 5, 10))
print(check_triangle(8, 15, 17))


def check_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def is_right_angle_triangle(a, b, c):
    if not check_triangle(a, b, c):
        return False

    sides = sorted([a, b, c])
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


print(is_right_angle_triangle(9, 12, 15))
print(is_right_angle_triangle(3, 4, 7))
print(is_right_angle_triangle(8, 8, 8))
print(is_right_angle_triangle(5, 12, 13))
print(is_right_angle_triangle(10, 24, 26))
