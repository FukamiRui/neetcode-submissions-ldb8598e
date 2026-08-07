import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        idx = random.randint(0, len(nums) - 1)

        pickup = nums.pop(idx)
        mid_vals = [pickup]

        high, low = [], []

        for num in nums:
            if num > pickup:
                high.append(num)
            elif num < pickup:
                low.append(num)
            else:
                mid_vals.append(num)
        return self.sortArray(low) + mid_vals + self.sortArray(high)
        