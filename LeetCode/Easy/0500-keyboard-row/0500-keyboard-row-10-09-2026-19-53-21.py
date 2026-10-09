class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        tr=set("qwertyuiop")
        mr=set("asdfghjkl")
        br=set("zxcvbnm")
        out_words = []

        for word in words:
            for row in [tr, mr, br]:
                bad = False
                for char in word:
                    if char.lower() not in row:
                        bad = True
                        break
                if not bad:
                    out_words.append(word)
        return out_words