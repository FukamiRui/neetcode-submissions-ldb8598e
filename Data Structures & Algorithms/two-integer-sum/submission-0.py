class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

     pre = {}

     for i, n in enumerate(nums):
        comp = target - n

        if comp in pre:
            return [pre[comp], i]
        pre[n] = i 