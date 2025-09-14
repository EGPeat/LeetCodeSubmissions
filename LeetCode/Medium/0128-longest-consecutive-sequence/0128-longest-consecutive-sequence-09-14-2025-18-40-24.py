class Solution:
    def longestConsecutive(self, nums):
        longest_sequence = 0
        hashset = dict()
        for i, num in enumerate(nums):
            hashset[num] = i
        for key in hashset.keys():
            length = 1
            longest_sequence = max(longest_sequence, length)
            if key - 1 not in hashset.keys():
                i = 1
                while i < len(nums):
                    if key + i in hashset.keys():
                        i += 1
                        length += 1
                        longest_sequence = max(longest_sequence, length)
                    else:
                        break
        return longest_sequence
