from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_counter = Counter(arr)
        hash_set_counter = set()
        for item in hash_counter:
            if hash_counter[item] in hash_set_counter:
                return False
            hash_set_counter.add(hash_counter[item])
        return True