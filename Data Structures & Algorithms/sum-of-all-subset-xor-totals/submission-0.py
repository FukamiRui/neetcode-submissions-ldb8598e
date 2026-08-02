class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        curr = []

        def backTracking(i, curr):
            if i == len(nums):
                return curr
            
            with_XOR = backTracking(i + 1, curr ^ nums[i])
            without_XOR = backTracking(i + 1, curr)

            return with_XOR + without_XOR
        
        return backTracking(0, 0)
        