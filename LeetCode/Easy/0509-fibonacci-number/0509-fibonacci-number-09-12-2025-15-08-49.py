class Solution:
    def __init__(self):
        self.memo = [0, 1]
        pass

    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        self.fibonaccihelper(n)
        return self.memo[n]

    def fibonaccihelper(self, n):
        if n < 2:
            return self.memo[n]
        if len(self.memo) > n:
            return self.memo[n]
        
        first_num = self.fibonaccihelper(n-2)
        second_num = self.fibonaccihelper(n-1)
        self.memo.append(first_num+second_num)
        return self.memo[n]
        