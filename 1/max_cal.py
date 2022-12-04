f = open("input.txt")

max = 0
sum = 0

def update_max(sum: int):
    global max
    if sum > max:
        max = sum 

while True:
    line = f.readline()
    if not line:
        print('-----')
        print(f'{sum}')
        print()
        update_max(sum)
        sum = 0
        break
    if line == '\n':
        print('-----')
        print(f'{sum}')
        print()
        update_max(sum)
        sum = 0
    else:
        sum = sum + int(line)
        print(f'{line.strip()}')

print()
print(f'max: {max}')
