import os

playing_field = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def play(field):
    for i in field:
        print(*i, end=" ", sep="|")
        print()


def check_winnings(field: list) -> bool:
    if (field[0][0] == field[1][0] and field[0][0] == field[2][0] and field[0][0] != "-") \
            or (field[0][1] == field[1][1] and field[0][1] == field[2][1] and field[0][1] != "-") or \
            (field[0][2] == field[1][2] and field[0][2] == field[2][2] and field[0][2] != "-") or \
            (field[0][0] == field[0][1] and field[0][0] == field[0][2] and field[0][0] != "-") or \
            (field[1][0] == field[1][1] and field[0][0] == field[1][2] and field[1][0] != "-") or \
            (field[2][0] == field[2][1] and field[2][0] == field[2][2] and field[2][0] != "-") or \
            (field[0][0] == field[1][1] and field[0][0] == field[2][2] and field[0][0] != "-") or \
            (field[0][2] == field[1][1] and field[0][2] == field[2][0] and field[0][2] != "-"):
        return True
    return False


player = "x"

while True:
    play(playing_field)
    step = input(f"Ход {player}\nВведите ход [строкастолбец]\n")
    step = list(map(int, step))

    if (3 < step[0] or step[0] < 1) or (3 < step[1] or step[1] < 1):
        os.system("clear")
        print("error")
        continue
    os.system("clear")
    playing_field[step[0] - 1][step[1] - 1] = player
    if check_winnings(playing_field):
        play(playing_field)
        print(f"Победа {player}")
        break
    if player == "x":
        player = "o"
    else:
        player = "x"
