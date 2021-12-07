import time


def f1(start_pos, end_pos):
    return abs(start_pos - end_pos)


def f2(p1, p2):
    n = abs(p1 - p2)
    return n*(n+1)/2


def main():
    tic = time.perf_counter_ns()
    with open('input.txt', 'r') as data_file:
        sub_locs = [int(x) for x in data_file.read().split(',')]
        crabs = {loc: sub_locs.count(loc) for loc in set(sub_locs)}
        print(min(sum(f2(s, e)*crabs[s] for s in crabs) for e in range(max([x for x in crabs]))))
        toc = time.perf_counter_ns()
        print(f'Problem completed in {(toc-tic)/1000000}ms')


if __name__ == '__main__':
    main()
