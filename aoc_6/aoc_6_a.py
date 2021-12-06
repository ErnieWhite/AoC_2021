def main():
    with open('test_input.txt', 'r') as lanternfish_file:
        starting_fishes = [int(x) for x in lanternfish_file.read().split(',')]
        fishes = {x: 0 for x in range(9)}
        for fish in starting_fishes:
            fishes[fish] += 1
        for day in range(80):
            baby_fish = fishes[0]
            for timer in range(8):
                fishes[timer] = fishes[timer + 1]
            fishes[8] = baby_fish
            fishes[6] += baby_fish
        print(sum(fishes.values()))


if __name__ == '__main__':
    main()
