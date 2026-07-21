class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        n = len(nums)

        for i in range(n):
            if i > farest:
                return False
            farest = max(farest, nums[i] + i)
        return True
        