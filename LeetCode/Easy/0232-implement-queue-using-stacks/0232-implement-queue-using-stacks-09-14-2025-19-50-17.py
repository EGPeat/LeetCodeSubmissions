class MyQueue:
    def __init__(self):
        self.forward_stack = []
        self.backward_stack = []

    def push(self, x: int) -> None:
        self.forward_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.backward_stack.pop()
        

    def peek(self) -> int:
        if not self.backward_stack:
            self.backward_stack = self.forward_stack[::-1]
            self.forward_stack = []
        return self.backward_stack[-1]

    def empty(self) -> bool:
        if not self.backward_stack and not self.forward_stack:
            return True
        else:
            return False




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()