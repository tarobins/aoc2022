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

    rock_hashes = []
    top_rows = []
    max_diff = 0
    num_rocks = 1000000000000
    for i in range(0, num_rocks):
        rock_position = (top_row + 4, 2)
        
        while True:
            blow_jet()
            if not can_move_down(rock_coordinates[current_rock_index], rock_position, grid):
                break;
            new_rock_position = (rock_position[0] - 1, rock_position[1])
            rock_position = new_rock_position

        insert_rock(rock_coordinates[current_rock_index], rock_position, grid)

        top_row = max(map(lambda x: x[0], grid.keys()))

        # print(f'grid {grid}')
        # print(f'top_row {top_row}')
        

        diffs = []
        for j in range(0,6):
            col = [k for k in grid.keys() if k[1] == j]
            if len(col) > 0:
                col_diff_max =  top_row - max(map(lambda x: x[0], col))
                # if col_diff_max > max_diff:
                    # max_diff = col_diff_max
                diffs.append(col_diff_max)
            else:
                diffs.append(top_row + 1)
                    # print(f'new max diff {max_diff}')


        current_rock_index = (current_rock_index + 1) % len(rock_coordinates)

        rock_hash = tuple(diffs) + (current_rock_index, jet_index)
        
        top_rows.append(top_row)
        
        # print(f'rock_hash for {i} = {rock_hash} height = {top_rows}')
        if rock_hash in rock_hashes:
            print(f'Repeat at {i} of {rock_hash}')
            rock_hashes.append(rock_hash)
            break
        rock_hashes.append(rock_hash)

    print(f'hash {rock_hashes[-1]} at {rock_hashes.index(rock_hashes[-1])}')

    # print(rock_hashes)
    # print(list(zip(rock_hashes, top_rows)))

    # print(top_row + 1)

    
    first_instance = rock_hashes.index(rock_hashes[-1])
    cycle_length = len(rock_hashes) - first_instance - 1

    print(f'first_instance {first_instance} cycle_length {cycle_length}')

    num_remaining = num_rocks - first_instance

    print(f'num_remaining {num_remaining}')

    number_of_cycles = num_remaining/cycle_length

    int_cycles = int(number_of_cycles)

    remaining = int(cycle_length * (number_of_cycles - int_cycles))
    # remaining = 23

    print(f'number_of_cycles {number_of_cycles} int_cycles {int_cycles} remaining {remaining}')

    height_before_cycles = top_rows[first_instance]
    cycles_height = top_rows[-1] - top_rows[first_instance]

    if remaining > 0:
        partial_cycles_height = top_rows[first_instance + remaining - 1] - top_rows[first_instance]
    else:
        partial_cycles_height = 0

    print(f'heigh_before_cycle {height_before_cycles} cycle_heigh {cycles_height} partial_cycles_height {partial_cycles_height}')

    print(height_before_cycles + cycles_height * (int_cycles) + partial_cycles_height + 1)

    # print(max_diff)
    




if __name__ == '__main__':
    app.run(main)