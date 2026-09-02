class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack):
            #print(i, haystack[i], needle[0])
            if haystack[i] == needle[0]:
                #print("at loc")
                for j in range(len(needle)):
                    #print(i, j, haystack[i+j], needle[j])
                    if i+j >= len(haystack):
                        return -1
                    if haystack[i+j] != needle[j]:
                        break
                    if j == len(needle)-1:
                        return i
            i+=1

        return -1
        