class Solution:
    def check_difference(self, w1, w2):
        diff = 0
        for char1, char2 in zip(w1, w2):
            if char1 != char2:
                diff += 1
            if diff > 1:
                return False
        return True
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        word_dict = defaultdict(list)
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if self.check_difference(wordList[i], wordList[j]):
                    word_dict[wordList[i]].append(wordList[j])
                    word_dict[wordList[j]].append(wordList[i])

        #print(word_dict)
        visited = set(beginWord)
        queue = deque([(beginWord, 1)])
        while queue:
            #print(queue)
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for neighbor in word_dict[word]:
                if neighbor not in visited:
                    queue.append((neighbor, dist + 1))
                    visited.add(neighbor)
        return 0
