from absl import app
from absl import flags



def main(argv):
    filename = argv[1]
    f = open(filename)

    cycle_count = 1
    reg = 1

    cycles_sum = 0

    while line := f.readline().strip():
        tokens = line.split(' ')
        cmd = tokens[0]
        if (cmd == 'noop'):
            if (cycle_count - 20) % 40 == 0:
                cycles_sum += cycle_count * reg
            cycle_count += 1
        else:
            if (cycle_count - 20) % 40 == 0:
                cycles_sum += cycle_count * reg
            if (cycle_count + 1 - 20) % 40 == 0:
                cycles_sum += (cycle_count + 1) * reg
            val = int(tokens[1])
            cycle_count += 2
            reg += val

    print(cycles_sum)


if __name__ == '__main__':
    app.run(main)