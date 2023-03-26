from absl import app

def current_location(data, original_index):
    return [i for i in range(len(data)) if data[i][0] == original_index][0]

def item_location(data, item):
    return [i for i in range(len(data)) if data[i][1] == item][0]

def main(argv):
    if len(argv) < 2:
        f = open('20/test_input.txt')
    else:
        f = open(argv[1])
    d = list(enumerate([int(line.strip()) * 811589153 for line in f.readlines()]))

    # print(f'Initial:\n{[i[1] for i in d]}')
    for j in range(10):
        for i in range(len(d)):
            cur_index = current_location(d, i)
            cur_item = d[cur_index]
            d.pop(cur_index)
            new_index = ((cur_index % len(d)) + cur_item[1]) % len(d)
            d.insert(new_index, cur_item)
        # print(f'after {i} ({cur_item[1]} moves)\n{[i[1] for i in d]}')
        
    index_of_zero = item_location(d, 0)

    print(f'index_of_zero {index_of_zero}')

    index_1000 = (index_of_zero + 1000) % len(d)
    index_2000 = (index_of_zero + 2000) % len(d)
    index_3000 = (index_of_zero + 3000) % len(d)

    print(f'1000th {index_1000} = {d[index_1000][1]}')
    print(f'2000th {index_2000} = {d[index_2000][1]}')
    print(f'3000th {index_3000} = {d[index_3000][1]}')

    ans = d[index_1000][1] + d[index_2000][1] + d[index_3000][1]

    print(ans)



if __name__ == '__main__':
    app.run(main)