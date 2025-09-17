class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_arr = [1] * (n+1)
        right_arr = [1] * (n+1)

        for i in range(1, n+1):
            left_arr[i] = left_arr[i-1] * nums[i-1]
            right_arr[n-i-1] = right_arr[n-i]
            right_arr[n-i-1] = right_arr[n-i] * nums[n-i]
        #print(nums)
        #print(left_arr)
        #print(right_arr)
        out = [0] * n
        for i in range(n):
            out[i] = left_arr[i] * right_arr[i]
        #print(out)
        return out