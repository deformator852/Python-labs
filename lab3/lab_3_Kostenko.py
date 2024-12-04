import math


def gauss_function(x, mu, sigma):
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coefficient * math.exp(exponent)


def first_task():
    x = float(input("Введіть значення x для обчислення Гаусової функції: "))
    mu = float(input("Введіть значення середнього (mu): "))
    sigma = float(input("Введіть стандартне відхилення (sigma): "))

    result = gauss_function(x, mu, sigma)
    print(f"Значення Гаусової функції: {result}")


def second_task():
    apples = {"John": 3, "Mary": 5, "Adam": 6}
    for name, count in apples.items():
        print(f"{name} має {count} яблук", end=", ")

    total_apples = sum(apples.values())
    print(f"\nЗагальна кількість яблук: {total_apples}")


def third_task():
    kilometers = 12.25
    miles = 7.38

    kilometers_in_miles = miles * 1.61
    miles_in_kilometers = kilometers / 1.61

    print(f"{miles} миль = {round(kilometers_in_miles, 2)} кілометрів")
    print(f"{kilometers} кілометрів = {round(miles_in_kilometers, 2)} миль")


def fourth_task():
    x = -1
    result = 3 * (x ** 3) - 2 * (x ** 2) + 3 ** x - 1
    print(f"Рішення рівняння: {result}")


def fifth_task():
    hours = 2
    seconds_in_hour = 3600
    print(f"Кількість годин: {hours}")
    print(f"У {hours} годинах {hours * seconds_in_hour} секунд")


def sixth_task():
    a = float(input("Введіть перше число (a): "))
    b = float(input("Введіть друге число (b): "))

    print(f"Сума чисел: {a + b}")
    print(f"Різниця чисел: {a - b}")
    print(f"Добуток чисел: {a * b}")

    if b != 0:
        print(f"Частка чисел: {a / b}")
    else:
        print("Помилка: неможливо поділити на нуль!")


def seventh_task():
    x = float(input("Введіть значення x для обчислення виразу: "))
    y = 1 / (x + 1 / (x + 1 / (x + 1 / (x + 1 / (x + 1 / x)))))

    print(f"Результат обчислення виразу: {y}")


def eighth_task():
    hour = int(input("Введіть години початкового часу: "))
    mins = int(input("Введіть хвилини початкового часу: "))
    duration = int(input("Введіть тривалість події (в хвилинах): "))

    total_minutes = mins + duration
    new_minutes = total_minutes % 60
    extra_hours = total_minutes // 60
    new_hour = (hour + extra_hours) % 24

    print(f"Час після події: {new_hour}:{new_minutes:02d}")


first_task()
second_task()
third_task()
fourth_task()
fifth_task()
sixth_task()
seventh_task()
eighth_task()
