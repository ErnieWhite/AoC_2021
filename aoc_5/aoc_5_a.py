def main():
    point_counts = {}
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    with open('input.txt') as data_file:
        while data := data_file.readline():
            xs = int(data.split(' -> ')[0].split(',')[0]), int(data.split(' -> ')[1].split(',')[0])
            ys = int(data.split(' -> ')[0].split(',')[1]), int(data.split(' -> ')[1].split(',')[1])
            if xs[0] == xs[1] or ys[0] == ys[1]:
                min_x = min(xs) if min(xs) < min_x else min_x
                max_x = max(xs) if max(xs) > max_x else max_x
                min_y = min(ys) if min(ys) < min_y else min_y
                max_y = max(ys) if max(ys) > max_y else max_y
                for x in range(min(xs), max(xs) + 1):
                    for y in range(min(ys), max(ys) + 1):
                        point_counts[(y, x)] = point_counts.get((y, x), 0) + 1
        # for x in range(min_x, max_x+1):
        #     for y in range(min_y, max_y + 1):
        #         count = point_counts.get((y, x), 0)
        #         print(count if count > 0 else '.', end='')
        #     print()
        danger_areas = 0
        for v in point_counts.values():
            if v > 1:
                danger_areas += 1
        print(danger_areas)


if __name__ == '__main__':
    main()
