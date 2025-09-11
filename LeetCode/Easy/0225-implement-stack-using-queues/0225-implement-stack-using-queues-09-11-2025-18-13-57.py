class MyStack:

    def __init__(self):
        self.forward_queue = deque()
        self.backward_queue = deque()

    def push(self, x: int) -> None:
        self.backward_queue.append(x)
        while self.forward_queue:
            self.backward_queue.append(self.forward_queue.popleft())
        self.forward_queue, self.backward_queue = self.backward_queue, self.forward_queue


    def pop(self) -> int:
        top_elem = self.forward_queue.popleft()
        return top_elem

    def top(self) -> int:
        top_elem = self.forward_queue[0]
        return top_elem


    def empty(self) -> bool:
        if not self.forward_queue and not self.backward_queue:
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()