def first_task():
    numbers_list = [20, 12, 17, 1, 3, 7, 140, 18, 36]
    numbers_tuple = tuple(numbers_list)

    threshold = int(input("Введіть порогове число: "))
    filtered_list = [value for value in numbers_tuple if value < threshold]
    print(f"Число {threshold}: Менші числа - {filtered_list}")


def second_task():
    fruits_tuple = ("apple", "banana", "cherry")
    result_string = ", ".join(fruits_tuple)
    print(f"З'єднані слова: {result_string}")


def third_task():
    book_collection = {
        "1984": {"author": "George Orwell", "year": 1949, "pages": 328},
        "To Kill a Mockingbird": {"author": "Harper Lee", "year": 1960, "pages": 281},
        "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925, "pages": 180},
        "War and Peace": {"author": "Leo Tolstoy", "year": 1869, "pages": 1225},
    }

    title = input("Введіть назву книги для пошуку: ")
    if title in book_collection:
        details = book_collection[title]
        print(f"Інформація про книгу '{title}':")
        print(f"Автор: {details['author']}")
        print(f"Рік видання: {details['year']}")
        print(f"Кількість сторінок: {details['pages']}")
    else:
        print(f"Книга '{title}' відсутня у колекції.")


def fourth_task():
    student_data = {
        "Ivanov": ("Ivan", 21, "Computer Science"),
        "Petrov": ("Petr", 22, "Mathematics"),
        "Sidorov": ("Alex", 20, "Physics"),
        "Kovalenko": ("Olga", 23, "Biology"),
    }

    surname = input("Введіть прізвище студента для перегляду інформації: ")
    if surname in student_data:
        info = student_data[surname]
        print(f"Деталі студента {surname}:")
        print(f"Ім'я: {info[0]}")
        print(f"Вік: {info[1]}")
        print(f"Спеціальність: {info[2]}")
    else:
        print(f"Студента з прізвищем '{surname}' не знайдено.")


def fifth_task():
    contacts = {
        "Shevchenko": ["+380671234567", "+380991111222"],
        "Bondarenko": ["+380931234567"],
        "Tkachenko": ["+380662345678", "+380931112233"],
    }

    def add_number(contact, phone):
        if contact in contacts:
            contacts[contact].append(phone)
            print(f"До контакту '{contact}' додано номер {phone}.")
        else:
            print(f"Контакт '{contact}' не знайдено у телефонній книзі.")

    add_number("Shevchenko", "+380501234567")

    print("\nОновлена телефонна книга:")
    for person, phones in contacts.items():
        print(f"{person}: {', '.join(phones)}")


first_task()
second_task()
third_task()
fourth_task()
fifth_task()
