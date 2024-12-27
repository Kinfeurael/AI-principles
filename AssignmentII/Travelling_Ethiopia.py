import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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

'''Task #3 Create an agent guided by any strategy t go from one random state to all other states optimally.'''

def traverse_all_cities(cities, roads, start_city, strategy): 
  
    visited = set() 
    path = [] 
    total_cost = 0 
 
    frontier = deque([(start_city, [], 0)]) if strategy == 'bfs' else [(start_city, [], 0)]  # (current_city, path_so_far, cost_so_far) 
 
    while frontier: 
        current_city, current_path, cost_so_far = ( 
            frontier.popleft() if strategy == 'bfs' else frontier.pop() 
        ) 
 
        if current_city in visited: 
            continue 
 
        
        visited.add(current_city) 
        current_path = current_path + [current_city] 
 
        
        path = current_path 
        total_cost = cost_so_far 
 
        
        for neighbor, distance in roads.get(current_city, []): 
            if neighbor not in visited: 
                frontier.append((neighbor, current_path, cost_so_far + distance)) 
 
    return path, total_cost  





# Data
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}


 #Visit all cities example
path, cost = traverse_all_cities(cities, roads, 'Addis Ababa', 'bfs')
print(f"Traversal Path: {path} with cost {cost}")

visualize_graph(cities, roads)
