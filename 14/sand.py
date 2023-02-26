from absl import app
from math import copysign, sqrt
from functools import reduce

def find_sand_resting_point(cave, max_y):
    current_location = (500, 0)
    while current_location[1] <= max_y:
        if not ((current_location[0], current_location[1] + 1) in cave):
            current_location = (current_location[0], current_location[1] + 1)
        elif not ((current_location[0] - 1, current_location[1] + 1) in cave):
            current_location = (current_location[0] - 1, current_location[1] + 1)
        elif not ((current_location[0] + 1, current_location[1] + 1) in cave):
            current_location = (current_location[0] + 1, current_location[1] + 1)
        else:
            return current_location
    return current_location


def main(argv):
    file_name = argv[1]

    f = open(file_name)

    cave = {}

    while line := f.readline().strip():
        string_pairs = line.split(' -> ')
        corners = list(map(lambda d: tuple(map(lambda i: int(i), d.split(','))), string_pairs))
        # print(corners)
        for i in range(0, len(corners) - 1):
            displacement = tuple(map(lambda p: p[1] - p[0], zip(corners[i],corners[i + 1])))
            # print(f'displacement {displacement}')
            magnitude = int(sqrt(displacement[0] ** 2 + displacement[1] ** 2))
            # print(f'magnitude {magnitude}')
            direction = tuple(map(lambda v: int(v / magnitude), displacement))
            # print(f'direction {direction}')
            cur = corners[i]
            for i in range(0, magnitude + 1):
                cave[cur] = '#'
                cur = tuple(map(lambda p: p[0] + p[1], zip(cur,direction)))
    
    max_y = reduce(lambda cur_max, cell: max(cur_max, cell[1]), cave, -1)

    count = 0
    while next_grain := find_sand_resting_point(cave, max_y):
        count += 1
        cave[next_grain] = "o"
        if next_grain == (500, 0):
            break
        
    print(count)


if __name__ == '__main__':
    app.run(main)
