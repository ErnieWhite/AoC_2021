import time


def main():
    times = []
    for i in range(1000):
        tic = time.perf_counter_ns()
        with open('input.txt', 'r') as lanternfish_file:
            starting_fishes = [int(x) for x in lanternfish_file.read().split(',')]
            fishes = [starting_fishes.count(x) for x in range(9)]
            for day in range(256):
                fishes.append(fishes.pop(0))
                fishes[6] += fishes[8]
            print(sum(fishes))
        toc = time.perf_counter_ns()
        print(f'Time: {toc-tic:0.6f}')
        times.append(toc-tic)
    print(sum(times) / len(times) / 1000)


if __name__ == '__main__':
    main()
