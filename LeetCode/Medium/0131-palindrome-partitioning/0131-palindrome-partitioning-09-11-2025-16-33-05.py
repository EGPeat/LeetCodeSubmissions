class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(word):
            return word == word[::-1]

        output = []
        path = []
        
        def dfs(s,output, path, start):
            if start == len(s):
                #print("output found", path, output)
                output.append(path.copy())
                return
            for i in range(start, len(s)):
                #print(path, s, s[start:i+1], start, i+1)
                if is_palindrome(s[start:i+1]):
                    path.append(s[start:i+1])
                    #print("Is palindrome")
                    dfs(s,output, path, i+1)
                    path.pop()
                    
        dfs(s, output, path, 0)
        return output