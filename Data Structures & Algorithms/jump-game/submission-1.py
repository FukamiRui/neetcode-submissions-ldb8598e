class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        n = len(nums)

        for i in range(n):
            if curr < i:
                return False
            curr = max(curr, i + nums[i])
        return True
        