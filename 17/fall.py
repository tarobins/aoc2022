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
    # print(f'rock_coordinates {rock_coordinates}')
    min_col = min([col for _, col in rock_coordinates])
    max_col = max([col for _, col in rock_coordinates])
    width = max_col - min_col + 1
    # print(f'min_col {min_col} max_col {max_col}')
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
    # min_row = min([row for row, _ in rock_coordinates])
    # max_row = max([row for row, _ in rock_coordinates])
    # height = max_row - min_row + 1
    # print(f'rock_position {rock_position}, height {height}')
    # if rock_position[0] - height + 1 > 0:    
    #     return True
    # else:
    #     return False

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

    # rock_position = (top_row + 4, 2)  # need starting position st the bottom is 3 from pile

    # print(rock_position)

    def blow_jet():
        nonlocal jet_index, jets, rock_position, grid
        jet = jets[jet_index]
        jet_index = (jet_index+1) % len(jets)
        if jet == '>':
            if can_move_right(rock_coordinates[current_rock_index], rock_position, grid):
                rock_position = (rock_position[0], rock_position[1] + 1)
            #     print('right')
            # else:
            #     print('cant go right')
        elif jet == '<':
            if can_move_left(rock_coordinates[current_rock_index], rock_position, grid):
                rock_position = (rock_position[0], rock_position[1] - 1)
            #     print('left')
            # else:
            #     print('cant go left')

    for i in range(0, 2022):
        rock_position = (top_row + 4, 2)
        # print(f'Rock {current_rock_index} starting at {rock_position}')
        # print(f'rock looks like {rocks[current_rock_index]} {rock_coordinates[current_rock_index]}')
        
        while True:
            blow_jet()
            if not can_move_down(rock_coordinates[current_rock_index], rock_position, grid):
                break;
            new_rock_position = (rock_position[0] - 1, rock_position[1])
            rock_position = new_rock_position
            # print(f'rock moved to {rock_position}')
        

        insert_rock(rock_coordinates[current_rock_index], rock_position, grid)

        # print(f'rock settled at {rock_position}')

        # print(f'grid {grid}')

        top_row = max(map(lambda x: x[0], grid.keys()))
        # print(f'new top row {top_row}')
        current_rock_index = (current_rock_index + 1) % len(rock_coordinates)

    print(top_row + 1)
    

    

    # top_row = max(map(grid))
    #need to get top of rock just fallen to update top_row
    #update current_rock_index

    # print(rock_position) 


    




if __name__ == '__main__':
    app.run(main)