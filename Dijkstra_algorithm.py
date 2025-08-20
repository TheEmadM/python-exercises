"""
Dijkstra's Algorithm (shortest path)

This module finds the shortest path from a start node to an end node 
in a weighted directed graph using Dijkstra's algorithm.
"""

def dijkstra(graph, start, end):
    """
    Find the shortest path and its cost using Dijkstra's algorithm.

    Args:
        graph (dict): A dictionary of dictionaries representing the weighted graph.
                      E.g., {"start": {"a": 6, "b": 2}, ...}
        start (str): The starting node.
        end (str): The destination node.

    Returns:
        tuple:
            - path (list): The shortest path from start to end.
            - total_cost (float): Total cost of the shortest path.
            - costs (dict): Costs to reach all nodes from the start.
    """
    # Initialize costs and parents
    infinity = float("inf")
    costs = {node: infinity for node in graph}
    costs[start] = 0
    parents = {node: None for node in graph}
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

    # Main loop
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

    # Reconstruct path
    path = []
    curr = end
    while curr is not None:
        path.insert(0, curr)
        curr = parents[curr]

    return path, costs[end], costs


# Example usage
graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}

path, total_cost, all_costs = dijkstra(graph, "start", "fin")
print("Shortest path:", path)
print("Total cost:", total_cost)
