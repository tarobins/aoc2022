from absl import app
import re

number_match = r'(\d+)'

def convert_to_list(string, indent):
    print(f'{indent}convert_to_list:{string}')
    if string[0] == '[':
        sublist = convert_to_list(string[1:], indent + '  ')
        if sublist == None:
            return []
        else:
            return sublist
    elif string[0] == ']':
        return None
    else:
        val_string = re.match(number_match, string).group(1)
        print(f'{indent}val_string {val_string}')
        if string[len(val_string)] == ',':
            rest_of_string = string[len(val_string) + 1:]
        else:
            rest_of_string = string[len(val_string):]
        rest_of_list = convert_to_list(rest_of_string, indent + '  ')
        if rest_of_list == None:
            return [int(val_string)]
        else:
            return [int(val_string)] + rest_of_list


def main(argv):
    file_name = argv[1]

    f = open(file_name)

    left_string = f.readline()
    right_string = f.readline()

    left_string = '[[[]]]'
    # left = convert_to_list(left_string, '')
    left = eval(left_string)

    print(left)

    

if __name__ == '__main__':
    app.run(main)