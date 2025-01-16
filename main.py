import os

playing_field = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def play(field):

    for i in field:
        for j in i:
            print(j, end=" ", sep="!")
        print()




player = "x"

while True:
    play(playing_field)
    step = input(f"Ход {player}\nВведите ход\n")
    step = list(map(int, step))

    if (3 < step[0] or step[0] < 1) or (3 < step[1] or step[1] < 1):

        os.system("clear")
        print("error")
        continue
    os.system("clear")
    playing_field[step[0] - 1][step[1] - 1] = player
    # play(playing_field)
    if player == "x":
        player = "o"
    else:
        player = "x"

