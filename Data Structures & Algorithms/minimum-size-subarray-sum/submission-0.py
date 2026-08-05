class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = float("inf")
        curr = 0
        l = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                mini = min(mini, r - l + 1)
                curr -= nums[l]
                l += 1
        
        return mini if mini != float("inf") else 0

        