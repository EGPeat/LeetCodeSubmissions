class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        memo = [False] * (len(s)+1)
        memo[0] = True
        for word in wordDict:
            trie.insert(word)
        for i in range(1, len(s)+1):
            for j in range(i):
                if memo[j] and s[j:i] in wordset:
                    memo[i] =True
                    break
        return memo[len(s)]
