def main():
    with open('test_input.txt') as file:
        directions = file.readlines()
    horizontal = 0
    depth = 0
    sub_info = {
        'forward': 0,
        'depth': 0,
        'aim': 0,
    }
    for direction in directions:
        command, amount = direction.split()
        match command:
            case 'forward':
                sub_info['forward'] += int(amount)
                sub_info['depth'] += sub_info['aim'] * int(amount)
            case 'down':
                sub_info['aim'] += int(amount)
            case 'up':
                sub_info['aim'] -= int(amount)
        print(f'Move {command} {amount} times.')
    print(f'Forward: {sub_info["forward"]}')
    print(f'Depth: {sub_info["depth"]}')
    print(f'Aim: {sub_info["aim"]}')
    print(f'Product: {sub_info["forward"] * sub_info["depth"]}')


if __name__ == '__main__':
    main()
