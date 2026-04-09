class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(nums, low, high, target):
            if low > high:
                return -1

            mid = low + (high - low) // 2

            if nums[mid] == target:
                    return mid
            elif nums[mid] > target:
                    return binarysearch(nums, low, mid - 1, target)
            else:
                    return binarysearch(nums, mid + 1, high, target)
        
        return binarysearch(nums, 0, len(nums) - 1, target)