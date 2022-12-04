import heapq

f = open("input.txt")

elf_sum = 0

max_elves = []

def update_max(elf_sum: int):
    global max_elves
    heapq.heappush(max_elves, elf_sum)
    if len(max_elves) > 3:
        heapq.heappop(max_elves)

while True:
    line = f.readline()
    if not line:
        print('-----')
        print(f'{elf_sum}')
        print()
        update_max(elf_sum)
        elf_sum = 0
        break
    if line == '\n':
        print('-----')
        print(f'{elf_sum}')
        print()
        update_max(elf_sum)
        elf_sum = 0
    else:
        elf_sum = elf_sum + int(line)
        print(f'{line.strip()}')

print(max_elves)
s = sum(max_elves)
print(f'max sum: {s}')
