class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n=len(nums)
        res=0
        for num in nums:
            
            count =0
            for i in nums:
                if i==num:
                    count +=1
                    if count > n/2:
                        return num
        return res