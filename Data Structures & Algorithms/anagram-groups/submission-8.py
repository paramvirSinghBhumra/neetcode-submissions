class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in sol:
                sol[key] = []
            sol[key].append(s)

        return [i for i in sol.values()]