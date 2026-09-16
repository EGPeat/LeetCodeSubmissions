class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        ig = len(g) - 1
        ic = len(s) - 1
        happy = 0
        while ig >= 0 and ic >= 0:
            if s[ic] >= g[ig]:
                ig -= 1
                ic -= 1
                happy += 1
                #print(s[ic], g[ig], ic, ig, happy)
            else:
                ig -= 1
        return happy