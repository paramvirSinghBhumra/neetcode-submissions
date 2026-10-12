class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_cntr = {}
        t_cntr = {}

        for i in range(len(s)):
            if s[i] in s_cntr.keys():
                s_cntr[s[i]] += 1
            else:
                s_cntr[s[i]] = 1

        for i in range(len(t)):
            if t[i] in t_cntr.keys():
                t_cntr[t[i]] += 1
            else:
                t_cntr[t[i]] = 1

        return t_cntr == s_cntr
        