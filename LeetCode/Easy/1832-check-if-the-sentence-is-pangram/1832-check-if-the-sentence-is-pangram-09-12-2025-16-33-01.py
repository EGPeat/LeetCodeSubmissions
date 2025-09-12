class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashset = set()
        for char in sentence:
            hashset.add(char.lower())
        if len(hashset) < 26:
            return False
        else:
            return True