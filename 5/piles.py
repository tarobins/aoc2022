from collections import deque

f = open("input.txt")

piles:dict[int, deque[str]] = {}

for i in range(0, 9):
    piles[i] = deque[list]()

print(piles)

while line := f.readline():
    if line.strip().startswith('['):
        index = 0
        while True:
            index = line.find('[', index)
            print(f'index {index}')
            if index == -1:
                break
            col = index // 4
            val = line[index+1]
            print(f'col: {col}, val: {line[index+1]}')
            piles[col].append(val)
            index += 2
    if line.strip().startswith('move'):
        tokens = line.split(' ')
        print(tokens)
        count = int(tokens[1])
        frm = int(tokens[3]) - 1
        to = int(tokens[5]) - 1
        print(count, frm, to)
        piles[frm].rotate(-1 * count)
        for i in range(0, count):
            item = piles[frm].pop()
            piles[to].appendleft(item)

    

result = ''

for i in range(0,9):
    result = result + piles[i].popleft()

print(result)
        
        



