def first_task():
    hat_list = [1, 2, 3, 4, 5]
    hat_list[2] = int(input("Введіть нове ціле число для заміни середнього елементу списку: "))
    hat_list.pop()
    print("Довжина списку після змін:", len(hat_list))
    print("Оновлений список:", hat_list)


def second_task():
    n = int(input("Введіть кількість елементів для створення списку: "))
    arr = []

    for i in range(n):
        element = int(input(f"Введіть елемент номер {i + 1}: "))
        arr.append(element)

    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    print("Сортування завершено. Відсортований список:", arr)


def third_task():
    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    unique_list = []

    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)

    print("Список з унікальними елементами:", unique_list)


def fourth_task():
    chessboard = [["_"] * 8 for _ in range(8)]

    chessboard[0][0] = "T"
    chessboard[0][7] = "T"
    chessboard[7][0] = "T"
    chessboard[7][7] = "T"

    print("Шахівниця:")
    for row in chessboard:
        print(row)


first_task()
second_task()
third_task()
fourth_task()
