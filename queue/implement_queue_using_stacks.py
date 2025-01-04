# https://leetcode.com/problems/implement-queue-using-stacks/description/
# Similar problems
# https://leetcode.com/problems/implement-stack-using-queues/

class MyQueue:

    def __init__(self):
        self.rear = []
        self.front = []

    def push(self, x: int) -> None:
        self.rear.append(x)

    def pop(self) -> int:

        if self.empty():
            return None

        while self.rear:
            x = self.rear.pop()
            self.front.append(x)

        output = self.front.pop()

        while self.front:
            x = self.front.pop()
            self.rear.append(x)

        return output

    def peek(self) -> int:

        if self.empty():
            return None

        while self.rear:
            x = self.rear.pop()
            self.front.append(x)

        output = self.front[-1]

        while self.front:
            x = self.front.pop()
            self.rear.append(x)

        return output

    def empty(self) -> bool:

        return not self.rear

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()