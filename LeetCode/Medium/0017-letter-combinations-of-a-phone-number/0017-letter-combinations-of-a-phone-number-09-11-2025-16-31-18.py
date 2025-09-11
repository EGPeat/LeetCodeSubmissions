class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ln_dict = {
        "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
    }
        return combo_helper(ln_dict, "", 0, digits, []) if len(digits) > 0 else []
def combo_helper(ln_dict, currstring, n, digits, stringlist):
    if n + 1 > len(digits):
        stringlist.append(currstring)
        return
    for option in ln_dict[digits[n]]:
        combo_helper(ln_dict, currstring + option, n+1, digits, stringlist)
    return stringlist