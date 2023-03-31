from absl import app
import numpy as np
import re

def column_of_first_space(row: int, grid: np.ndarray[str]):
    return np.argmax(grid[row, :] == '.')

def column_of_last_space(row: int, grid: np.ndarray[str]):
    return len(grid[row, :]) - np.argmax(grid[row, ::-1] == '.') - 1

def row_of_first_space(col: int, grid: np.ndarray[str]):
    return np.argmax(grid[:, col] == '.')

def row_of_last_space(col: int, grid: np.ndarray[str]):
    return len(grid[:, col]) - np.argmax(grid[::-1, col] == '.') - 1

def column_of_first_position(row: int, grid: np.ndarray[str]):
    return np.argmax(np.isin(grid[row, :], ['.', '#']))

def column_of_last_position(row: int, grid: np.ndarray[str]):
    return len(grid[row, :]) - np.argmax(np.isin(grid[row, ::-1], ['.', '#'])) - 1

def row_of_first_position(col: int, grid: np.ndarray[str]):
    return np.argmax(np.isin(grid[:, col], ['.', '#']))

def row_of_last_position(col: int, grid: np.ndarray[str]):
    return len(grid[:, col]) - np.argmax(np.isin(grid[::-1, col], ['.', '#'])) - 1

def next_position(position: np.ndarray[int], direction: np.ndarray[int], grid: np.ndarray[str]):
    global left, right, up, down
    if np.array_equal(direction, left):
        if (position + direction)[1] < column_of_first_position(position[0], grid):
            return np.array([position[0], column_of_last_position(position[0], grid)])
        else:
            return position + direction
    elif np.array_equal(direction, right):
        if (position + direction)[1] > column_of_last_position(position[0], grid):
            return np.array([position[0], column_of_first_position(position[0], grid)])
        else:
            return position + direction
    elif np.array_equal(direction, up):
        if (position + direction)[0] < row_of_first_position(position[1], grid):
            return np.array([row_of_last_position(position[1], grid), position[1]])
        else:
            return position + direction
    elif np.array_equal(direction, down):
        if (position + direction)[0] > row_of_last_position(position[1], grid):
            return np.array([row_of_first_position(position[1], grid), position[1]])
        else:
            return position + direction

def move(position: np.ndarray[int], direction: np.ndarray[int], steps: int, grid: np.ndarray[str]):
    for _ in range(steps):
        np = next_position(position, direction, grid)
        if grid[np[0], np[1]] == '#':
            break
        position = np
    return position

left = np.array([0, -1])
right = np.array([0, 1])
up = np.array([-1, 0])
down = np.array([1, 0])

def turn(direction: np.ndarray[int], turn: str):
    global left, right, up, down
    if turn == 'L':
        if np.array_equal(direction, left):
            return down
        elif np.array_equal(direction, right):
            return up
        elif np.array_equal(direction, up):
            return left
        elif np.array_equal(direction, down):
            return right
    else:
        if np.array_equal(direction, left):
            return up
        elif np.array_equal(direction, right):
            return down
        elif np.array_equal(direction, up):
            return right
        elif np.array_equal(direction, down):
            return left
    

def main(argv):
    filename = argv[1]
    # filename = '22/test_input.txt'
    f = open(filename)
    lines = f.readlines()
    directions = lines.pop()
    lines.pop()
    lines = [line.rstrip() for line in lines]
    ncol = max(map(len, lines))
    nrow = len(lines)
    grid = np.zeros((nrow, ncol), dtype=str)
    for i, line in enumerate(lines):
        grid[i, :len(line)] = list(line)
    
    moves = re.split(r'[RL]', directions)
    turns = re.split(r'\d+', directions)[1:-1]

    # position = np.array([5, 3])
    # direction = left
    # new_position = move(position, direction, 4, grid)
    # print(f'new_position: {new_position}')

    position = np.array([0, column_of_first_space(0, grid)])
    direction = right

    print(f'starting position: {position} in direction {direction}')

    i = 0
    while True:
        position = move(position, direction, int(moves[i]), grid)
        print(f'move {i}: {moves[i]} to {position}')
        if i >= len(turns):
            break
        direction = turn(direction, turns[i])
        print(f'turn {i}: {turns[i]} to {direction}')
        i += 1
    
    print(f'final position: {position}')
    print(f'final direction: {direction}')
    
    direction_value = 0
    if np.array_equal(direction, left):
        direction_value = 2
    elif np.array_equal(direction, down):
        direction_value = 1
    elif np.array_equal(direction, up):
        direction_value = 3

    answer = (position[0] + 1)  * 1000 + (position[1] + 1) * 4 + direction_value

    print(f'answer: {answer}')



if __name__ == '__main__':
    app.run(main)