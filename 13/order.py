from absl import app
from copy import deepcopy
import re

number_match = r'(\d+)'

def convert_number(string, indent):
    # print(f'{indent}convert_number: {string}')
    val_string = re.match(number_match, string).group(1)
    rest_of_string = string[len(val_string):]
    return ([int(val_string)], rest_of_string)

def convert_list_contents(string: str, indent):
    # print(f'convert_list_contents: {string}')
    remaining_string = string
    list = []
    while True:
        if remaining_string[0] == ',':
            remaining_string = remaining_string[1:]
        elif remaining_string[0] == ']':
            return (list, remaining_string)
        elif remaining_string[0] == '[':
                (sublist, remaining_string) = convert_list(remaining_string, indent + '  ')
                list.append(sublist)
        elif remaining_string[0].isdigit():
            (sublist, remaining_string) = convert_number(remaining_string, indent + '  ')
            list.extend(sublist)
        else:
            exit('convert_list_contents: Unexpected charater')
    

def convert_list(string: str, indent):
    # print(f'{indent}convert_list: {string}')
    if string[0] == '[':
        (list, remaining_string) = convert_list_contents(string[1:], indent + '  ')
        if remaining_string[0] != ']':
            exit('Unexpected charater, missing ]')
        else:
            return (list, remaining_string[1:])
    else:
        exit('convert_list: Unexpected charater')

def compare_list_elements(left, right):
    if not isinstance(left, list):
        return compare_list([left], right)
    elif not isinstance(right, list):
        return compare_list(left, [right])
    else: 
        return compare_list(left, right)

def compare_list(left, right):
    # print(f'Compare {left} to {right}')
    for l in left:
        # print(f'left {l}')
        if len(right) == 0:
            return False
        r = right.pop(0)
        # print(f'right {r}')
        if isinstance(l, list) or isinstance(r, list):
           res = compare_list_elements(l, r)
           if res != None:
             return res
        elif l < r:
            # print(f'C')
            return True
        elif l > r:
            # print(f'D')
            return False
    if len(right) != 0:
        # print(f'E')
        return True
    # print(f'F')

def find_position(target, elements):
    count = 0
    for pair in elements:
        # print(f'pair if {pair}')
        if not compare_list(deepcopy(target), deepcopy(pair)):
            count += 1
            # print(f'A pair is {pair}')
            # print('A')
        else:
            # print(f'B pair is {pair}')
            # print('B')
            pass
    return count + 1



def main(argv):
    file_name = argv[1]

    f = open(file_name)

    elements = []

    while left_string := f.readline().strip():
        right_string = f.readline().strip()
        f.readline()
        elements.append(convert_list(left_string, '')[0])
        elements.append(convert_list(right_string, '')[0])

    print(elements)
    
    p1 = find_position([[2]], elements)
    p2 = find_position([[6]], elements) + 1
    # print(p2)
    print(p1 * p2)

    # while left_string := f.readline().strip():
    #     pair += 1
    #     right_string = f.readline().strip()
    #     f.readline()
    #     (left, _) = convert_list(left_string, '')
    #     (right, _) = convert_list(right_string, '')
    #     r = compare_list(left, right)
    #     if r:
    #         sum += pair
    
    # print(sum)


    # left = [1, [1, 1], 1, 1]
    # right = [1, [1], 1, 1]

    # print(left)
    # print(right)

    # r = compare_list(left, right)

    # print(r)

    

if __name__ == '__main__':
    app.run(main)