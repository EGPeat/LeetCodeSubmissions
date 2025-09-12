class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        output = ''
        vowels_rev = ''
        for char in s:
            if char.lower() not in vowels:
                output += char
            else:
                vowels_rev += char
                output += "#"
        vowels_rev = vowels_rev[::-1]
        for new in vowels_rev:
            output = output.replace("#", new, 1)
        return output
