class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        maxi = 0

        for num in nums:
            maxi = max(prev1, prev2 + num)
            prev1, prev2 = maxi, prev1
        return prev1
        