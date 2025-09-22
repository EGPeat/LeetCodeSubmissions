class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self, ch):
        return ord(ch) - ord('a')

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            index = self.charToIndex(char)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEnd = True

    def search(self, word: str, node=None) -> bool:
        #print(word)
        if not node:
            node = self.root
        for i, char in enumerate(word):
            index = self.charToIndex(char)
            if index == -51:
                for next_char in node.children:
                    if next_char:
                        found = self.search(word[i+1:], node = next_char)
                        if found: 
                            return True
                return False
            #print(char, index, "\n",node.children)
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


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)