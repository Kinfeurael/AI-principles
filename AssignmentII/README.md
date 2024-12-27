# Traveling Ethiopia Problem

## Overview
The **Traveling Ethiopia Problem** is a pathfinding challenge involving Ethiopian cities connected by road networks. The goal is to design an AI agent that can plan paths between cities or visit all cities optimally, using uninformed search strategies like BFS and DFS.

## Features
- **Graph Representation**:
  - Cities are represented as nodes, and roads as edges with distances (costs).
- **Pathfinding**:
  - Find a path between two cities using BFS or DFS.
  - Optionally, find a path visiting all cities exactly once.
- **Visualization**:
  - Visualize the road network and highlight the paths found.
- **Extendable**:
  - Handle dynamic road conditions (e.g., blocked roads).
  - Find k-shortest paths between cities.

## Requirements
- Python 3.8+
- Libraries:
  - `networkx`
  - `matplotlib`

Install the required libraries using:
```bash
pip install networkx matplotlib
```

## Getting Started

### Input Format
The problem uses a graph represented as a dictionary:
```python
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}
```

### Example Usage

#### 1. Visualization
Visualize the road network and highlight the paths found.
```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
for city, connections in roads.items():
    for neighbor, dist in connections:
        G.add_edge(city, neighbor, weight=dist)
# Plot
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.show()
```

#### 2. Single Path Finder
Find a path from a starting city to a goal city using BFS or DFS.
```python
from pathfinder import uninformed_path_finder

path, cost = uninformed_path_finder(
    cities, roads, 'Addis Ababa', 'Mekelle', 'bfs'
)
print(f"BFS Path: {path} with cost {cost}")
```

#### 3. Traverse All Cities
Find an optimal traversal path visiting all cities.
```python
from pathfinder import traverse_all_cities

path, cost = traverse_all_cities(cities, roads, 'Addis Ababa', 'dfs')
print(f"Traversal Path: {path} with cost {cost}")
```
## Functions

### `uninformed_path_finder`
Find a path between two cities using BFS or DFS.
```python
def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - goal_city: The destination city.
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').

    Returns:
    - path: List of cities representing the path from start_city to goal_city.
    - cost: Total cost (number of steps or distance) of the path.
    """
```

### `traverse_all_cities`
Find a traversal path visiting all cities.
```python
def traverse_all_cities(cities, roads, start_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').

    Returns:
    - path: List of cities representing the traversal path.
    - cost: Total cost (distance) of the traversal.
    """
```

## Example Output
```text
BFS Path: ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Mekelle'] with cost 990
Traversal Path: ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Mekelle', 'Hawassa'] with cost 1265
```

## Future Enhancements
- Add support for dynamic road conditions (e.g., blocked roads).
- Implement k-shortest paths algorithm.
