def has_cycle(graph):
    # Helper function for DFS
    def dfs(node):
        # Mark the current node as visited and add it to the recursion stack
        visited[node] = True
        rec_stack[node] = True
        
        # Visit all neighbors of the current node
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:  # If the neighbor hasn't been visited, recurse
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:  # If the neighbor is in the recursion stack, a cycle is found
                return True
        
        # Remove the current node from the recursion stack
        rec_stack[node] = False
        return False

    # Initialize visited and recursion stack dictionaries
    visited = {node: False for node in graph}
    rec_stack = {node: False for node in graph}

    # Perform DFS for each node
    for node in graph:
        if not visited[node]:  # If the node hasn't been visited, start DFS from it
            if dfs(node):
                return True

    return False