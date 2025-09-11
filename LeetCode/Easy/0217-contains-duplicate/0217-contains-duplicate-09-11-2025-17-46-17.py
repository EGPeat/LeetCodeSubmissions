class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      hash_map = {}
      for item in nums:
        val = hash_map.get(item, 0)
        hash_map[item] = val + 1
        if val + 1 >= 2:
          return True
      return False
