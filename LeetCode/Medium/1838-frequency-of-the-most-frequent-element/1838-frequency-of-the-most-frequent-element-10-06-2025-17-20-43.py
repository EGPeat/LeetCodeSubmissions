class Solution:
    def maxFrequency(self, elements: List[int], k: int) -> int:
        import bisect
        from collections import defaultdict
        if min(elements) == max(elements):
            return len(elements)
        number_freq = defaultdict(int)
        
        for n in elements:
            number_freq[n] += 1
        sorted_keys = list(number_freq.keys())
        sorted_keys.sort(reverse=True)
        best_count = 0

        for i in range(len(sorted_keys)):
            temp_ops = k
            goal = sorted_keys[i]
            temp_count = number_freq[goal]
            for z in range(i + 1, len(sorted_keys)):
                second_goal = sorted_keys[z]
                for _ in range(number_freq[second_goal]):
                    if temp_ops <= 0:
                        break
                    else:
                        if temp_ops - (goal - second_goal) < 0:
                            break
                        else:
                            temp_ops -= (goal - second_goal)
                            temp_count += 1
            if temp_count > best_count:
                    best_count = temp_count
            

        return best_count