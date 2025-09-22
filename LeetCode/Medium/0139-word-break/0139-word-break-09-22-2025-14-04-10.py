class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = self.charToIndex(char)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = self.charToIndex(char)
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = self.charToIndex(char)
            if not node.children[index]:
                return False
            node = node.children[index]
        return True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        memo = [False] * (len(s)+1)
        memo[0] = True
        for word in wordDict:
            trie.insert(word)
        for i in range(1, len(s)+1):
            for j in range(i):
                if memo[j] and trie.search(s[j:i]):
                    memo[i] =True
        return memo[len(s)]
