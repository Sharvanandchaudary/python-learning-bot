import random

# Dictionary of algorithms with their descriptions and pseudocode
algorithms = {
    "Binary Search": {
        "description": "Binary search is an efficient algorithm for finding an item from a sorted list of items.",
        "pseudocode": """
BinarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  # Target not found
        """
    },
    "Quick Sort": {
        "description": "QuickSort is a divide-and-conquer algorithm that sorts an array by partitioning it.",
        "pseudocode": """
QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return QuickSort(left) + [pivot] + QuickSort(right)
        """
    },
    "Merge Sort": {
        "description": "MergeSort is a divide-and-conquer algorithm that splits an array into halves, sorts them, and then merges them.",
        "pseudocode": """
MergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    return merge(left, right)

merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result
        """
    },
    "Dijkstra's Algorithm": {
        "description": "Dijkstra’s algorithm finds the shortest path in a weighted graph.",
        "pseudocode": """
Dijkstra(graph, start):
    initialize distance[start] = 0 and distance[all other nodes] = infinity
    create a priority queue Q
    
    while Q is not empty:
        current_node = Q.pop()
        
        for neighbor, weight in graph[current_node]:
            distance_via_current = distance[current_node] + weight
            if distance_via_current < distance[neighbor]:
                distance[neighbor] = distance_via_current
                Q.push(neighbor)
    
    return distance  # Shortest distances from start node
        """
    },
    "Breadth-First Search (BFS)": {
        "description": "BFS is an algorithm for traversing or searching tree or graph data structures. It starts at the root and explores neighbors level by level.",
        "pseudocode": """
BFS(graph, start):
    create a queue Q
    enqueue(start) into Q
    create a visited set
    
    while Q is not empty:
        current_node = dequeue from Q
        if current_node not in visited:
            visit(current_node)
            visited.add(current_node)
            for neighbor in graph[current_node]:
                enqueue(neighbor) into Q
        """
    },
    "Depth-First Search (DFS)": {
        "description": "DFS is an algorithm for traversing or searching tree or graph data structures. It explores as far as possible along each branch before backtracking.",
        "pseudocode": """
DFS(graph, node, visited):
    if node not in visited:
        visit(node)
        visited.add(node)
        for neighbor in graph[node]:
            DFS(graph, neighbor, visited)
        """
    },
    "Fibonacci Sequence (Dynamic Programming)": {
        "description": "The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. This dynamic programming solution avoids recalculating the same value multiple times.",
        "pseudocode": """
Fibonacci(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for i in range(2, n+1):
        next_fib = prev + curr
        prev = curr
        curr = next_fib
    return curr
        """
    },
    "Knapsack Problem (Dynamic Programming)": {
        "description": "The 0/1 Knapsack problem is a problem in combinatorial optimization where the goal is to determine the most valuable set of items to include in a knapsack without exceeding a weight limit.",
        "pseudocode": """
Knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]
        """
    },
    "Bubble Sort": {
        "description": "Bubble Sort is a simple sorting algorithm where each pair of adjacent elements is compared and swapped if they are in the wrong order.",
        "pseudocode": """
BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
        """
    },
    "Insertion Sort": {
        "description": "Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time.",
        "pseudocode": """
InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
        """
    },
    "Selection Sort": {
        "description": "Selection Sort is a sorting algorithm that repeatedly selects the smallest (or largest) element from an unsorted part of the list and moves it to the sorted part.",
        "pseudocode": """
SelectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
        """
    },
}

# Function to get a random algorithm with its description and pseudocode
def get_algorithm():
    algorithm_name = random.choice(list(algorithms.keys()))
    algorithm_data = algorithms[algorithm_name]
    
    return {
        "name": algorithm_name,
        "description": algorithm_data["description"],
        "pseudocode": algorithm_data["pseudocode"]
    }

# Example usage
# Example usage
if __name__ == "__main__":
    algorithm, description, pseudocode = get_algorithm()
    print(f"Algorithm: {algorithm}")
    print(f"Description: {description}")
    print(f"Pseudocode: {pseudocode}")
