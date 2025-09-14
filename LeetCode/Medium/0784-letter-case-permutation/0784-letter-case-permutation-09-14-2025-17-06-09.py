
from string import ascii_letters


class Solution:
    def letterCasePermutation(self, string):
        subsets = []
        second_subset = []
        for letter in string:
            if not subsets:
                if letter in ascii_letters:
                    second_subset.append(letter.upper())
                    second_subset.append(letter.lower())
                else:
                    second_subset.append(letter)

            while subsets:
                temp = subsets.pop()
                print(temp)
                if letter in ascii_letters:
                    temp2 = temp + letter.lower()
                    temp = temp + letter.upper()
                    second_subset.append(temp2)
                    second_subset.append(temp)
                else:
                    temp += letter
                    second_subset.append(temp)
            subsets, second_subset = second_subset, subsets
        return subsets
