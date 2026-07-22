class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                three = v + nums[left] + nums[right]

                if three > 0:
                    right -= 1
                elif three < 0:
                    left += 1
                
                else:
                    res.append([v, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res

        