''' Task 4: Adversial Search '''

# Implementing  the minimax algorithm to find the best achievable destination.

# The state space graph from figure 4.
class CoffeeMinimaxAgent:
    def __init__(self):
        self.graph = {
            "Addis Ababa": ["Ambo", "Buta Jirra", "Adama"],
            "Adama": ["Addis Ababa", "Dire Dawa", "Mojo"],
            "Mojo": ["Kaffa", "Dilla"],
            "Dire Dawa": ["Chiro", "Harar"],
            "Buta Jirra": ["Addis Ababa", "Wolkite", "Worabe"],
            "Wolkite": ["Tepi", "Bench Naji"],
            "Worabe": ["Durame", "Hossana"],
            "Ambo": ["Nekemte", "Gedo"],
            "Nekemte": ["Limu", "Gimbi"],
            "Gedo": ["Shambu", "Fincha"]
        }
        self.utility_values = {
            "Harar": 10,
            "Chiro": 6,
            "Dilla": 9,
            "Kaffa": 7,
            "Tepi": 6,
            "Bench Naji": 5,
            "Durame": 5,
            "Hossana": 6,
            "Limu": 8,
            "Gimbi": 8,
            "Shambu": 4,
            "Fincha": 5
        }
    
    def minimax(self, current_city, visited, is_max_turn):
        if current_city in self.utility_values:
            return (self.utility_values[current_city], [current_city])
        
        if is_max_turn:
            best_value = float('-inf')
            best_path = []
            for neighbor in self.graph[current_city]:
                if neighbor not in visited:
                    new_visited = visited.copy()
                    new_visited.add(neighbor)
                    value, path = self.minimax(neighbor, new_visited, False)
                    if value > best_value:
                        best_value = value
                        best_path = [current_city] + path
            return (best_value, best_path)
        else:
            best_value = float('inf')
            best_path = []
            for neighbor in self.graph[current_city]:
                if neighbor not in visited:
                    new_visited = visited.copy()
                    new_visited.add(neighbor)
                    value, path = self.minimax(neighbor, new_visited, True)
                    if value < best_value:
                        best_value = value
                        best_path = [current_city] + path
            return (best_value, best_path)
    
    def find_best_destination(self):
        start_city = "Addis Ababa"
        visited = {start_city}
        utility, path = self.minimax(start_city, visited, True)
        destination = path[-1] if path else None
        return {
            'destination': destination,
            'utility': utility,
            'path': path
        }

# Example usage:
if __name__ == "__main__":
    agent = CoffeeMinimaxAgent()
    result = agent.find_best_destination()
    print(f"Best Destination: {result['destination']}")
    print(f"Utility: {result['utility']}")
    print(f"Path: {' -> '.join(result['path'])}")