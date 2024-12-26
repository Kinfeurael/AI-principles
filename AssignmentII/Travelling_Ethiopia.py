import networkx as nx
import matplotlib.pyplot as plt


# Data
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

'''Task #1 Graph representation and Visualization'''

def visualize_graph(cities, roads):
    G = nx.Graph()
    
    # Add edges to the graph
    for city, connections in roads.items():
        for connected_city, distance in connections:
            G.add_edge(city, connected_city, weight=distance)

    pos = nx.spring_layout(G)  # Layout for visualization
    
    # Draw the graph
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10)
    
    # Draw edge labels (distances)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Ethiopia Road Network")
    plt.show()

visualize_graph(cities, roads)

'''Task #2 Path Finding '''

from collections import deque

def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    visited = set()
    path = []
    cost = 0

    if strategy == 'bfs':
        # Breadth-First Search
        queue = deque([(start_city, [start_city], 0)])
        while queue:
            current_city, current_path, current_cost = queue.popleft()
            if current_city == goal_city:
                return current_path, current_cost
            if current_city not in visited:
                visited.add(current_city)
                for neighbor, distance in roads[current_city]:
                    queue.append((neighbor, current_path + [neighbor], current_cost + distance))

    elif strategy == 'dfs':
        # Depth-First Search
        stack = [(start_city, [start_city], 0)]
        while stack:
            current_city, current_path, current_cost = stack.pop()
            if current_city == goal_city:
                return current_path, current_cost
            if current_city not in visited:
                visited.add(current_city)
                for neighbor, distance in roads[current_city]:
                    stack.append((neighbor, current_path + [neighbor], current_cost + distance))

    return None, None

'''
#Example usage

# Find a path using BFS
start_city = 'Addis Ababa' 
goal_city =  'Mekelle'
path, cost = uninformed_path_finder(cities, roads, start_city, goal_city, strategy='bfs')
print("BFS Path:", path)
print("BFS Cost:", cost)

# Find a path using DFS
path, cost = uninformed_path_finder(cities, roads, start_city, goal_city, strategy='dfs')
print("DFS Path:", path)
print("DFS Cost:", cost) '''

