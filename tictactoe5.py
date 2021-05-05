def is_impossible(m):
    black = 0
    white = 0
    for i in range(3):
        for j in range(3):
            if m[i][j] == "X":
                black += 1
            elif m[i][j] == "O":
                white += 1
    if abs(black - white) > 1:
        return True
    return False

def is_finish(m):
    count = 0
    for i in range(3):
        for j in range(3):
            if m[i][j] == "_":
                count += 1
    if count == 0:
        return True
    return False

def is_winner(turn, m):
    for i in range(3):
        if check_row(i, turn, m):
            return True
    for j in range(3):
        if check_column(j, turn, m):
            return True
    if check_diagonal(turn, m):
        return True
    if check_reverse_diagonal(turn, m):
        return True

def check_row(i, turn, m):
    count = 0
    for j in range(3):
        if m[i][j] == turn:
            count += 1
    return count_judge(count)

def check_column(j, turn, m):
    count = 0
    for i in range(3):
        if m[i][j] == turn:
            count += 1
    return count_judge(count)

def check_diagonal(turn, m):
    count = 0
    for i in range(3):
        if m[i][i] == turn:
            count += 1
    return count_judge(count)

def check_reverse_diagonal(turn, m):
    count = 0
    for i in range(3):
        if m[i][2 - i] == turn:
            count += 1
    return count_judge(count)

def count_judge(count):
    if count == 3:
        return True
    else:
        return False

def show(m):
    print("---------")
    print("| {} {} {} |".format(m[0][0], m[0][1], m[0][2]))
    print("| {} {} {} |".format(m[1][0], m[1][1], m[1][2]))
    print("| {} {} {} |".format(m[2][0], m[2][1], m[2][2]))
    print("---------")

def show_winner(m):
    if is_impossible(m):
        print("Impossible")
    elif is_winner("X", m) and is_winner("O", m):
        print("Impossible")
    elif is_winner("X", m):
        print("X wins")
    elif is_winner("O", m):
        print("O wins")
    elif is_finish(m):
        print("Draw")
    else:
        print("Game not finished")

def is_gameover(m):
    if is_winner("X", m):
        print("X wins")
        return True
    elif is_winner("O", m):
        print("O wins")
        return True
    elif is_finish(m):
        print("Draw")
        return True
    else:
        return False

def update_matrix(turn, coordinates, m):
    rowcol = coordinates.split()
    if len(rowcol) != 2:
        print("You should enter numbers!")
        return False
    row = rowcol[0]
    col = rowcol[1]
    if not row.isnumeric():
        print("You should enter numbers!")
        return False
    if not col.isnumeric():
        print("You should enter numbers!")
        return False
    row = int(row)
    col = int(col)
    if not row in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        return False
    if not col in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        return False
    if m[row - 1][col - 1] != "_":
        print("This cell is occupied! Choose another one!")
        return False
    m[row - 1][col - 1] = turn
    return True

row1 = ["_"] * 3
row2 = ["_"] * 3
row3 = ["_"] * 3
m = [row1, row2, row3]

show(m)
turn = "X"
while not is_gameover(m):
    coordinates = input("Enter the coordinates: ")
    if not update_matrix(turn, coordinates, m):
        continue
    show(m)
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

# show_winner(m)
