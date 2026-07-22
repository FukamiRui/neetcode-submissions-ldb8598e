class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_sum = nums[0]

        for i in nums:
            if curr < 0:
                curr = 0
            curr += i 
            max_sum = max(max_sum, curr)
        
        return max_sum
        