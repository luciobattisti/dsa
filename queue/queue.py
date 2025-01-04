from typing import Optional, Any


class Node:
    def __init__(self, val: Any):
        self.val = val
        self.next: Optional[Node] = None


class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def is_empty(self):
        return not self.front

    def enqueue(self, val: Any):
        new_node = Node(val)

        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            return None

        curr_front = self.front
        self.front = self.front.next
        curr_front.next = None

        if self.is_empty():
            self.rear = None

        self.size -= 1
        return curr_front.val

    def traverse(self):
        node = self.front
        print("[", end="")
        while node:
            print(node.val, end=",")
            node = node.next
        print("]")


if __name__ == "__main__":
    queue = Queue()

    print("Test enqueue")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.traverse()

    print("Test dequeue")
    print("Removed:", queue.dequeue())
    queue.traverse()
    print("Removed:", queue.dequeue())
    queue.traverse()
    print("Removed:", queue.dequeue())
    queue.traverse()
    print("Removed: ", queue.dequeue())










