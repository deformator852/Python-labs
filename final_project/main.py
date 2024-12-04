from random import randint


def show_grid(grid):
    border = "+-------+-------+-------+"
    for row in grid:
        print(border)
        print("|       |       |       |")
        print("|   " + "   |   ".join(row) + "   |")
        print("|       |       |       |")
    print(border)


def player_turn(grid):
    while True:
        user_input = input("Введіть номер клітинки (1-9): ")
        if user_input.isdigit() and 1 <= int(user_input) <= 9:
            r, c = divmod(int(user_input) - 1, 3)
            if grid[r][c] not in ['P', 'C']:
                grid[r][c] = 'P'
                break
            else:
                print("Ця клітинка вже зайнята, оберіть іншу.")
        else:
            print("Некоректний ввод. Введіть число від 1 до 9.")


def available_cells(grid):
    return [(r, c) for r in range(3) for c in range(3) if grid[r][c] not in ['P', 'C']]


def check_winner(grid, symbol):
    winning_patterns = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    return any(all(grid[r][c] == symbol for r, c in pattern) for pattern in winning_patterns)


def computer_turn(grid):
    free_positions = available_cells(grid)
    if free_positions:
        r, c = free_positions[randint(0, len(free_positions) - 1)]
        grid[r][c] = 'C'


def game():
    grid = [
        ['1', '2', '3'],
        ['4', 'C', '6'],
        ['7', '8', '9']
    ]

    show_grid(grid)

    while True:
        player_turn(grid)
        show_grid(grid)
        if check_winner(grid, 'P'):
            print("Вітаємо! Ви перемогли!")
            break
        if not available_cells(grid):
            print("Гра завершена. Нічия!")
            break

        print("Хід комп'ютера...")
        computer_turn(grid)
        show_grid(grid)
        if check_winner(grid, 'C'):
            print("Комп'ютер переміг! Спробуйте ще раз.")
            break
        if not available_cells(grid):
            print("Гра завершена. Нічия!")
            break


game()
