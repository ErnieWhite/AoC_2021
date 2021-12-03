def main():
    with open('submove.txt') as file:
        directions = file.readlines()
    horizontal = 0
    depth = 0
    sub_moves = {}
    for direction in directions:
        command, amount = direction.split()
        sub_moves[command] = sub_moves.get(command, 0) + int(amount)
        print(f'Move {command} {amount} times.')
    horizontal = sub_moves['forward']
    depth = sub_moves['down'] - sub_moves['up']
    print(f'Horriontal: {horizontal}')
    print(f'Depth: {depth}')
    print(f'Product: {horizontal*depth}')


if __name__ == '__main__':
    main()
