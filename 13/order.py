from absl import app
import re

number_match = r'(\d+)'

def convert_number(string, indent):
    print(f'{indent}convert_number: {string}')
    val_string = re.match(number_match, string).group(1)
    rest_of_string = string[len(val_string):]
    return ([int(val_string)], rest_of_string)

def convert_list_contents(string: str, indent):
    print(f'convert_list_contents: {string}')
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
    print(f'{indent}convert_list: {string}')
    if string[0] == '[':
        (list, remaining_string) = convert_list_contents(string[1:], indent + '  ')
        if remaining_string[0] != ']':
            exit('Unexpected charater, missing ]')
        else:
            return (list, remaining_string[1:])
    else:
        exit('convert_list: Unexpected charater')


def main(argv):
    file_name = argv[1]

    f = open(file_name)

    left_string = f.readline()
    right_string = f.readline()

    left_string = '[[4,4],[4],4,[],[5,[6]]]'


    (left, _) = convert_list(left_string, '')
    # left = eval(left_string)

    print(left)

    

if __name__ == '__main__':
    app.run(main)