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
    # Initialize costs and parents (making 2 hash tables (costs and parents) and an array for recording fully processed nodes)
    infinity = float("inf")
    costs = {node: infinity for node in graph}
    costs[start] = 0
    parents = {node: None for node in graph}
    processed = []


    # Consider that all the nodes at the beginning are of cost inf and only start is 0. 
    # So in the first loop it chooses start for the lowest node.
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
        # Neighbors are a list of all neighbors of current lowest node. We check all of them in following loop.
        neighbors = graph[node]
        # Here it chooses all neighbors of the lowest which in the first loop they are the neighbors of start. 
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        # The node that is processed here is the node that we evaluate all its neighbors.
        # In first loop the start node is fully processed.
        processed.append(node)
        # Then when new costs are updated for its neighbors, we start to choose the next node to be processed from them.
        # In first loop it is simple: the neighbor with lowest cost from start.
        node = find_lowest_cost_node(costs)

    # Reconstruct path
    path = []
    curr = end
    while curr is not None:
        path.insert(0, curr)
        curr = parents[curr]

    return path, costs[end], costs


# Example usage

if __name__ == "__main__":
    graph = {
        "start": {"a": 6, "b": 2},
        "a": {"fin": 1},
        "b": {"a": 3, "fin": 5},
        "fin": {}
    }
    path, total_cost, all_costs = dijkstra(graph, "start", "fin")
    print("Shortest path:", path)
    print("Total cost:", total_cost)
