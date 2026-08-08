class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checked = {}
        for idx, num in enumerate(nums):
            if num in checked and idx - checked[num] <= k:
                return True
            
            checked[num] = idx
        
        return False
        