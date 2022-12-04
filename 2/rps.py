f = open("input.txt")

total = 0

while line := f.readline():
    play = line.strip().split()
    print(play)
    them = ord(play[0]) - ord('A')
    me = ord(play[1]) - ord('X')
    print(f'{them} {me}')
    score = (me - them + 1) % 3 * 3 + me + 1
    print(score)
    total += score

print(f'total: {total}')