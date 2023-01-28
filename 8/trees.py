from typing import Tuple

f = open("test_input.txt")

lines = [[ int(x) for x in j] for j in f.read().splitlines()]

height = len(lines)
width = len(lines[0])

def tree_view_direction(cells: list[Tuple[int, int]], tree_height: int):
    view = 0
    for cell in cells:
        row = cell[0]
        col = cell[1]
        if lines[row][col] < tree_height:
            view += 1
        else:
            view += 1
            break
    return view
        
        

def tree_score(row: int, col: int, width: int, height: int) -> int:
    tree_height = lines[row][col]
    up_trees = [(r, col) for r in range(row - 1, -1, -1)]
    left_trees = [(row, c) for c in range(col - 1, -1, -1)]
    right_trees = [(row, c) for c in range(col + 1, width, 1)]
    down_trees = [(r, col) for r in range(row + 1, height, 1)] 

    return tree_view_direction(up_trees, tree_height) * tree_view_direction(down_trees, tree_height) *\
        tree_view_direction(left_trees, tree_height) * tree_view_direction(right_trees, tree_height)

max_score = 0

for r in range(0, height):
    for c in range(0, width):
        rc_tree_score = tree_score(r, c, width, height)
        if rc_tree_score > max_score:
            max_score = rc_tree_score

print(max_score)
