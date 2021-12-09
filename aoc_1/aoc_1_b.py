import time


def main():
    tic = time.perf_counter_ns()
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    previous_average_depth = sum(int(lines[x].strip()) for x in range(3))
    increase = 0
    for index in range(1, len(lines)-2):
        average_depth = sum(int(lines[x].strip()) for x in range(index, index+3))
        data = list(lines[x] for x in range(index, index+3))
        if average_depth and previous_average_depth < average_depth:
            increase += 1
        previous_average_depth = average_depth
    print(increase)
    toc = time.perf_counter_ns()
    print(f'Time: {(toc-tic)/1000000}ms')



if __name__ == '__main__':
    main()
