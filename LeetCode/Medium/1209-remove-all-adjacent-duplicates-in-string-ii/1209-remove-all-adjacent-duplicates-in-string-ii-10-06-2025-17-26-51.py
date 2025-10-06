class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        current_index = 0
        string_length = len(s)
      
        while current_index < string_length:
            next_index = current_index
            while next_index < string_length and s[next_index] == s[current_index]:
                next_index += 1
            consecutive_count = next_index - current_index
            remaining_count = consecutive_count % k
            if stack and stack[-1][0] == s[current_index]:
                stack[-1][1] = (stack[-1][1] + remaining_count) % k
                if stack[-1][1] == 0:
                    stack.pop()
            elif remaining_count > 0:
                stack.append([s[current_index], remaining_count])
            current_index = next_index
        result_parts = [character * count for character, count in stack]
        return "".join(result_parts)