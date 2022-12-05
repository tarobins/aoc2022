f = open("input.txt")

count = 0

while line := f.readline():
    ranges = line.split(',')
    range1 = ranges[0].split('-')
    range2 = ranges[1].split('-')

    range1Start = int(range1[0])
    range1End = int(range1[1])

    range2Start = int(range2[0])
    range2End = int(range2[1])

    if ((range1End >= range2Start and range1Start <= range2End) or 
        (range2End >= range1Start and range2Start <= range1End)):
        count += 1

print(count)