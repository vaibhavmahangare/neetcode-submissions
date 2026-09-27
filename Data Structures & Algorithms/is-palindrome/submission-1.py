class Solution:
    def isPalindrome(self, s: str) -> bool:


        valid=""
        for char in s:
            if 'A'<= char <="Z" or 'a'<= char <="z" or '0'<= char <="9":
                valid = valid+ char
        valid = valid.lower()
        print(valid)
        new =valid[::-1]
        if new == valid:
            return True
        else:
            return False

        