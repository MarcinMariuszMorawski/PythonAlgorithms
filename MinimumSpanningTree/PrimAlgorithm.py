from collections import defaultdict
import heapq


def prim_minimum_spanning_tree(graph, start):
    current = start
    vertices = len(graph)
    visited = dict.fromkeys(graph.keys(), False)
    visited_count = 1
    heap = []
    minimum_spanning_tree = defaultdict(set)

    while visited_count <= vertices:
        if visited[current] is False:
            visited[current] = True
            for to, length in graph[current].items():
                heapq.heappush(heap, (length, (current, to)))
            len_of_edge, edge = heapq.heappop(heap)
            if visited[edge[1]] is False:
                minimum_spanning_tree[edge[0]].add(edge[1])
            current = edge[1]
            visited_count += 1
        else:
            len_of_edge, edge = heapq.heappop(heap)
            if visited[edge[1]] is False:
                minimum_spanning_tree[edge[0]].add(edge[1])
            current = edge[1]
    return minimum_spanning_tree
