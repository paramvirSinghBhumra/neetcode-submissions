class Solution:
    DELIM = '....'
    def encode(self, strs: List[str]) -> str:
        # if len(strs) != 0:
        #     return self.DELIM.join(strs)
        # return "None"
        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
        
        encoded_sizes = self.DELIM.join(sizes)
        encoded_strings = "".join(strs)

        return encoded_sizes + self.DELIM + encoded_strings
        

    def decode(self, s: str) -> List[str]:
        # if s == "None":
        #     return []
        # return s.split(self.DELIM)
        arr_s = s.split(self.DELIM)
        print(s, arr_s)
        s_string = arr_s[-1]
        final_decode = []

        if arr_s[0] == '':
            return []
        
        start = 0
        for i in range(len(arr_s)-1):
            end = start + int(arr_s[i])
            final_decode.append(s_string[start:end])

            start = end
        
        return final_decode

        