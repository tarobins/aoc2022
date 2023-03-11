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

# def max_remaining(remaining, flows, time, current_node, graph):
#     time_to_next = graph[current_node][remaining[0]]
#     r = 0
#     for n in remaining:
#         r += (30 - time - time_to_next) * flows[n]
#     return r

max_reward = 0
num_permutations = 0

def permute(currentPurmutation: int, elementsToPermutate: int, graph, flows, current_node, partial_reward, time):
    global max_reward, num_permutations

    if elementsToPermutate == 0:
        num_permutations += 1
        max_reward = max(max_reward, partial_reward)
    else:
        for x in (1 << p for p in range(0, elementsToPermutate.bit_length())):
            if (not (elementsToPermutate & x)) or x == current_node :
                continue
            new_time = time + graph[current_node][x] + 1
            if (new_time > 30):
                max_reward = max(max_reward, partial_reward)
                continue
            new_reward = partial_reward + (30 - new_time) * flows[x]

            permute(currentPurmutation | x, elementsToPermutate &  ~x, graph, flows, x, new_reward, new_time)
    

def main(argv):
    graph = {}
    flows: dict = {}
    start_node = 1
    f = open(argv[1])

    next_node_id = 1
    node_ids = {}

    while line := f.readline():
        node_match = re.findall(r'[A-Z]{2}', line)
        node_id = node_ids.get(node_match[0])
        if not node_id:
            node_id = next_node_id
            next_node_id <<= 1
            node_ids[node_match[0]] = node_id
            
        graph[node_id] = {} 
            
        
        for neighbor in node_match[1:]:
            neighbor_id = node_ids.get(neighbor)
            if not neighbor_id:
                neighbor_id = next_node_id
                next_node_id <<= 1
                node_ids[neighbor] = neighbor_id
            graph[node_id][neighbor_id] = 1
        flow = int(re.findall(r'\d+', line)[0])
        if flow != 0:
            flows[node_id] = flow

    shortest_path(graph, node_ids.values())

    start_elements_to_permute = 0
    for flow_key in flows.keys():
        start_elements_to_permute |= flow_key
    
    print(f'start_elements_to_permute {start_elements_to_permute:b}')
    print(f'{flows}')
    print(f'{node_ids}')

    permute(0, start_elements_to_permute, graph, flows, start_node, 0, 0)

    print(f'max reward: {max_reward}')




if __name__ == '__main__':
    app.run(main)