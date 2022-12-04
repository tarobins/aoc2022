f = open("input.txt")

total = 0

while line := f.readline():
    play = line.strip().split()
    print(play)
    c = ord(play[0]) - ord('A')
    r = ord(play[1]) - ord('X')
    print(f'{r} {c}')
    score = (c + r - 1) % 3 + 1 + 3 * r
    print(score)
    total += score

print(f'total: {total}')