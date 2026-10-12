class Solution:
    DELIM = '....'
    def encode(self, strs: List[str]) -> str:
        if len(strs) != 0:
            return self.DELIM.join(strs)
        return "None"

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        return s.split(self.DELIM)
        
        # for i in range(len(ret)):
        #     if len(ret[i]) == 0:
        #         ret[i] = None
        # return 