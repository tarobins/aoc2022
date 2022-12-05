f = open("input.txt")

sum = 0

def getVal(item: str) -> int:
    if item >= 'a' and item <= 'z':
        val = ord(item) - ord('a') + 1
        return val
    else:
        val = ord(item) - ord('A') + 27
        return val


while line1 := f.readline().strip():
    line2 = f.readline().strip()
    line3 = f.readline().strip()
    
    print(line1)
    print(line2)
    print(line3)
    
    set1 = set(line1)
    set2 = set(line2)
    set3 = set(line3)


    dup = list(set1.intersection(set2).intersection(set3))[0]

    print(f'dup: {dup}')

    sum += getVal(dup)


print(sum)
    