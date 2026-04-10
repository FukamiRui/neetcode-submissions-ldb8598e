class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        for i in range(n):
            for l in range(0, n - i - 1):
                if nums[l] > nums[l + 1]:
                    nums[l], nums[l + 1] = nums[l + 1], nums[l]
                     
         
        