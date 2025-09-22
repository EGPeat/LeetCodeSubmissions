class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqDict = {}
        for char in nums: 
            if char in freqDict:
                freqDict[char] += 1
            else:
                freqDict[char] = 1

        max_freq = 0
        sum_val = 0
        for key, value in freqDict.items():
            if value > max_freq:
                max_freq = value
                sum_val = value
            elif value == max_freq:
                sum_val += value
        return sum_val