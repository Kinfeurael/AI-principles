import networkx as nx
import matplotlib.pyplot as plt

'''Task #1 Graph representation and Visualization'''

# Data
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

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
