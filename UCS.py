import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        (cost, node, path) = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == goal:
            return (cost, path)

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))

    return float("inf"), []

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
goal_node = 'D'
cost, path = uniform_cost_search(graph, start_node, goal_node)

print(f"Path from {start_node} to {goal_node}: {path} with total cost: {cost}")