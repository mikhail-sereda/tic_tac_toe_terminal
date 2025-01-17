import os

playing_field = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
player = "X"


def play(field):
    for i in field:
        print()
        print("\t", end="")
        print(*i, sep=" | ", end=" ")
        print()
    print()


def check_winnings(field: list) -> bool:
    for i in range(3):
        set_rov = set(field[i])
        if field[0][i] == field[1][i] and field[0][i] == field[2][i] and field[0][i] != "-":
            return True
        elif len(set_rov) == 1 and not ("-" in set_rov):
            return True
    if (field[0][0] == field[1][1] and field[0][0] == field[2][2] and field[0][0] != "-") or \
            (field[0][2] == field[1][1] and field[0][2] == field[2][0] and field[0][2] != "-"):
        return True
    return False


def check_cell(field: list[list], row: int, column: int) -> bool:
    """
    :param field: Игровое поле.
    :param row:
    :param column:
    :return:
    """
    return field[row - 1][column - 1] != "-"


def check_index(check_row: str, check_col: str):
    return check_row in ["1", "2", "3"] and check_col in ["1", "2", "3"]


play(playing_field)

while True:
    row = input(f"Ход {player}\nВведите номер строки (1-3)\n")
    col = input(f"Ход {player}\nВведите номер столбца (1-3)\n")
    os.system("clear")

    if not check_index(row, col):
        play(playing_field)
        os.system("echo Неверный ход. Ошибочное значение столбца или ячейки")
        continue

    row = int(row)
    col = int(col)

    if check_cell(playing_field, row, col):
        play(playing_field)
        os.system("echo Неверный ход. Ячейка занята. Укажите свободную ячейку")
        continue
    # play(playing_field)
    playing_field[row - 1][col - 1] = player
    os.system("clear")
    play(playing_field)
    if check_winnings(playing_field):
        os.system(f"echo Победа {player}")
        break
    if player == "X":
        player = "O"
    else:
        player = "X"
