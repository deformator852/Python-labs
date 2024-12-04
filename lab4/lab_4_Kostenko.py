def first_task():
    n = int(input("Введіть ціле число для перевірки: "))
    print(n >= 100)


def second_task():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))

    if a > b:
        print(f"Максимальне число: {a}")
    else:
        print(f"Максимальне число: {b}")


def third_task():
    plant = input("Назва рослини: ")

    if plant == "Spathiphyllum":
        print("Так, Спатіфілум — найкраща рослина на світі!")
    elif plant == "spathiphyllum":
        print("Ні, я хочу великий Спатіфілум!")
    else:
        print(f"Спатіфілум! Не {plant}!")


def fourth_task():
    income = float(input("Введіть ваш річний дохід: "))

    if income <= 85528:
        tax = income * 0.18 - 556.02
    else:
        tax = 14839.02 + (income - 85528) * 0.32

    if tax < 0:
        tax = 0

    tax = round(tax, 0)
    print("Розмір податку:", tax, "талерів")


def fifth_task():
    year = int(input("Введіть рік: "))

    if year < 1582:
        print("Цей рік не входить до періоду Григоріанського календаря")
    else:
        if year % 4 != 0:
            print("Звичайний рік")
        elif year % 100 != 0:
            print("Високосний рік")
        elif year % 400 != 0:
            print("Звичайний рік")
        else:
            print("Високосний рік")

    odd_numbers = 0
    even_numbers = 0

    number = int(input("Введіть число або 0 для завершення: "))

    while number != 0:
        if number % 2 == 1:
            odd_numbers += 1
        else:
            even_numbers += 1
        number = int(input("Введіть число або 0 для завершення: "))

    print("Кількість непарних чисел:", odd_numbers)
    print("Кількість парних чисел:", even_numbers)

    counter = 5
    while counter:
        print("Цикл, крок:", counter)
        counter -= 1
    print("Завершено цикл. Лічильник:", counter)


def sixth_task():
    secret_number = 777

    print(
        """
        +================================+
        | Ласкаво просимо в мою гру! |
        | Введіть ціле число і спробуйте   |
        | вгадати секретне число.        |
        | Яке число я вибрав?             |
        +================================+
        """)

    while True:
        user_guess = int(input("Введіть своє припущення: "))
        if user_guess == secret_number:
            print("Молодець! Ти вгадав число!")
            break
        else:
            print("Невірно! Спробуй ще раз!")


def seventh_task():
    import time

    for i in range(1, 6):
        print(f"{i} Міссісіпі")
        time.sleep(1)

    print("Готові чи ні, я йду!")


def eighth_task():
    while True:
        word = input("Введіть слово для перевірки: ")

        if word == "chupacabra":
            print("Ви вийшли з циклу успішно.")
            break


def ninth_task():
    user_word = input("Введіть слово: ")
    user_word = user_word.upper()

    for letter in user_word:
        if letter in ('A', 'E', 'I', 'O', 'U'):
            continue

        print(letter)


def tenth_task():
    word_without_vowels = ""

    user_word = input("Введіть слово: ")
    user_word = user_word.upper()
    for letter in user_word:
        if letter in ('A', 'E', 'I', 'O', 'U'):
            continue

        word_without_vowels += letter

    print(word_without_vowels)


def eleventh_task():
    blocks = int(input("Введіть кількість блоків для побудови піраміди: "))

    height = 0
    blocks_in_layer = 1

    while blocks >= blocks_in_layer:
        blocks -= blocks_in_layer
        height += 1
        blocks_in_layer += 1

    print("Висота піраміди:", height)


def twelfth_task():
    c0 = int(input("Введіть натуральне число для обчислень: "))

    steps = 0

    while c0 != 1:
        print(c0)

        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1

        steps += 1

    print(c0)
    print("Кроків:", steps)


first_task()
second_task()
third_task()
fourth_task()
fifth_task()
sixth_task()
seventh_task()
eighth_task()
ninth_task()
tenth_task()
eleventh_task()
twelfth_task()
