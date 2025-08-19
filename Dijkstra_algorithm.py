"""
Dijkstra's Algorithm (shortest path)

This script finds the cheapest path from 'start' to 'fin' 
in a weighted directed graph using Dijkstra's algorithm.
"""

# 1. Build the graph (dictionary of dictionaries)
graph = {}
graph["start"] = {"a": 6, "b": 2}
graph["a"] = {"fin": 1}
graph["b"] = {"a": 3, "fin": 5}
graph["fin"] = {}

# 2. Track costs from 'start'
infinity = float("inf")
costs = {"a": 6, "b": 2, "fin": infinity}

# 3. Track parents (to reconstruct shortest path)
parents = {"a": "start", "b": "start", "fin": None}

# 4. Track processed nodes
processed = []


def find_lowest_cost_node(costs):
    """Return the unprocessed node with the lowest cost."""
    lowest_cost = float("inf")
    lowest_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_node = node
    return lowest_node


# 5. Main Dijkstra loop
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


def reconstruct_path(parents, end):
    """Reconstruct path from 'start' to end node using parents dict."""
    path = []
    while end is not None:
        path.insert(0, end)
        end = parents.get(end)
    return path


# 6. Results
print("Lowest costs:", costs)
print("Parents map:", parents)
print("Shortest path:", reconstruct_path(parents, "fin"))
