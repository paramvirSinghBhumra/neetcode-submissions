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