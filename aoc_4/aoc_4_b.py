def update_board(board, num):
    for row in board:
        for square in row:
            if square[0] == num:
                square[1] = True


def board_won(board):
    # check across
    for row in board:
        if all([x[1] for x in row]):
            return True

    # check down
    #  The composition just transposes the board
    for column in [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]:
        if all([x[1] for x in column]):
            return True

    # check diagonal
    # diagonals don't count

    return False


def calculate_score(board, num):
    temp = [y[0] for x in board for y in x if not y[1]]
    board_total = sum(temp)
    return board_total, num, board_total * num


def main():
    with open('input.txt', 'r') as file:
        numbers = [int(x) for x in file.readline().split(',')]
        file.readline()  # just ignore the first blank line
        boards = []
        board = []
        while line := file.readline():
            if line.strip() == '':
                boards.append(board)
                board = []
            else:
                board.append([[int(x), False] for x in line.split()])
        boards.append(board)

        score = 0
        boards_left = [x for x in range(len(boards))]

        for num in numbers:
            # if score != 0:
            #     break
            for board_id, board in enumerate(boards):
                if board_id in boards_left:
                    update_board(board, num)
                    if board_won(board):
                        board_total, current_num, score = calculate_score(board, num)
                        if len(boards_left) == 1:
                            print(f'Board Total: {board_total} Current Number: {current_num} Board Score: {score}')
                        boards_left.remove(board_id)


if __name__ == '__main__':
    main()
