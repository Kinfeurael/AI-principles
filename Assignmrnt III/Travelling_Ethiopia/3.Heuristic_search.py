''' Task 3: Implement A* search algorithm to find the shortest path from 
    Addis Ababa to Moyale using the given state space graph and heuristic.'''

import heapq

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
    "Wolaita Sodo": {"Dawro": 6, "Hossana": 4, "Arba Minch": 4},
    "Dawro": {"Wolaita Sodo": 6, "Bonga": 10},
    "Arba Minch": {"Wolaita Sodo": 4, "Basketo": 10, "Konso": 4},
    "Basketo": {"Arba Minch": 10, "Bench Maji": 5},
    "Bench Maji": {"Basketo": 5, "Juba": 22},
    "Juba": {"Bench Maji": 22},
    "Hawassa": {"Shashemene": 1, "Dilla": 3},
    "Dilla": {"Hawassa": 3, "Bule Hora": 4},
    "Bule Hora": {"Dilla": 4, "Yabello": 2},
    "Yabello": {"Bule Hora": 2, "Konso": 3, "Moyale": 6},
    "Konso": {"Arba Minch": 4, "Yabello": 3},
    "Nairobi": {"Moyale": 22},
    "Assela": {"Adama": 4, "Assasa": 4},
    "Assasa": {"Assela": 4, "Dodolla": 1},
    "Dodolla": {"Assasa": 1, "Shashemene": 3, "Robe": 13},
    "Robe": {"Dodolla": 13, "Goba": 18, "Liben": 11, "Sof Oumer": 23},
    "Liben": {"Robe": 11, "Moyale": 11},
    "Goba": {"Robe": 18, "Sof Oumer": 6, "Babille": 28},
    "Sof Oumer": {"Goba": 6, "Robe": 23, "Gode": 23},
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
    "Dollo": {"Gode": 17, "Moyale": 18},
    "Mokadisho": {"Gode": 22 , "Moyale": 40},
    "Moyale": {"Yabello": 6, "Nairobi": 22, "Dollo": 18, "Mokadisho": 40, "Liben": 11},

}

heuristic = {
    "Asmara": 68,
    "Axum": 66,
    "Adigrat": 62,
    "Adwa": 65,
    "Mekelle": 58,
    "Sekota": 59,
    "Lalibela": 57,
    "Alamata": 53,
    "Woldia": 50,
    "Dessie": 44,
    "Kemise": 40,
    "Debre Sina": 33,
    "Debre Birhan": 31,
    "Samara": 42,
    "Fanti Rasu": 49,
    "Gabi Rasu": 32,
    "Killbet Rasu": 55,
    "Shire": 67,
    "Humera": 65,
    "Debark": 60,
    "Gondar": 56,
    "Metema": 62,
    "Azezo": 55,
    "Khartoum": 81,
    "Bahir Dar": 48,
    "Debre Tabor": 52,
    "Debre Markos": 39,
    "Finote Selam": 42,
    "Injibara": 44,
    "Metekel": 59,
    "Addis Ababa": 26,
    "Adama": 23,
    "Ambo": 31,
    "Nekemte": 39,
    "Gimbi": 43,
    "Bedelle": 40,
    "Gore": 46,
    "Dembi Dolo": 49,
    "Assosa": 51,
    "Gambela": 51,
    "Wolkite": 25,
    "Jimma": 33,
    "Bonga": 33,
    "Tepi": 41,
    "Mizan Teferi": 37,
    "Buta Jira": 21,
    "Batu": 19,
    "Worabe": 22,
    "Shashemene": 16,
    "Hossana": 21,
    "Wolaita Sodo": 17,
    "Dawro": 23,
    "Arba Minch": 13,
    "Basketo": 23,
    "Bench Maji": 28,
    "Juba": 50,
    "Hawassa": 15,
    "Dilla": 12,
    "Bule Hora": 8,
    "Yabello": 6,
    "Konso": 9,
    "Nairobi": 22,
    "Assela": 22,
    "Assasa": 18,
    "Dodolla": 19,
    "Robe": 22,
    "Liben": 11,
    "Goba": 40,
    "Sof Oumer": 45,
    "Matahara": 26,
    "Awash": 27,
    "Chiro": 31,
    "Dire Dawa": 31,
    "Harar": 35,
    "Babille": 37,
    "Jigjiga": 40,
    "Dega Habur": 45,
    "Kebri Dahar": 40,
    "Werder": 46,
    "Gode": 35,
    "Dollo": 18,
    "Mokadisho": 40,
    "Moyale": 0
}

class AStarSearch:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def a_star(self, start, goal):
        open_set = []  # Priority queue
        heapq.heappush(open_set, (0 + self.heuristic[start], 0, start, []))
        closed_set = set()

        while open_set:
            _, cost, current, path = heapq.heappop(open_set)

            if current in closed_set:
                continue
            
            path = path + [current]
            if current == goal:
                return path, cost
            
            closed_set.add(current)
            
            for neighbor, weight in self.graph[current].items():
                if neighbor not in closed_set:
                    new_cost = cost + weight
                    priority = new_cost + self.heuristic[neighbor]
                    heapq.heappush(open_set, (priority, new_cost, neighbor, path))
        
        return None, float("inf")  # No path found

astar = AStarSearch(graph, heuristic)
path, cost = astar.a_star("Addis Ababa", "Moyale")
print("Path:", path)
print("Cost:", cost)

