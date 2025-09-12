class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = {char: num.count(char) for char in set(num)}
        palindromic_list = []
        key_list = sorted(list(count.keys()))
        if len(key_list) == 1 and key_list[0] == "0":
            return "0"


        odd_list = []
        for key in key_list:
            if count[key] % 2 == 1:
                count[key] -= 1
                odd_list.append(key)
        if odd_list:
            palindromic_list.append(odd_list[-1])
        


        for key in key_list:
            while count[key] > 0:
                if count[key] % 2 == 0:
                    count[key] -= 2
                    palindromic_list.append(key)
                    palindromic_list.insert(0, key)

        while True:
            if palindromic_list[0] == '0':
                palindromic_list.pop(0)
            if palindromic_list[-1] == '0':
                palindromic_list.pop()
            if palindromic_list[0] != '0' and palindromic_list[-1] != '0':
                break

        list_str = "".join(palindromic_list)



        
        return list_str