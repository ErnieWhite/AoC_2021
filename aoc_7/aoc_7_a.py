import time


def fuel_cost(start_pos, end_pos):
    return max(start_pos, end_pos) - min(start_pos, end_pos)


def main():
    tic = time.perf_counter_ns()
    crabs = {}
    with open('input.txt', 'r') as data_file:
        sub_locs = [x for x in data_file.read().split(',')]
        for loc in sub_locs:
            crabs[loc] = crabs.get(loc, 0) + 1
        cost = [sum(fuel_cost(int(s), int(e))*crabs[s] for s in crabs) for e in crabs]
        print(min(cost))
    toc = time.perf_counter_ns()
    print(f'Problem completed in {toc-tic}ns by Python')


if __name__ == '__main__':
    main()
