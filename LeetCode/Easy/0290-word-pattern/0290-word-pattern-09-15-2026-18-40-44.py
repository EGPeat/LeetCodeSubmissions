class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        pattern_l = list(pattern)
        if len(pattern_l) != len(words):
            return False

        pw_dict = {}
        wp_dict = {}
        for w, p in zip(words, pattern_l):
            if p in pw_dict and pw_dict[p] != w:
                return False
            if p not in pw_dict and wp_dict.get(w, -1) != -1:
                return False
            else:
                pw_dict[p] = w
                wp_dict[w] = p
        return True