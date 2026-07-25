class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapping = set()
        n = 0
        for i in range(len(nums)):
            if nums[i] in mapping:
                return nums[i]
            mapping.add(nums[i])
        