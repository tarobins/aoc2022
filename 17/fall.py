from absl import app

rocks = [
'''
####
''',
'''
.#.
###
.#.
''',
'''
..#
..#
###
''',
'''
#
#
#
#
''',
'''
##
##
'''
]

grid_row = '.......'

def coordinate_rock(rock):
    cur_line = 0
    lines = [x for x in rock.split('\n') if len(x) > 0]
    r = []
    for row, line in enumerate(reversed(lines)):
        for col, char in enumerate(line):
            if char == '#':
                r.append((row, col))
    return r

def can_move_left(rock_coordinates, rock_position, grid):
    if rock_position[1] <= 0:
        return False
    new_position = (rock_position[0], rock_position[1] - 1)
    return can_position(rock_coordinates, new_position, grid)


def can_move_right(rock_coordinates, rock_position, grid):
    min_col = min([col for _, col in rock_coordinates])
    max_col = max([col for _, col in rock_coordinates])
    width = max_col - min_col + 1
    if rock_position[1] + width - 1 >= 6:
        return False
    new_position = (rock_position[0], rock_position[1] + 1)
    return can_position(rock_coordinates, new_position, grid)

def can_move_down(rock_coordinates, rock_position, grid):
    # print(rock_coordinates)
    if rock_position[0] <= 0:
        return False
    new_position = (rock_position[0] - 1, rock_position[1])
    return can_position(rock_coordinates, new_position, grid)


def grid_coordinates(rock_coordinates, rock_position):
    for coordinate in rock_coordinates:
        yield (coordinate[0] + rock_position[0], coordinate[1] + rock_position[1])
    

def insert_rock(rock_coordinates, rock_position, grid):
    for coordinate in grid_coordinates(rock_coordinates, rock_position):
        grid[coordinate] = '#'

def can_position(rock_coordinates, rock_position, grid):
    for coordinate in grid_coordinates(rock_coordinates, rock_position):
        if grid.get(coordinate) == '#':
            return False
    return True



def main(argv):
    f = open(argv[1])
    # f = open('17/test_input.txt')
    jets = f.readline()

    rock_coordinates = list(map(coordinate_rock,rocks))

    top_row = -1
    piece = 0
    current_rock_index = 0
    jet_index = 0

    grid = {}

    def blow_jet():
        nonlocal jet_index, jets, rock_position, grid
        jet = jets[jet_index]
        jet_index = (jet_index+1) % len(jets)
        if jet == '>':
            if can_move_right(rock_coordinates[current_rock_index], rock_position, grid):
                rock_position = (rock_position[0], rock_position[1] + 1)
        elif jet == '<':
            if can_move_left(rock_coordinates[current_rock_index], rock_position, grid):
                rock_position = (rock_position[0], rock_position[1] - 1)

    for i in range(0, 2022):
        rock_position = (top_row + 4, 2)
        
        while True:
            blow_jet()
            if not can_move_down(rock_coordinates[current_rock_index], rock_position, grid):
                break;
            new_rock_position = (rock_position[0] - 1, rock_position[1])
            rock_position = new_rock_position

        insert_rock(rock_coordinates[current_rock_index], rock_position, grid)

        top_row = max(map(lambda x: x[0], grid.keys()))

        current_rock_index = (current_rock_index + 1) % len(rock_coordinates)

    print(top_row + 1)
    




if __name__ == '__main__':
    app.run(main)