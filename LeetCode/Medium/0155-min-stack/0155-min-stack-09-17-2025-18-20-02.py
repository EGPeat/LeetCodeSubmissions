class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.currmin = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.currmin = min(self.currmin, val)
        self.minstack.append(self.currmin)

    def pop(self) -> None:
        tmp = self.stack.pop()
        tmp2 = self.minstack.pop()
        if self.minstack and tmp2 < self.minstack[-1]:
            self.currmin = self.minstack[-1]
        if not self.minstack:
            self.currmin = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currmin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()