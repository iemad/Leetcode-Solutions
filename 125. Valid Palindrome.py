class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence  = s.lower().replace(' ', '')

        sentence = ''.join(char for char in sentence if char.isalnum())

        return sentence == sentence[::-1]
