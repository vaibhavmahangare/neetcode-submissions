class Solution:
    def isPalindrome(self, s: str) -> bool:

        new = s[::-1]
        if s == new:
            return True
        else :
            return False
        