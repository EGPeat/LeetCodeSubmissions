class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx in range(len(temperatures) - 1, -1, -1):
            if stack:
                while stack and temperatures[idx] >= stack[-1][0]:
                    stack.pop()
                if stack:
                    res[idx] = stack[-1][1] - idx
                stack.append((temperatures[idx], idx))

            stack.append((temperatures[idx], idx))
        return res
