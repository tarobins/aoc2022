from absl import app

def visit(node_name, nodes):
    node_children = nodes[node_name]
    if isinstance(node_children, int):
        return node_children
    else:
        left = visit(node_children[0], nodes)
        right = visit(node_children[2], nodes)
        if node_children[1] == '+':
            return left + right
        elif node_children[1] == '-':
            return left - right
        elif node_children[1] == '*':
            return left * right
        else:
            return left / right
        
def path_to_humn(node_name, nodes):
    print(f'path_to_humn on {node_name}')
    node_children = nodes[node_name]
    if node_name == 'humn':
        return ['humn']
    if isinstance(node_children, int):
        return None
    sub_path = path_to_humn(node_children[0], nodes)
    if sub_path == None:
        sub_path = path_to_humn(node_children[2], nodes)
    if sub_path == None:
        return None
    return [node_name] + sub_path

def solve_humn(node_name, expected_value, nodes, humn_path):
    if node_name == 'humn':
        return expected_value
    node_children = nodes[node_name]
    if isinstance(node_children, int):
        print('wtf')
    left_child_name = node_children[0]
    op = node_children[1]
    right_child_name = node_children[2]
    if not left_child_name in humn_path:
        left_value = visit(left_child_name, nodes)
        if op == '+':
            return solve_humn(right_child_name, expected_value - left_value, nodes, humn_path)
        elif op == '-':
            return solve_humn(right_child_name, left_value - expected_value, nodes, humn_path)
        elif op == '*':
            return solve_humn(right_child_name, expected_value / left_value, nodes, humn_path)
        else:
            return solve_humn(right_child_name,left_value / expected_value, nodes, humn_path)
    else:
        right_value = visit(right_child_name, nodes)
        if op == '+':
            return solve_humn(left_child_name, expected_value - right_value, nodes, humn_path)
        elif op == '-':
            return solve_humn(left_child_name, right_value + expected_value, nodes, humn_path)
        elif op == '*':
            return solve_humn(left_child_name, expected_value / right_value, nodes, humn_path)
        else:
            return solve_humn(left_child_name,right_value * expected_value, nodes, humn_path)


def main(argv):
    f = open(argv[1])
    # f = open('21/test_input.txt')

    nodes = {}

    while line := f.readline().strip():
        tokens = line.split(' ')
        # print(tokens)
        if len(tokens) == 2:
            nodes[tokens[0][:-1]] = int(tokens[1])
        else:
            nodes[tokens[0][:-1]] = (tokens[1], tokens[2], tokens[3])
    
    nodes['root'] = (nodes['root'][0], '-', nodes['root'][2])
    # print(nodes)
    # print(visit(nodes['root'], nodes))
    humn_path = path_to_humn('root', nodes)
    print(solve_humn('root', 0, nodes, humn_path))

    # root_node_children = nodes['root']
    # left_child_name = root_node_children[0]
    # right_child_name = root_node_children[2]
    # if 




if __name__ == "__main__":
    app.run(main)