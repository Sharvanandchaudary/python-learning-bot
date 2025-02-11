import random

# Dictionary of data structures with their descriptions, pseudocode, and simple implementation
data_structures = {
    "Stack": {
        "description": "A stack follows LIFO (Last In First Out) principle.",
        "pseudocode": """
Push(stack, element):
    add element to the top of the stack

Pop(stack):
    if stack is empty:
        return 'Stack is empty'
    return remove and return element from the top of the stack

Peek(stack):
    if stack is empty:
        return 'Stack is empty'
    return top element of the stack

IsEmpty(stack):
    return True if stack is empty, False otherwise
        """,
        "implementation": """
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
        """
    },
    "Queue": {
        "description": "A queue follows FIFO (First In First Out) principle.",
        "pseudocode": """
Enqueue(queue, element):
    add element to the end of the queue

Dequeue(queue):
    if queue is empty:
        return 'Queue is empty'
    return remove and return element from the front of the queue

Front(queue):
    if queue is empty:
        return 'Queue is empty'
    return front element of the queue

IsEmpty(queue):
    return True if queue is empty, False otherwise
        """,
        "implementation": """
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return 'Queue is empty'
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
        """
    },
    "Binary Tree": {
        "description": "A binary tree is a hierarchical data structure where each node has at most two children.",
        "pseudocode": """
Insert(tree, value):
    if tree is empty:
        create a new node with the value and make it the root
    else:
        recursively insert the value in the left or right subtree

InOrderTraversal(tree):
    if tree is not empty:
        traverse the left subtree
        visit the current node
        traverse the right subtree

PreOrderTraversal(tree):
    if tree is not empty:
        visit the current node
        traverse the left subtree
        traverse the right subtree

PostOrderTraversal(tree):
    if tree is not empty:
        traverse the left subtree
        traverse the right subtree
        visit the current node
        """,
        "implementation": """
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left:
                self._insert_recursive(current_node.left, value)
            else:
                current_node.left = Node(value)
        else:
            if current_node.right:
                self._insert_recursive(current_node.right, value)
            else:
                current_node.right = Node(value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")
        """
    },
    "Linked List": {
        "description": "A linked list is a linear data structure where each element (node) points to the next.",
        "pseudocode": """
InsertAtHead(list, element):
    create a new node with the element and set it as the head

InsertAtTail(list, element):
    traverse the list and insert the node at the end

DeleteNode(list, element):
    traverse the list and delete the node that contains the element

Traverse(list):
    visit each node starting from the head
        """,
        "implementation": """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        """
    },
    "Hash Table": {
        "description": "A hash table is a data structure that maps keys to values for efficient lookup.",
        "pseudocode": """
Insert(table, key, value):
    hash_index = hash(key)
    insert key-value pair at hash_index

Get(table, key):
    hash_index = hash(key)
    return the value at hash_index

Delete(table, key):
    hash_index = hash(key)
    delete the key-value pair at hash_index
        """,
        "implementation": """
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        return None
        """
    }
}

# Function to get a random data structure with its description, pseudocode, and implementation
import random

def get_data_structure():
    if not data_structures:  # Check if dictionary is empty
        return {"error": "No data structures available"}
    
    ds_name = random.choice(list(data_structures.keys()))
    ds_data = data_structures.get(ds_name, {})

    return {
        "name": ds_name,
        "description": ds_data.get("description", "No description available"),
        "pseudocode": ds_data.get("pseudocode", "No pseudocode available"),
        "implementation": ds_data.get("implementation", "No implementation available"),
    }


# Example usage
if __name__ == "__main__":
    data_structure, description, pseudocode, implementation = get_data_structure()
    
    print(f"Data Structure of the Day: {data_structure}")
    print(f"Description: {description}")
    print(f"Pseudocode: {pseudocode}")
    print(f"Implementation: {implementation}")
