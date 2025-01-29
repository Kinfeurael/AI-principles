''' Task 1: Implement Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms for 
    the state space graph of Ethiopia.'''

#graph representation as an adjacency list of the state space graph of figure 1

graph = {
    "Asmara": ["Axum", "Adigrat"],
    "Axum": ["Asmara", "Shire","Adwa"],
    "Adigrat": ["Asmara", "Adwa", "Mekelle"],
    "Adwa": ["Axum", "Adigrat", "Mekelle"],
    "Mekelle": ["Adigrat", "Adwa", "Alamata", "Sekota"],
    "Sekota": ["Mekelle", "Alamata", "Lalibela"],
    "Lalibela": ["Sekota", "Woldia", "Debre Tabor"],
    "Alamata": ["Mekelle", "Sekota", "Woldia", "Samara"],
    "Woldia": ["Lalibela", "Dessie", "Alamata", "Samara"],
    "Dessie": ["Woldia", "Kemise"],
    "Kemise": ["Dessie", "Debre Sina"],
    "Debre Sina": ["Kemise", "Debre Birhan", "Debre Markos"],
    "Debre Birhan": ["Debre Sina", "Addis Ababa"],
    "Samara": ["Alamata", "Woldia", "Fanti Rasu", "Gabi Rasu"],
    "Fanti Rasu": ["Samara", "Killbet Rasu"],
    "Gabi Rasu": ["Samara", "Awash"],
    "Killbet Rasu": ["Fanti Rasu"],
    "Shire": ["Axum", "Humera", "Debark"],
    "Humera": ["Shire", "Gondar", "Khartoum"],
    "Debark": ["Shire", "Gondar"],
    "Gondar": ["Debark", "Humera", "Azezo", "Metema"],
    "Metema": ["Azezo", "Gondar", "Khartoum",],
    "Azezo": ["Gondar", "Metema", "Bahir Dar"],
    "Khartoum": ["Humera", "Metema"],
    "Bahir Dar": ["Azezo", "Debre Tabor", "Finote Selam", "Injibara", "Metekel"],
    "Debre Tabor": ["Bahir Dar", "Lalibela"],
    "Debre Markos": ["Finote Selam", "Debre Sina"],
    "Finote Selam": ["Bahir Dar", "Debre Markos", "Injibara"],
    "Injibara": ["Bahir Dar", "Finote Selam"],
    "Metekel": ["Bahir Dar", "Assosa"],
    "Addis Ababa": ["Debre Birhan", "Ambo", "Adama"],
    "Adama": ["Addis Ababa", "Matahara", "Assela", "Batu"],
    "Ambo": ["Addis Ababa", "Wolkite", "Nekemte"],
    "Nekemte": ["Ambo", "Gimbi", "Bedelle"],
    "Gimbi": ["Nekemte", "Dembi Dolo"],
    "Bedele": ["Nekemte", "Gore", "Jimma"],
    "Gore": ["Bedele", "Gambela", "Tepi"],
    "Dembi Dolo": ["Gimbi", "Assosa", "Gambela"],
    "Assosa": ["Metekel", "Dembi Dolo"],
    "Gambela": ["Dembi Dolo", "Gore"],
    "Wolkite": ["Ambo", "Jimma", "Worabe"],
    "Jimma": ["Bedele", "Wolkite", "Bonga"],
    "Bonga": ["Jimma", "Tepi", "Dawro", "Mizan Teferi"],
    "Tepi": ["Gore", "Mizan Teferi", "Bonga"],
    "Mizan Teferi": ["Tepi", "Bonga", "Basketo"],
    "Buta Jira": ["Worabe", "Batu"],
    "Batu": ["Buta Jira", "Adama", "Shashemene"],
    "Worabe": ["Buta Jira", "Wolkite", "Hossana"],
    "Shashemene": ["Batu", "Hawassa", "Dodolla", "Hossana"],
    "Hossana": ["Worabe", "Shashemene", "Wolaita Sodo"],
    "Wolaita Sodo": ["Dawro", "Hossana", "Arba Minch"],
    "Dawro": ["Wolaita Sodo", "Basketo", "Bonga"],
    "Arba Minch": ["Wolaita Sodo", "Basketo", "Konso"],
    "Basketo": ["Dawro", "Arba Minch", "Mizan Teferi", "Bench Maji"],
    "Bench Maji": ["Basketo", "Juba"],
    "Juba": ["Bench Maji"],
    "Hawassa": ["Shashemene", "Dilla"],
    "Dilla": ["Hawassa", "Bule Hora"],
    "Bule Hora": ["Dilla","Yabello"],
    "Yabello": ["Bule Hora", "Konso", "Moyale"],
    "Konso": ["Arba Minch", "Yabello",],
    "Moyale": ["Yabello", "Nairobi"],
    "Nairobi": ["Moyale"],
    "Assela": ["Adama", "Assasa"],
    "Assasa": ["Assela", "Dodolla"],
    "Dodolla": ["Assasa", "Shashemene", "Bale"],
    "Bale": ["Dodolla", "Goba", "Liben" "Sof Oumer"],
    "Liben": ["Bale"],
    "Goba": ["Bale", "Sof Oumer", "Dega Habur"],
    "Sof Oumer": ["Goba", "Bale", "Kebri Dehar"],
    "Matahara": ["Adama", "Awash"],
    "Awash": ["Matahara", "Gabi Rasu","Chiro"],
    "Chiro": ["Awash", "Dire Dawa"],
    "Dire Dawa": ["Chiro", "Harar"],
    "Harar": ["Dire Dawa", "Babille"],
    "Babille": ["Harar", "Jigjiga"],
    "Jigjiga": ["Babille", "Dega Habur"],
    "Dega Habur": ["Goba", "Jigjiga", "Kebri Dahar"],
    "Kebri Dahar": ["Sof Oumer", "Dega Habur", "Gode", "Werder"],
    "Werder": ["Kebri Dahar"],
    "Gode": ["Kebri Dahar", "Dollo","Mokadisho" ],
    "Dollo": ["Gode"],
    "Mokadisho": ["Gode"],
}
###########################################################################################################

# Breadth-First Search (BFS) and Depth-First Search (DFS) in Python
from collections import deque
class EthiopiaSearch:
    def __init__(self, graph, initial_state, goal_state):
        self.graph = graph  # Adjacency list representation of the graph
        self.initial_state = initial_state
        self.goal_state = goal_state

    def breadth_first_search(self):
        """Performs Breadth-First Search (BFS)"""
        queue = deque([[self.initial_state]])  # Queue to hold paths
        visited = set()  # To keep track of visited nodes

        while queue:
            path = queue.popleft()  # Get the first path in the queue
            node = path[-1]  # Get the last node in the path

            if node in visited:
                continue

            visited.add(node)

            # Check if we reached the goal state
            if node == self.goal_state:
                return path

            # Add neighbors to the queue
            for neighbor in self.graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

        return None  # No path found

    def depth_first_search(self):
        """Performs Depth-First Search (DFS)"""
        stack = [[self.initial_state]]  # Stack to hold paths
        visited = set()  # To keep track of visited nodes

        while stack:
            path = stack.pop()  # Get the last path in the stack
            node = path[-1]  # Get the last node in the path

            if node in visited:
                continue

            visited.add(node)

            # Check if we reached the goal state
            if node == self.goal_state:
                return path

            # Add neighbors to the stack
            for neighbor in self.graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

        return None  # No path found

    def search(self, strategy="bfs"):
        """Performs search based on the given strategy."""
        if strategy == "bfs":
            return self.breadth_first_search()
        elif strategy == "dfs":
            return self.depth_first_search()
        else:
            raise ValueError("Invalid search strategy. Use 'bfs' or 'dfs'.")
        
############################################################################################################

# Example usage
initial_state = "Addis Ababa"
goal_state = "Hawassa"

search_problem = EthiopiaSearch(graph, initial_state, goal_state)

# Perform BFS
bfs_path = search_problem.search(strategy="bfs")
print("BFS Path:", bfs_path)

# Perform DFS
dfs_path = search_problem.search(strategy="dfs")
print("DFS Path:", dfs_path)