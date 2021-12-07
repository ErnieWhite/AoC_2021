import time


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
    tic = time.perf_counter_ns()
    point_counts = {}
    p: tuple
    with open('input.txt') as data_file:
        while data := data_file.readline():
            s = int(data.split(' -> ')[0].split(',')[0]), int(data.split(' -> ')[0].split(',')[1])
            e = int(data.split(' -> ')[1].split(',')[0]), int(data.split(' -> ')[1].split(',')[1])
            l = tuple(line(s, e))
            for p in l:
                point_counts[(p[0], p[1])] = point_counts.get((p[0], p[1]), 0) + 1
        danger_areas = sum(x for x in point_counts.values() if x > 1)
        print(danger_areas)
    toc = time.perf_counter_ns()
    print((toc-tic))


if __name__ == '__main__':
    main()

# tic = time.perf_counter_ns()
# c = {}
# with open("input.txt") as f:
#     for x in f.readlines():
#         (p1x, p1y), (p2x, p2y) = [[*map(int, y.split(","))] for y in x.split(" -> ")]
#         for i in range(max(abs(xd := p2x - p1x), abs(yd := p2y - p1y))+1):
#             b = (p1x + (xd != 0) * i - (xd < 0) * i * 2, p1y + (yd != 0) * i - (yd < 0) * i * 2)
#             if b not in c:
#                 c[b] = 1
#             else:
#                 c[b] += 1
# print(sum(x > 1 for x in c.values()))
# toc = time.perf_counter_ns()
# print((toc-tic))
