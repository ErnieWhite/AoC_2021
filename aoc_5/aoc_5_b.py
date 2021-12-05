def line(s, e):
    """ returns the points of a line
    y = mx + b is the equation for a line
    m is slope of the line
    b is the y intercept

        y2 - y1
    m = -------
        x2 - x1

    b = y - mx
    :param s: tuple - The first point on the line (x, y)
    :param e: tuple - The last point on the line (x, y)
    :return: tuple (x, y)
    """
    dx = e[0] - s[0]
    dy = e[1] - s[1]
    if dx != 0:
        m = dy / dx
        b = s[1] - m * s[0]

        # we are going to process our line from left to right
        sx = min([s[0], e[0]])
        ex = max([s[0], e[0]])
        for x in range(sx, ex + 1):
            yield x, int(m * x + b)
    else:
        sy = min([s[1], e[1]])
        ey = max([s[1], e[1]])
        for y in range(sy, ey + 1):
            yield s[0], y


def main():
    point_counts = {}
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    p: tuple
    with open('input.txt') as data_file:
        while data := data_file.readline():
            s = int(data.split(' -> ')[0].split(',')[0]), int(data.split(' -> ')[0].split(',')[1])
            e = int(data.split(' -> ')[1].split(',')[0]), int(data.split(' -> ')[1].split(',')[1])
            l = tuple(line(s, e))
            for p in l:
                min_x = p[0] if p[0] < min_x else min_x
                max_x = p[0] if p[0] > max_x else max_x
                min_y = p[1] if p[1] < min_y else min_y
                max_y = p[1] if p[1] > max_y else max_y
                point_counts[(p[0], p[1])] = point_counts.get((p[0], p[1]), 0) + 1
        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y + 1):
                count = point_counts.get((y, x), 0)
                print(count if count > 0 else '.', end='')
            print()
        danger_areas = 0
        for v in point_counts.values():
            if v > 1:
                danger_areas += 1
        print(danger_areas)


if __name__ == '__main__':
    main()
