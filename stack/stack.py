from typing import Any


class Stack:
    def __init__(self):
        self.items = []

    def push(self, val: Any):
        self.items.append(val)

    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())