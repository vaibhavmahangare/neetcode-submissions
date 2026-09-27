class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l=0
        r=len(numbers)-1
        ans=[]

        while(l<r):
            sum=numbers[l]+numbers[r]
            if sum< target:
                l+=1
            elif sum>target:
                r-=1
            else:
                 ans.append(l+1)
                 ans.append(r+1)
                 break
        
        return ans

         
        