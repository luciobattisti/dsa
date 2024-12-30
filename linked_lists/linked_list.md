A **linked list** is a linear data structure made up of nodes, where each node contains two parts: 

1. **Data**: The actual value or information.
2. **Pointer/Link**: A reference to the next node in the sequence (or `None` if it's the last node).

### Key Features:
- **Dynamic Size**: Unlike arrays, linked lists can easily grow or shrink in size by allocating or deallocating memory for nodes.
- **Non-contiguous Memory**: Nodes are stored in different memory locations and are connected via pointers, making it flexible but less cache-friendly compared to arrays.
- **Insertion/Deletion**: Adding or removing elements is efficient, especially at the beginning or middle, as it only requires updating pointers.

### Types of Linked Lists:
1. **Singly Linked List**: Each node points to the next node, and the last node points to `None`.
   - Example: `1 -> 2 -> 3 -> None`
2. **Doubly Linked List**: Each node has two pointers—one to the next node and another to the previous node.
   - Example: `None <- 1 <-> 2 <-> 3 -> None`
3. **Circular Linked List**: The last node points back to the first node, forming a circle.

### Example in Python:

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Create a simple linked list: 1 -> 2 -> 3 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Traversing the linked list
current = head
while current:
    print(current.value, end=" -> ")
    current = current.next
# Output: 1 -> 2 -> 3 ->
```

Linked lists are commonly used in scenarios where dynamic data management is required, such as implementing stacks, queues, or adjacency lists in graph representations.