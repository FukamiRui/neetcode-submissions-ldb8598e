class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        prev1, prev2 = 0, 0

        for num in nums:
            maxi = max(prev1, prev2 + num) 
            prev1, prev2 = maxi, prev1
        return prev1
        