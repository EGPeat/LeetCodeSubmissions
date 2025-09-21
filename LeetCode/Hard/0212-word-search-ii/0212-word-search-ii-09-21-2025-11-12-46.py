class TrieNode:
    def __init__(self):
        self.children: List[Optional['TrieNode']] = [None] * 26
        self.word_index: int = -1

    def insert(self, word: str, index: int) -> None:
        current_node = self
        for char in word:
            char_index = ord(char) - ord('a')
            if current_node.children[char_index] is None:
                current_node.children[char_index] = TrieNode()
            current_node = current_node.children[char_index]
        current_node.word_index = index


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node: TrieNode, row: int, col: int) -> None:
            char_index = ord(board[row][col]) - ord('a')
          
            if node.children[char_index] is None:
                return
          
            node = node.children[char_index]
          
            if node.word_index >= 0:
                result.append(words[node.word_index])
                node.word_index = -1
          
            original_char = board[row][col]
            board[row][col] = '#'
          
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for delta_row, delta_col in directions:
                new_row, new_col = row + delta_row, col + delta_col
                if (0 <= new_row < rows and 
                    0 <= new_col < cols and 
                    board[new_row][new_col] != '#'):
                    dfs(node, new_row, new_col)
          
            board[row][col] = original_char
        trie_root = TrieNode()
        for index, word in enumerate(words):
            trie_root.insert(word, index)
      
        rows, cols = len(board), len(board[0])
        result = []
      
        for row in range(rows):
            for col in range(cols):
                dfs(trie_root, row, col)
      
        return result