class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count={}
        for char in s:
            if char in count:
                count[char]= count[char]+1
            else:
                count[char]=1
        
        for char in t:
            if char not in count:
                return False
            elif count[char] ==0 :
                return False
            else:
                count[char]= count[char]-1

        return True

        