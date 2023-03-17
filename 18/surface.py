from absl import app
from math import sqrt



def main(argv):
    if len(argv) < 2:
        file_name = '18/test_input.txt'
    else:
        file_name = argv[1]

    f = open(file_name)

    boxes = []

    while line := f.readline().strip():
        boxes.append(tuple(map(int, line.split(','))))

    face_count = 0
    visited = set()
    
    xs = [x for x, y, z in boxes]
    max_x = max(xs) + 1
    min_x = min(xs) - 1
    ys = [y for x, y, z in boxes]
    max_y = max(ys) + 1
    min_y = min(ys) - 1
    zs = [z for x, y, z in boxes]
    max_z = max(zs) + 1 
    min_z = min(zs) - 1

    start = (min_x, min_y, min_z)

    queue = [start]

    while len(queue) > 0:
        current = queue.pop(0)
        if current in visited:
            continue
        print(current)
        visited.add(current)

        # x + 1
        x_up = (current[0] + 1, current[1], current[2])
        if x_up in visited:
            pass
        elif x_up in boxes:
            face_count += 1
        elif x_up[0] > max_x:
            pass
        else:
            queue.append(x_up)

        # x - 1
        x_down = (current[0] - 1, current[1], current[2])
        if x_down in visited:
            pass
        elif x_down in boxes:
            face_count += 1
        elif x_down[0] < min_x:
            pass
        else:
            queue.append(x_down)
            
        # y + 1
        y_up = (current[0], current[1] + 1, current[2])
        if y_up in visited:
            pass
        elif y_up in boxes:
            face_count += 1
        elif y_up[1] > max_y:
            pass
        else:
            queue.append(y_up)

        # y - 1
        y_down = (current[0], current[1] - 1, current[2])
        if y_down in visited:
            pass
        elif y_down in boxes:
            face_count += 1
        elif y_down[1] < min_y:
            pass
        else:
            queue.append(y_down)
        
        # z + 1
        z_up = (current[0], current[1], current[2] + 1)
        if z_up in visited:
            pass
        elif z_up in boxes:
            face_count += 1
        elif z_up[2] > max_z:
            pass
        else:
            queue.append(z_up)

        # z - 1
        z_down = (current[0], current[1], current[2] - 1)
        if z_down in visited:
            pass
        elif z_down in boxes:
            face_count += 1
        elif z_down[2] < min_z:
            pass
        else:
            queue.append(z_down)    

    print(face_count)



    
    


if __name__ == '__main__':
    app.run(main)