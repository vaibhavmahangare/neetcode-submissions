from typing import List

class Solution:

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[left]
        i = left + 1
        j = right

        while True:
            while i <= right and nums[i] < pivot:
                i += 1

            while nums[j] > pivot:
                j -= 1

            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j

    def quicksort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return

        p = self.partition(nums, left, right)
        self.quicksort(nums, left, p - 1)
        self.quicksort(nums, p + 1, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums
