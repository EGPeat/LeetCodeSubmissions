class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letters_used = [0] * 26
        output = []
        present = set()
        for c in s:
            letters_used[ord(c) - ord('a')] += 1
        for c in s:
            if (c not in present) and output:
                present.add(c)
                letters_used[ord(c) - ord('a')] -= 1
                top = output[-1]
                while letters_used[ord(output[-1]) - ord('a')] > 0 and c < output[-1]:
                    top2 = output.pop()
                    present.remove(top2)
                    if len(output) == 0:
                        break
                output.append(c)

            elif c not in present:
                present.add(c)
                letters_used[ord(c) - ord('a')] -= 1
                output.append(c)
            else:
                letters_used[ord(c) - ord('a')] -= 1
        new_output = "".join(output)





        return new_output
