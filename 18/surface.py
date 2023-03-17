from absl import app
from math import sqrt

def process_side(sides, side):
    if side in sides:
        sides[side] = sides[side] + 1
    else:
        sides[side] = 1

def get_sides(box):
    sides = []

    #xy
    sides.append(tuple(sorted(((box[0] + 1, box[1], box[2]), (box[0] + 1, box[1] + 1, box[2]), (box[0], box[1] + 1, box[2]), (box[0], box[1], box[2])))))
    sides.append(tuple(sorted(((box[0] + 1, box[1], box[2] + 1), (box[0] + 1, box[1] + 1, box[2] + 1), (box[0], box[1] + 1, box[2] + 1), (box[0], box[1], box[2] + 1)))))

    #xz
    sides.append(tuple(sorted(((box[0] + 1, box[1], box[2]), (box[0] + 1, box[1], box[2] + 1), (box[0], box[1], box[2] + 1), (box[0], box[1], box[2])))))
    sides.append(tuple(sorted(((box[0] + 1, box[1] + 1, box[2]), (box[0] + 1, box[1] + 1, box[2] + 1), (box[0], box[1] + 1, box[2] + 1), (box[0], box[1] + 1, box[2])))))

    #yz
    sides.append(tuple(sorted(((box[0], box[1] + 1, box[2]), (box[0], box[1] + 1, box[2] + 1), (box[0], box[1], box[2] + 1), (box[0], box[1], box[2])))))
    sides.append(tuple(sorted(((box[0] + 1, box[1] + 1, box[2]), (box[0] + 1, box[1] + 1, box[2] + 1), (box[0] + 1, box[1], box[2] + 1), (box[0] + 1, box[1], box[2])))))

    return sides

def main(argv):
    if len(argv) < 2:
        file_name = 'test_input.txt'
    else:
        file_name = argv[1]

    f = open(file_name)

    boxes = []

    while line := f.readline().strip():
        boxes.append(tuple(map(int, line.split(','))))

    sides = {}
    
    

    for box in boxes:
        # process_side(sides, (box[0] + 1, box[1], box[2]))
        # process_side(sides, (box[0] - 1, box[1], box[2]))
        # process_side(sides, (box[0], box[1] + 1, box[2]))
        # process_side(sides, (box[0], box[1] - 1, box[2]))
        # process_side(sides, (box[0], box[1], box[2] + 1))
        # process_side(sides, (box[0], box[1], box[2] - 1))
        # print(sides)
        # print(box)
        box_sides = get_sides(box)
        # print(box_sides)
        for box_side in box_sides:
            # print(f'box_side {box_side}')
            process_side(sides, box_side)

    print(len({element: count for (element, count) in sides.items() if count == 1}))

    # single_sides = 0
    # for box in boxes:
    #     near_box = 0
    #     for box2 in boxes:
    #         if box == box2:
    #             continue
    #         distance = sqrt((box[0] - box2[0]) ** 2 + (box[1] - box2[1]) ** 2 + (box[2] - box2[2]) ** 2)
    #         if distance == 1:
    #             near_box += 1
        
    #     single_sides += 6 - near_box

    # print(single_sides)




    # print(sides)
    # print(len({element: count for (element, count) in sides.items() if count > 1}))


    
    


if __name__ == '__main__':
    app.run(main)