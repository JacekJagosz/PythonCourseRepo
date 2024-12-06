import heapq

def dijkstra(graph, start):
    # Dict to store the shortest path to each node
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0

    # Priority queue to keep track of nodes to visit
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the distance in the priority queue is larger, we've already found a shorter path
        if current_distance > shortest_paths[current_node]:
            continue

        # Check neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this path if it's better
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths



graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
