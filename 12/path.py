from absl import app

def find_start(letters):
    starts = []
    for row_number, row in enumerate(letters):
        for column_number, cell in enumerate(row):
            if cell == 'S' or cell == 'a':
                starts.append((row_number, column_number))
    return starts

def getLetterCode(letter):
    if letter == 'S':
        return 'a'.encode()[0]
    elif letter == 'E':
        return 'z'.encode()[0]
    else:
        return letter.encode()[0]

def add_if_can_go(letters, new_position, current_letter_code, queue, visited):
    new_letter = letters[new_position[0]][new_position[1]]
    new_letter_code = getLetterCode(new_letter)
    if (new_position[0], new_position[1]) in visited:
        return
    if new_letter_code <= current_letter_code + 1:
        visited.add((new_position[0], new_position[1]))
        queue.append(new_position)

def find_path_length(letters, start):
    # print(f'Starting at {start}')
    height = len(letters)
    width = len(letters[0])

    queue = []
    queue.append(start + (0, ))
    visited = set()

    count = 0

    while True:
        if len(queue) == 0:
            return 99999
        current = queue.pop(0)
        
        count += 1
        current_letter = letters[current[0]][current[1]]
        if (current_letter == 'E'):
            return current[2]
        current_letter_code = getLetterCode(current_letter)

        if current[1] != 0:
            left = (current[0], current[1] - 1, current[2] + 1)
            add_if_can_go(letters, left, current_letter_code, queue, visited)
        if current[0] != 0:
            up = (current[0] - 1, current[1], current[2] + 1)
            add_if_can_go(letters, up, current_letter_code, queue, visited)
        if current[1] != width - 1:
            right = (current[0], current[1] + 1, current[2] + 1)
            add_if_can_go(letters, right, current_letter_code, queue, visited)
        if current[0] != height - 1:
            down = (current[0] + 1, current[1], current[2] + 1)
            add_if_can_go(letters, down, current_letter_code, queue, visited)

def main(argv):
    input_file = argv[1]
    f = open(input_file)

    letters = []

    while line := f.readline().strip():
        letters.append(list(line))
    
    start = find_start(letters)

    steps = min(map(lambda a : find_path_length(letters, a), start))

    print(f'Steps {steps}')

if __name__ == '__main__':
    app.run(main)