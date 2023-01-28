from math import sqrt
from typing import Tuple

def distance(head: Tuple[int, int], tail: Tuple[int, int]) -> float:
    return sqrt(pow(head[0] - tail[0], 2) + pow(head[1] - tail[1], 2))

# print(distance((0,0), (0,0)))
# print(distance((1,0), (0,0)))
# print(distance((1,1), (0,0)))
# print(distance((1,2), (0,0)))
# print(distance((0,2), (0,0)))


def new_tail_position(head: Tuple[int, int], tail: Tuple[int, int]) -> Tuple[int, int]:
    current_distance = distance(head, tail)
    if (current_distance <= sqrt(2)):
        return tail
    else:
        tail_row = tail[0]
        tail_col = tail[1]
        if (tail_row < head[0]):
            tail_row += 1
        elif (tail_row > head[0]):
            tail_row -= 1
        if (tail_col < head[1]):
            tail_col += 1
        elif (tail_col > head[1]):
            tail_col -= 1
        return (tail_row, tail_col)

# print(new_tail_position((1,1), (0,0)))
# print(new_tail_position((1,0), (0,0)))
# print(new_tail_position((2,0), (0,0)))
# print(new_tail_position((1,2), (0,0)))
# print(new_tail_position((2,2), (0,0)))

def new_head_position(head: Tuple[int, int], command: str) -> Tuple[int, int]:
    if command == 'U':
        return (head[0] + 1, head[1])
    elif command == 'D':
        return (head[0] - 1, head[1])
    elif command == 'R':
        return (head[0], head[1] + 1)
    elif command == 'L':
        return (head[0], head[1] - 1)

# print(new_head_position((5,5), 'U'))
# print(new_head_position((5,5), 'D'))
# print(new_head_position((5,5), 'R'))
# print(new_head_position((5,5), 'L'))


visited = set()

f = open('test_input.txt')

# commands:list[Tuple[str, int]] = []
head = (0,0)
tail = (0,0)
visited.add(tail)

while line := f.readline().strip():
    command = line.split(' ')
    command_name = command[0]
    command_count = int(command[1])
    
    for i in range(0, command_count):
        head = new_head_position(head, command_name)
        tail = new_tail_position(head, tail)
        visited.add(tail)

print(len(visited))
        



