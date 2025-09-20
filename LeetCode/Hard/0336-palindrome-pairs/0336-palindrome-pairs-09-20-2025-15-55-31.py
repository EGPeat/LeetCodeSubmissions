class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_to_index = {word: index for index, word in enumerate(words)}
        result = []
      
        for current_index, current_word in enumerate(words):
            for split_pos in range(len(current_word) + 1):
                prefix = current_word[:split_pos]
                suffix = current_word[split_pos:]
              
                reversed_prefix = prefix[::-1]
                reversed_suffix = suffix[::-1]
              
                if reversed_prefix in word_to_index and word_to_index[reversed_prefix] != current_index and suffix == reversed_suffix:
                    result.append([current_index, word_to_index[reversed_prefix]])
                if split_pos > 0 and reversed_suffix in word_to_index and word_to_index[reversed_suffix] != current_index and prefix == reversed_prefix:
                    result.append([word_to_index[reversed_suffix], current_index])
      
        return result
