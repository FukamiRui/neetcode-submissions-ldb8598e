class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_sum = 0
        

        for i in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += i
            curr_max = max(curr_max, curr_sum)
        
        return curr_max

        
        