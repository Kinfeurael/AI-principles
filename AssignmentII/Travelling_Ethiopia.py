import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


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
    nx.draw(G, pos, with_labels=True, node_color='aqua', node_size=3000, font_size=10)
    
    # Draw edge labels (distances)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Travel Ethiopia")
    plt.show()

'''Task #2 Path Finding '''


def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    visited = set()
    if strategy == 'bfs':
        queue = deque([(start_city, [start_city], 0)])  # (current_city, path, cost)
        while queue:
            current, path, cost = queue.popleft()
            if current == goal_city:
                return path, cost
            if current not in visited:
                visited.add(current)
                for neighbor, dist in roads.get(current, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor], cost + dist))
    elif strategy == 'dfs':
        stack = [(start_city, [start_city], 0)]
        while stack:
            current, path, cost = stack.pop()
            if current == goal_city:
                return path, cost
            if current not in visited:
                visited.add(current)
                for neighbor, dist in roads.get(current, []):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor], cost + dist))
    return None, float('inf')

def traverse_all_cities(cities, roads, start_city, strategy):
    visited = set()
    path = []
    cost = 0

    def dfs(city):
        nonlocal cost
        if len(visited) == len(cities):
            return True  # All cities visited
        for neighbor, dist in roads.get(city, []):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                cost += dist
                if dfs(neighbor):  # Recursive call
                    return True
                # Backtrack
                path.pop()
                cost -= dist
                visited.remove(neighbor)
        return False

    if strategy == 'dfs':
        visited.add(start_city)
        path.append(start_city)
        dfs(start_city)
    return path, cost

''' Visit all cities example
path, cost = traverse_all_cities(cities, roads, 'Mekelle', 'dfs')
print(f"Traversal Path: {path} with cost {cost}")'''

visualize_graph(cities, roads)

