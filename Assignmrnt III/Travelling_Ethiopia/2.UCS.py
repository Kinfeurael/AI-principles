
# Task 2: Uniform Cost Search (UCS) and Customized UCS for visiting multiple goals

# Graph representation using adjacency list of figure 2

graph = {
    "Asmara": {"Axum": 5, "Adigrat": 6},
    "Axum": {"Asmara": 5, "Shire": 2, "Adwa": 1},
    "Adigrat": {"Asmara": 6, "Adwa": 4, "Mekelle": 4},
    "Adwa": {"Axum": 1, "Adigrat": 4, "Mekelle": 7},
    "Mekelle": {"Adigrat": 4, "Adwa": 7, "Alamata": 5, "Sekota":9},
    "Sekota": {"Mekelle": 9, "Alamata": 6, "Lalibela": 6},
    "Lalibela": {"Sekota": 6, "Woldia": 7, "Debre Tabor": 8},
    "Alamata": {"Mekelle": 5, "Sekota": 6, "Woldia": 3, "Samara": 11},
    "Woldia": {"Lalibela": 7, "Dessie": 6, "Alamata": 3, "Samara": 8},
    "Dessie": {"Woldia": 6, "Kemise": 4},
    "Kemise": {"Dessie": 4, "Debre Sina": 6},
    "Debre Sina": {"Kemise": 6, "Debre Birhan": 2, "Debre Markos": 17},
    "Debre Birhan": {"Debre Sina": 2, "Addis Ababa": 5},
    "Samara": {"Alamata": 11, "Woldia": 8, "Fanti Rasu": 7, "Gabi Rasu": 9},
    "Fanti Rasu": {"Samara": 7, "Killbet Rasu": 6},
    "Gabi Rasu": {"Samara": 9, "Awash": 5},
    "Killbet Rasu": {"Fanti Rasu": 6},
    "Shire": {"Axum": 2, "Humera": 8, "Debark": 7},
    "Humera": {"Shire": 8, "Gondar": 9, "Khartoum": 21},
    "Debark": {"Shire": 7, "Gondar": 4},
    "Gondar": {"Debark": 4, "Humera": 9, "Azezo": 1, "Metema": 7},
    "Metema": {"Azezo": 7, "Gondar": 7, "Khartoum": 19},
    "Azezo": {"Gondar": 1, "Metema": 7, "Bahir Dar": 7},
    "Khartoum": {"Humera": 21, "Metema": 19},
    "Bahir Dar": {"Azezo": 7, "Debre Tabor": 4, "Finote Selam": 6, "Injibara": 4, "Metekel": 11},
    "Debre Tabor": {"Bahir Dar": 4, "Lalibela": 8},
    "Debre Markos": {"Finote Selam": 3, "Debre Sina": 17},
    "Finote Selam": {"Bahir Dar": 6, "Debre Markos": 3, "Injibara": 2},
    "Injibara": {"Bahir Dar": 4, "Finote Selam": 2},
    "Metekel": {"Bahir Dar": 11},
    "Addis Ababa": {"Debre Birhan": 5, "Ambo": 5, "Adama": 3},
    "Adama": {"Addis Ababa": 3, "Matahara": 3, "Assela": 4, "Batu": 4},
    "Ambo": {"Addis Ababa": 5, "Wolkite": 6, "Nekemte": 9},
    "Nekemte": {"Ambo": 9, "Gimbi": 4, "Bedelle": 2},
    "Gimbi": {"Nekemte": 4, "Dembi Dolo": 6},
    "Bedelle": {"Nekemte": 2, "Gore": 6, "Jimma": 7},
    "Gore": {"Bedelle": 6, "Gambela": 5, "Tepi": 9},
    "Dembi Dolo": {"Gimbi": 6, "Assosa": 12, "Gambela": 4},
    "Assosa": {"Dembi Dolo": 12},
    "Gambela": {"Dembi Dolo": 4, "Gore": 5},
    "Wolkite": {"Ambo": 6, "Jimma": 8, "Worabe": 5},
    "Jimma": {"Bedelle": 7, "Wolkite": 8, "Bonga": 4},
    "Bonga": {"Jimma": 4, "Tepi": 8, "Dawro": 10, "Mizan Teferi": 4},
    "Tepi": {"Gore": 9, "Mizan Teferi": 4, "Bonga": 8},
    "Mizan Teferi": {"Tepi": 4, "Bonga": 4},
    "Buta Jira": {"Worabe": 2, "Batu": 2},
    "Batu": {"Buta Jira": 2, "Adama": 4, "Shashemene": 3},
    "Worabe": {"Buta Jira": 2, "Wolkite": 5, "Hossana": 2},
    "Shashemene": {"Batu": 3, "Hawassa": 1, "Dodolla": 3, "Hossana": 7},
    "Hossana": {"Worabe": 2, "Shashemene": 7, "Wolaita Sodo": 4},
    "Wolaita Sodo": {"Dawro": 6, "Hossana": 4, "Arba Minch": 5},
    "Dawro": {"Wolaita Sodo": 6, "Bonga": 10},
    "Arba Minch": {"Wolaita Sodo": 5, "Basketo": 10, "Konso": 4},
    "Basketo": {"Arba Minch": 10, "Bench Maji": 5},
    "Bench Maji": {"Basketo": 5, "Juba": 22},
    "Juba": {"Bench Maji": 22},
    "Hawassa": {"Shashemene": 1, "Dilla": 3},
    "Dilla": {"Hawassa": 3, "Bule Hora": 4},
    "Bule Hora": {"Dilla": 4, "Yabello": 3},
    "Yabello": {"Bule Hora": 3, "Konso": 3, "Moyale": 6},
    "Konso": {"Arba Minch": 4, "Yabello": 3},
    "Moyale": {"Yabello": 6, "Nairobi": 22},
    "Nairobi": {"Moyale": 22},
    "Assela": {"Adama": 4, "Assasa": 4},
    "Assasa": {"Assela": 4, "Dodolla": 1},
    "Dodolla": {"Assasa": 1, "Shashemene": 3, "Bale": 13},
    "Bale": {"Dodolla": 13, "Goba": 18, "Liben": 11, "Sof Oumer": 23},
    "Liben": {"Bale": 11},
    "Goba": {"Bale": 18, "Sof Oumer": 6, "Babille": 28},
    "Sof Oumer": {"Goba": 6, "Bale": 23, "Gode": 23},
    "Matahara": {"Adama": 3, "Awash": 1},
    "Awash": {"Matahara": 1, "Gabi Rasu": 5, "Chiro": 4},
    "Chiro": {"Awash": 4, "Dire Dawa": 8},
    "Dire Dawa": {"Chiro": 8, "Harar": 4},
    "Harar": {"Dire Dawa": 4, "Babille": 2},
    "Babille": {"Harar": 2, "Jigjiga": 3, "Goba": 28},
    "Jigjiga": {"Babille": 3, "Dega Habur": 5},
    "Dega Habur": {"Jigjiga": 5, "Kebri Dahar": 6},
    "Kebri Dahar": {"Dega Habur": 6, "Gode": 5, "Werder": 6},
    "Werder": {"Kebri Dahar": 6},
    "Gode": {"Kebri Dahar": 5, "Dollo": 17, "Mokadisho": 22, "Sof Oumer": 23},
    "Dollo": {"Gode": 17},
    "Mokadisho": {"Gode": 22},
}

# Uniform Cost Search and Customized UCS for visiting multiple goals.

import heapq
def uniform_cost_search(graph, start, goal):
    """
    Uniform Cost Search to find the shortest path from start to goal.
    """
    # Priority queue to store (cost, current_node, path)
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        # Goal check
        if current == goal:
            return cost, path

        # Expand neighbors
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return float('inf'), []  # If no path is found

def customized_ucs(graph, start, goals):
    """
    Customized UCS to visit all goal states starting from a given start node.
    """
    visited_goals = set()
    total_cost = 0
    current = start
    path = []

    while visited_goals != set(goals):
        # Find the closest unvisited goal
        min_cost = float('inf')
        best_path = []
        next_goal = None

        for goal in goals:
            if goal not in visited_goals:
                cost, temp_path = uniform_cost_search(graph, current, goal)
                if cost < min_cost:
                    min_cost = cost
                    best_path = temp_path
                    next_goal = goal

        # Update the total cost and path
        total_cost += min_cost
        path.extend(best_path[:-1])  # Avoid duplicating nodes in the path
        current = next_goal
        visited_goals.add(next_goal)

    path.append(current)  # Add the last goal
    return total_cost, path


# Task 2.2: Path from Addis Ababa to Lalibela
cost, path = uniform_cost_search(graph, "Addis Ababa", "Lalibela")
print(f"Shortest path from Addis Ababa to Lalibela: Cost = {cost}, Path = {path}")

# Task 2.3: Customized UCS for visiting multiple goals
goals = ["Axum", "Gondar", "Lalibela", "Babille", "Jimma", "Bale", "Sof Oumer", "Arba Minch"]
total_cost, full_path = customized_ucs(graph, "Addis Ababa", goals)
print(f"Path visiting all goals: Total Cost = {total_cost}, Path = {full_path}")
