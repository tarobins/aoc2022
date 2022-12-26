f = open("test_input.txt")

lines = [[ int(x) for x in j] for j in f.read().splitlines()]

height = len(lines)
width = len(lines[0])

print(lines)

counted = [[False] * width for i in range(height)]

count = 0

for row in range(0, height):
    max = -1
    
    for col in range(0, width):
        if lines[row][col] > max:
            if not counted[row][col]:
                count += 1
                counted[row][col] = True
            max = lines[row][col]

for row in range(0, height):
    max = -1
    
    for col in range(width - 1, -1, -1):
        if lines[row][col] > max:
            if not counted[row][col]:
                count += 1
                counted[row][col] = True
            max = lines[row][col]
  
for col in range(0, height):
    max = -1
    
    for row in range(0, width):
        if lines[row][col] > max:
            if not counted[row][col]:
                count += 1
                counted[row][col] = True
            max = lines[row][col]

for col in range(0, height):
    max = -1
    
    for row in range(width - 1, -1, -1):
        if lines[row][col] > max:
            if not counted[row][col]:
                count += 1
                counted[row][col] = True
            max = lines[row][col]

print(count)

