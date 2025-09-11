class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = defaultdict(int)
        ransom = defaultdict(int)
        for letter in ransomNote:
            ransom[letter] += 1

        for idx in range(len(magazine)):
            freq[magazine[idx]] += 1
        for key in (list(freq.keys())+ list(ransom.keys())):
            if freq[key] < ransom[key]:
                return False
        return True