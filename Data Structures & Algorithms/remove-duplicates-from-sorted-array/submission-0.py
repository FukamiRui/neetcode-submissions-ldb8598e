class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       first_pointer = 0

       for i in range(0, len(nums)):
        if nums[i] != nums[first_pointer]:
            first_pointer += 1

            nums[first_pointer] = nums[i]
       return first_pointer + 1