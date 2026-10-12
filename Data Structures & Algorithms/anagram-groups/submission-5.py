class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # [0] * 26 [eat, tea] -> 1a, 1e, 1t
        res = {} # create anagram dict where key = letter_count

        for s in strs:
            letter_count = [0] * 26
            for c in s: 
                letter_count[ord(c)-ord("a")] += 1
            
            tpl_cnt = tuple(letter_count)

            if tpl_cnt in res.keys():
                res[tpl_cnt].append(s)
            else:
                res[tpl_cnt] = [s]
            
        return list(res.values())
            
        


                
