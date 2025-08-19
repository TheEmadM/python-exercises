from collections import deque

# Graph representing connections between people
graph = {}
graph["you"] = ["apple-alice", "pear-bob", "banana-claire"]
graph["pear-bob"] = ["carrot-anuj", "mango-peggy"]
graph["apple-alice"] = ["mango-peggy"]
graph["banana-claire"] = ["lemon-thom", "pineapple-jonny"]
graph["carrot-anuj"] = []
graph["mango-peggy"] = []
graph["lemon-thom"] = []
graph["pineapple-jonny"] = []

def person_is_seller(name: str) -> bool:
    """
    Checks if a given person's name indicates they are a mango seller.
    
    A person is considered a mango seller if their name starts with "mango".
    
    Args:
        name (str): The full name of the person (e.g., 'mango-peggy')
    
    Returns:
        bool: True if the person is a mango seller, False otherwise.
    """
    return str(name).lower().startswith("mango")


def search(name: str) -> bool:
    """
    Performs a breadth-first search (BFS) starting from the given person
    to find a mango seller in the graph.

    Args:
        name (str): The starting person's name (key in the graph dictionary)

    Returns:
        bool: True if a mango seller is found, False otherwise.
    """
    search_queue = deque(graph[name])  # Initialize the queue with neighbors
    searched = []  # Keep track of already searched people

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                # Extract the name after "mango-" and print it
                name_only = person.split("-", 1)[1] if "-" in person else person
                print(name_only + " is a mango seller")
                return True
            else:
                search_queue += graph.get(person, [])
                searched.append(person)
    return False


# Start searching from "you"
search("you")
