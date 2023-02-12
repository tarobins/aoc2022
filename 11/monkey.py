from absl import app
import re

class Monkey:
    
    def __init__(self, number, items: list[int], operation, test_mod, true_monkey, false_monkey) -> None:
        self.number = number
        self.items = items
        self.operation = operation
        self.test_mod = test_mod
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.number_of_items_inspected = 0

    def __str__(self):
        return f'Monkey {self.number}: Items: {self.items} Number of items inspected: {self.number_of_items_inspected}'
    
    def __repr__(self) -> str:
        return str(self)

    def accept_item(self, item):
        self.items.append(item)

    def process_items(self, monkeys: list['Monkey']):
        print(f'Monkey {self.number}')
        while self.items:
            self.number_of_items_inspected += 1
            item = self.items.pop(0)
            print(f'  Monkey inspects an item with a worry level of {item}.')
            new = eval(self.operation,{}, {'old': item})
            print(f'    Worry level changed to {new}')
            # new = int(new / 3)
            new = new % 9699690
            print(f'    Monkey gets bored with item. Worry level is divided by 3 to {new}')
            if new % self.test_mod == 0:
                print(f'    Current worry level is divisible by {self.test_mod}.')
                print(f'    Item with worry level {new} is thrown to monkey {self.true_monkey}.')
                monkeys[self.true_monkey].accept_item(new)
            else:
                print(f'    Current worry level is not divisible by {self.test_mod}.')
                print(f'    Item with worry level {new} is thrown to monkey {self.false_monkey}.')
                monkeys[self.false_monkey].accept_item(new)
            


def read_monkey(f):

    number_line = f.readline()
    if not number_line:
        return None

    number = int(re.search(r'(\d+)', number_line).group(0))

    items_line = f.readline()
    items = list(map(int, re.findall(r'(\d+)', items_line)))

    operation_line = f.readline()
    operation = re.search(r'\= (..*)', operation_line).group(1)

    test_line = f.readline()
    modulus = int(re.search(r'(\d+)', test_line).group(0))

    true_line = f.readline()
    true_monkey = int(re.search(r'(\d+)', true_line).group(0))

    false_line = f.readline()
    false_monkey = int(re.search(r'(\d+)', false_line).group(0))

    f.readline()

    # print(f'number {number}')
    # print(f'items {items}')
    # print(f'operation {operation}')
    # print(f'modulus {modulus}')
    # print(f'true monkey {true_monkey}')
    # print(f'false monkey {false_monkey}')

    return Monkey(number, items, operation, modulus, true_monkey, false_monkey)

def main(argv):
    input_file = argv[1]
    print(f'Input file: {input_file}')

    f = open(input_file)

    monkeys: list[Monkey] = []

    while True:
        m = read_monkey(f)
        if not m:
            break
        monkeys.append(m)
    for i in range(0, 10000):
        for monkey in monkeys:
            monkey.process_items(monkeys)

    for monkey in monkeys:
        print(f'Monkey {monkey.number} inspected items {monkey.number_of_items_inspected} times.')



if __name__ == '__main__':
    app.run(main)