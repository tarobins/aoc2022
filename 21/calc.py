from absl import app

def visit(node, nodes):
    if isinstance(node, int):
        return node
    else:
        left = visit(nodes[node[0]], nodes)
        right = visit(nodes[node[2]], nodes)
        if node[1] == '+':
            return left + right
        elif node[1] == '-':
            return left - right
        elif node[1] == '*':
            return left * right
        else:
            return left / right

def main(argv):
    f = open(argv[1])

    nodes = {}

    while line := f.readline().strip():
        tokens = line.split(' ')
        # print(tokens)
        if len(tokens) == 2:
            nodes[tokens[0][:-1]] = int(tokens[1])
        else:
            nodes[tokens[0][:-1]] = (tokens[1], tokens[2], tokens[3])
    
    # print(nodes)
    print(visit(nodes['root'], nodes))



if __name__ == "__main__":
    app.run(main)