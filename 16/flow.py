from absl import app
import math
import re

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

def max_remaining(remaining, flows, time, current_node, graph):
    time_to_next = graph[current_node][remaining[0]]
    r = 0
    for n in remaining:
        r += (30 - time - time_to_next) * flows[n]
    return r

max_reward = 0
num_permutations = 0

def permute(currentPurmutation: list[str], elementsToPermutate: list[str], graph, flows, start_node, partial_reward, time):
    global max_reward, num_permutations
    current_node = start_node
    if len(currentPurmutation) > 0:
            current_node = currentPurmutation[-1]
    
    if len(elementsToPermutate) == 0:
        num_permutations += 1
        max_reward = max(max_reward, partial_reward)
    else:
        for e in elementsToPermutate:
            new_time = time + graph[current_node][e] + 1
            if (new_time > 30):
                max_reward = max(max_reward, partial_reward)
                continue
            new_reward = partial_reward + (30 - new_time) * flows[e]

            permute(currentPurmutation + [e], [i for i in elementsToPermutate if i != e], graph, flows, start_node, new_reward, new_time)
    

def main(argv):
    graph = {}
    flows = {}
    start_node = 'AA'
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

    permute([], list(flows.keys()), graph, flows, start_node, 0, 0)

    print(f'max reward: {max_reward}')




if __name__ == '__main__':
    app.run(main)