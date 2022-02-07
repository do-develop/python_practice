"""
Logarithm time complexity can be represented in Big O notation, O(log n)

When an algorithm has O(log n) running time, it means that as the input size
grows the number of operations grows very slowly.
"""
# Logarithmic algorithm - Binary search
def binary_search_recursive(arr, low, high, target):
    # base case
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)
        else:
            return binary_search_recursive(arr, mid + 1, high, target)

    else:
        return -1


def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1
            

# TEST
arr = [2, 3, 4, 10, 30]
target = 10
print(binary_search_recursive(arr, 0, len(arr)-1, target))
print(binary_search_iterative(arr, target))

"""
Graph Traversal
BFS uses FIFO storage such as queue
- finding the shortest path between two nodes

DFS uses LIFO storage such as stack
when needs to consider every possibility because of its nature of going in depth
-

Tree is a undirected graph, hierarchical structure
,top most node is known as a root node,
Used in many search applications where data is constantly entering/leaving
A tree is an undirected graph in which any two vertices are connected by
exactly one path. In other words, any acyclic connected graph is a tree. 
"""
from collections import deque
"""
def BFS(graph, root):
    visited = list()  # stores visted nodes
    queue = deque()  # stores nodes to be visited
    queue.append(root)
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])  # append the adjacent node to that vistited node
    return visited

def DFS(graph, root):
    visited = list()
    stack = list()
    stack.append(root)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited
"""
def BFS(graph, root):
    visited = set()
    queue = deque([root])
    visited.add(root)
    
    while queue:
        node = queue.popleft()
        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)


def DFS(graph, root):
    visited = set()
    stack = [root]
    visited.add(root)

    while stack:
        node = stack.pop()
        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                stack.append(neigh)


# DFS recursive version
def dfs(graph, first, path = []):
    path += [first]

    for neigh in graph[first]:
        if neigh not in path:
            path = dfs(graph, neigh, path)
    return path


if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(BFS(graph, 'A'))
    print(DFS(graph, 'A')) 


"""
Sliding window technique
This technique shows how a nested for loop in some problems can be converted to
a single for loop to reduce the time complexity.
As its name suggests, this technique involves taking a subset of data from a
given array or string, expanding or shrinking that subset to satisfy certain
conditions, hence the sliding effect.
"""
def maxSum(arr, subarr_size):
    arr_size = len(arr)

    if arr_size < subarr_size:
        return -1  # invalid case

    window_sum = sum(arr[:subarr_size])
    max_sum = window_sum

    # compute the sums of remaining windows by removing first eleme
    # of preivous window and adding last element of the current window
    for i in range(arr_size - subarr_size):
        window_sum = window_sum - arr[i] + arr[i + subarr_size]
        max_sum = max(window_sum, max_sum)
    return max_sum

# Driver Code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))


"""
Recursion
n-th Fibonacci number
"""

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))

print(Fibonacci(10))

# DP version
def fibonacci(n):
    prv, cur = 0, 1
    if n < 0:
        return
    if n <= 1:
        return n
    else:
        for i in range(2, n + 1):
            nxt = prv + cur
            prv, cur = cur, nxt
        return cur

"""
Inverting binary tree
"""
# Recursive version
def invertTree(self, root):
    if not root:
        return
    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root

# Iterative version
def invertTree(self, root):
    if not root:
        return
    stack = [root]

    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root
"""
Reversed linked list
"""
"""
def reverseList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
"""
"""
Heaps
Heap is a special case of balanced binary tree data structure where the
root-node key is compared with its children and arranged accordingly.
Used in implementing efficient priority-queues, which in turn are used
for scheduling processes in many operating systems
"""

"""
Dynamic Programming
Dynamic Programming is mainly an optimization over plain recursion. Wherever
we see a recursive solution that has repeated calls for same inputs, we can
optimize it using Dynamic Programming. The idea is to simply store the results
of subproblems, so that we do not have to re-compute them when needed later.
This simple optimization reduces time complexities from exponential to
polynomial. 
"""

"""
Quick sort & Merge sort

Stability in Sorting Algorithms
The stability of a sorting algorithm is concerned with how the algorithm treats
equal (or repeated) elements. Stable sorting algorithms preserve the relative
order of equal elements, while unstable sorting algorithms don't.

"""
"""
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
            
"""

def bubble_sort(arr):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

print(bubble_sort([1,6,9,2,3,7,9,0,3,5,6,7,8,7,5,2,1]))
                

def insertion_sort(arr):
    for i in range(1, len(arr)):
        value_to_sort = arr[i]

        while arr[i-1] > value_to_sort and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1

    return arr

print(insertion_sort([1,6,9,2,3,7,9,0,3,5,6,7,8,7,5,2,1]))

    
def selection_sort(arr):
    for i in range(0, len(arr)-1): # last item left is the highest value
        min_val = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_val]:
                min_val = j

        if min_val != i:
            arr[min_val], arr[i] = arr[i], arr[min_val]
    return arr
        
print(selection_sort([1,6,9,2,3,7,9,0,3,5,6,7,8,7,5,2,1]))

def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low+high)//2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1

            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)


unsorted = [1,6,9,2,3,7,9,0,3,5,6,7,8,7,5,2,1]
quick_sort(unsorted)
print(unsorted)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i1, i2, idx = 0, 0, 0

        while i1 < len(left) and i2 < len(right):
            if left[i1] <= right[i2]:
                arr[idx] = left[i1]
                i1 += 1
            else:
                arr[idx] = right[i2]
                i2 += 1
            idx += 1

        while i1 < len(left):
            arr[idx] = left[i1]
            i1 += 1
            idx += 1

        while i2 < len(right):
            arr[idx] = right[i2]
            i2 += 1
            idx += 1

unsorted_arr = [1,6,9,2,3,7,9,0,3,5,6,7,8,7,5,2,1]
merge_sort(unsorted_arr)
print(unsorted_arr)    
            

        
