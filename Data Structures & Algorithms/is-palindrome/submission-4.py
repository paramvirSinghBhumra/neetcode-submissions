class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        string = []
        for letter in s:
            if letter.isalnum() and " " != letter:
                letter = letter.lower()
                stack.insert(0, letter)
                string.append(letter)
        
        return stack == string