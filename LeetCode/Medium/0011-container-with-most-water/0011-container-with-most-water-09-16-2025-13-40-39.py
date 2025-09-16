class Solution:
    def maxArea(self, height):
        st, ed = 0, len(height) - 1
        maxArea = min(height[st], height[ed]) * (ed - st)
        curr_area = 0
        while st < ed:  # -1:
            w = ed - st
            h = min(height[st], height[ed])
            curr_area = w * h
            if height[st] > height[ed]:
                ed -= 1
            else:
                st += 1
            maxArea = max(maxArea, curr_area)
        return maxArea
