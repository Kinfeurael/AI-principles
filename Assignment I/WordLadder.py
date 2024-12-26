from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    # If endWord is not in wordList, there is no solution
    if endWord not in wordList:
        return 0

    # Create a dictionary for all possible intermediate states
    wordList = set(wordList)  # Convert to set for O(1) lookups
    word_length = len(beginWord)
    all_combo_dict = defaultdict(list)
    
    for word in wordList:
        for i in range(word_length):
            intermediate_word = word[:i] + "*" + word[i+1:]
            all_combo_dict[intermediate_word].append(word)

    # Perform BFS
    queue = deque([(beginWord, 1)])  # (current_word, level)
    visited = set([beginWord])

    while queue:
        current_word, level = queue.popleft()

        for i in range(word_length):
            # Generate intermediate words
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            
            for neighbor in all_combo_dict[intermediate_word]:
                # If we find the endWord, return the level + 1
                if neighbor == endWord:
                    return level + 1
                
                # Otherwise, add it to the queue if not visited
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
            
            # Clear the intermediate state to save memory
            all_combo_dict[intermediate_word] = []

    return 0  # If no path is found
