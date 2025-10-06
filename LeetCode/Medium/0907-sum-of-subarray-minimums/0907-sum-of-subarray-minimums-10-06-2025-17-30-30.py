class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left_boundaries = [-1] * n
        right_boundaries = [n] * n
        stack = []
        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:
                stack.pop()
            if stack:
                left_boundaries[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right_boundaries[i] = stack[-1]
            stack.append(i)

        MOD = 10**9 + 7
        total_sum = sum((i - left_boundaries[i]) * (right_boundaries[i] - i) * value for i, value in enumerate(arr)) % MOD
      
        return total_sum