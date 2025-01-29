# Traveling Ethiopia Search Problem

## Overview
This repository contains implementations of various search algorithms to solve the Traveling Ethiopia Search Problem based on different state-space graphs.

## Problem Descriptions
The problem involves finding paths between cities in Ethiopia using different search strategies based on given graphs:

1. **State Space Graph Representation:**
   - Conversion of a state-space graph into a manageable data structure (stack/queue).
   - Implementation of search strategies: Breadth-First Search (BFS) and Depth-First Search (DFS).

2. **State Space Graph with Backward Cost:**
   - Conversion of the graph into a data structure.
   - Implementation of Uniform Cost Search (UCS) to find a path from "Addis Ababa" to "Lalibela".
   - A customized UCS algorithm to visit multiple goal states while preserving local optimum.

3. **State Space Graph with Heuristic and Backward Cost:**
   - Implementation of A* Search to find an optimal path from "Addis Ababa" to "Moyale".

4. **Adversarial Search in the Traveling Ethiopia Search Problem:**
   - Implementation of the MiniMax search algorithm to find the best destination based on coffee quality.

## Implementation Details
Each solution is implemented in Python with the following structure:

- `1.BFS_DFS.py`: Implements BFS and DFS search strategies.
- `2.UCS.py`: Implements Uniform Cost Search.
- `3.Heuristic_search.py`: Implements A* Search.
- `4.Adversial_search.py`: Implements the MiniMax search algorithm.

## Requirements
Ensure you have Python installed. No additional dependencies are required.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/kinfeurael/.git
   cd ethiopia-search ```
2. Run the desired Script
