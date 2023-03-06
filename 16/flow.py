from absl import app
import math
import re
import itertools

def shortest_path(graph, nodes):
    for i in nodes:
        for j in nodes:
            if i == j:
                graph[i][j] = 0
                continue
            if not j in graph[i].keys():
                graph[i][j] = math.inf

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if graph[i][j] > graph[i][k] + graph[j][k]:
                    graph[i][j] = graph[i][k] + graph[j][k]

max_reward = 0

def permute(currentPurmutation: list[str], elementsToPermutate: list[str], graph, flows, start_node, partial_reward, time):
    global max_reward
    if len(elementsToPermutate) == 0:
        # print(f'perm {currentPurmutation}')
        max_reward = max(max_reward, partial_reward)
    else:
        for e in elementsToPermutate:
            last_node = start_node
            if len(currentPurmutation) > 0:
                last_node = currentPurmutation[-1]
            new_time = time + graph[last_node][e] + 1
            new_reward = partial_reward + (30 - new_time) * flows[e]
            permute([c for c in currentPurmutation] + [e], [i for i in elementsToPermutate if i != e], graph, flows, start_node, new_reward, new_time)
    

def main(argv):
    graph = {}
    flows = {}
    start_node = None
    nodes = set()
    f = open(argv[1])
    while line := f.readline():
        node_match = re.findall(r'[A-Z]{2}', line)
        if not start_node:
            start_node = node_match[0]
        graph[node_match[0]] = {}
        nodes.add(node_match[0])
        for neighbor in node_match[1:]:
            graph[node_match[0]][neighbor] = 1
        flow = int(re.findall(r'\d+', line)[0])
        if flow != 0:
            flows[node_match[0]] = flow

    shortest_path(graph, nodes)
    
    print(f'graph {graph}')
    print(f'flows {flows})')
    print(f'start_node {start_node}')

    permute([], list(flows.keys()), graph, flows, start_node, 0, 0)

    print(f'max reward: {max_reward}')

    # test_permutation = ['DD', 'BB', 'JJ', 'HH', 'EE', 'CC']

    # print(f'test_permutation {test_permutation}')
    # r = permutation_reward(test_permutation, graph, flows, start_node)

    # print(f'reward {r}')




    # zero_node_names = [k for k,v in flows.items() if v == 0 and k != start_node]
    # print(f'zeros_nodes {zero_node_names}')

    # for zero_node_name in zero_node_names:
    #     zero_node = graph[zero_node_name]
    #     print(f'process zero node: {zero_node_name} = {zero_node}')
    #     for a in zero_node:
    #         for b in zero_node:
    #             a_node = graph[a]
    #             b_node = graph[b]
    #             print(a, a_node, b, b_node)
        

if __name__ == '__main__':
    app.run(main)