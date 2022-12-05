f = open("input.txt")

sum = 0

while line := f.readline():
    print(line.strip())
    numberOfItems = len(line) // 2
    itemsInFirstPocket = set()
    for i in range(0, numberOfItems):
        itemsInFirstPocket.add(line[i])
    print(itemsInFirstPocket)
    for i in range(numberOfItems, 2 * numberOfItems):
        item = line[i]
        if item in itemsInFirstPocket:
            print(f'item: {item}')
            if item >= 'a' and item <= 'z':
                val = ord(item) - ord('a') + 1
                print(f'val: {val}')
                sum += val
            else:
                val = ord(item) - ord('A') + 27
                print(f'val: {val}')
                sum += val
            break

print(sum)
    