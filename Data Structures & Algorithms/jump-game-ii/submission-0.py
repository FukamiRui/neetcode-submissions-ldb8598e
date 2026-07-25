class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        res = 0

        while r < len(nums) - 1:
            curr = 0

            for i in range(l, r + 1):
                curr = max(curr, nums[i] + i)
            
            l = r + 1
            r = curr
            res += 1
        return res

        