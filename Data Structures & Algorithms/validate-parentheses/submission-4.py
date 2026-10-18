class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(':')',
            '{':'}', 
            '[': ']'
        }
        stack = []

        for c in s:
            if len(stack) > 0 and stack[-1] in mapping.keys() and mapping[stack[-1]] == c:
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0