# Python Exercises

This repository contains Python exercises and small projects for learning purposes.

## Prerequisites

To run these exercises, make sure you have **Python 3 installed** on your system and clone this repository (or download it as a ZIP and extract it):

```bash
git clone https://github.com/TheEmadM/python-exercises.git
cd python-exercises
```
You can then run each exercise script directly with python filename.py (or python3 filename.py depending on your system).

## BFS Mango Seller Exercise

This exercise demonstrates a **breadth-first search (BFS)** algorithm in Python to find a "mango seller" in a graph.

### Learning points

- BFS using deque
- Avoid revisiting nodes
- String manipulation (startswith, split)

### How to run

```bash
python mango_seller.py 
```

## Dijkstra's Algorithm Exercise

This exercise demonstrates **Dijkstra's algorithm** to find the shortest (cheapest) path in a weighted directed graph.

### Description

- The graph is represented as a dictionary of dictionaries (adjacency list with weights).  
- Costs and parents are tracked in separate dictionaries.  
- The algorithm repeatedly selects the lowest-cost unprocessed node until all nodes are processed.  
- At the end, it prints the lowest costs, parents mapping, and reconstructs the shortest path from `"start"` to `"fin"`.


### Learning points

- Representing weighted graphs with nested dictionaries
- Implementing Dijkstra’s algorithm step by step
- Tracking processed nodes to avoid repetition
- Reconstructing the shortest path using a parent map

### How to run

```bash
python dijkstra_algorithm.py
```

