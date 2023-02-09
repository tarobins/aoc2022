from absl import app
from absl import flags



def main(argv):
    filename = argv[1]
    f = open(filename)

    cycle_count = 0
    reg = 0

    cycles_sum = 0

    pixels = ['.'] * 240

    while line := f.readline().strip():
        tokens = line.split(' ')
        # print(f'Processing {tokens} for {cycle_count} with {reg}')
        cmd = tokens[0]
        if (cmd == 'noop'):
            if (cycle_count + 1 - 20) % 40 == 0:
                cycles_sum += (cycle_count + 1) * (reg + 1)
            # print(f'{cycle_count} {reg} {cycle_count == reg + 1}')
            if (cycle_count % 40 == reg or cycle_count % 40 == reg + 1 or cycle_count % 40 == reg + 2):
                pixels[cycle_count] = '#'
            cycle_count += 1
        else:
            if (cycle_count + 1 - 20) % 40 == 0:
                cycles_sum += (cycle_count + 1) * (reg + 1)
            if (cycle_count + 2 - 20) % 40 == 0:
                cycles_sum += (cycle_count + 2) * (reg + 1) 
            if (cycle_count % 40 == reg or cycle_count % 40 == reg + 1 or cycle_count % 40 == reg + 2):
                pixels[cycle_count] = '#'
            if ((cycle_count + 1) % 40 == reg or (cycle_count + 1) % 40 == reg + 1 or (cycle_count + 1) % 40 == reg + 2):
                # print(f'Writing at {cycle_count + 1}')
                pixels[cycle_count + 1] = '#'
            val = int(tokens[1])
            cycle_count += 2
            reg += val

    print(cycles_sum)
    for i in range(0, 6):
        print(''.join(pixels[40*i:40 * (i + 1)]))

if __name__ == '__main__':
    app.run(main)