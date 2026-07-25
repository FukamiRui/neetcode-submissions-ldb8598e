class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapping = set()

        for i in range(len(nums)):
            if nums[i] in mapping:
                return nums[i]
            mapping.add(nums[i])
        