from PrimAlgorithm import prim_minimum_spanning_tree
import networkx as nx
import matplotlib.pyplot as plt

example_graph = {
    'A': {'B': 2, 'D': 3, 'E': 2},
    'B': {'B': 2, 'C': 3},
    'C': {'B': 3, 'D': 4, 'F': 2},
    'D': {'C': 4, 'A': 3, 'E': 2, 'F': 4},
    'E': {'A': 2, 'D': 2},
    'F': {'C': 2, 'D': 4}}

minimum_spanning_tree = prim_minimum_spanning_tree(example_graph, 'A')

graph = nx.Graph()

for node_from in example_graph.keys():
    for node_to, value in example_graph[node_from].items():
        graph.add_edge(node_from, node_to, color='r', weight=6, label=value)

for node_from in example_graph.keys():
    for node_to, value in example_graph[node_from].items():
        if node_from in minimum_spanning_tree and node_to in minimum_spanning_tree[node_from]:
            graph.add_edge(node_from, node_to, color='g')

pos = nx.spring_layout(graph)
edges = graph.edges()
colors = [graph[u][v]['color'] for u, v in edges]
weights = [graph[u][v]['weight'] for u, v in edges]
edge_labels = dict([((u, v), d['label'])
                    for u, v, d in graph.edges(data=True)])

nx.draw(graph, pos, edges=edges, edge_color=colors, width=weights, with_labels=True,
        font_size=16, node_color='g', edge_labels=True)
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=14)

plt.show()
print example_graph
print minimum_spanning_tree
