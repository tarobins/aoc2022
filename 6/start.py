from collections import deque

f = open("input.txt")

s = f.readline()

print(s)

for i in range(3, len(s)):
    foundRepeat = False
    for j in range(i-3, i+1):
        for k in range(j + 1, i+1):
            print(f'checking {j} {k} {s[j]} {s[k]}')
            if s[j] == s[k]:
                print('found repeat')
                foundRepeat = True
    if (not foundRepeat):
        print(i + 1)
        break
    
