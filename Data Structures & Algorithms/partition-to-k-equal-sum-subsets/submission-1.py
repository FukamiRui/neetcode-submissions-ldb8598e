class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        curr = 0
        
        nums.sort(reverse=True)

        total = sum(nums)

        if total % k != 0:
            return False
        
        target = total // k
       

        if nums[0] > target:
            return False
        
        subsets = [0] * k

        def backTracking(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]

                    if backTracking(i + 1):
                        return True

                    subsets[j] -= nums[i]

                if subsets[j] == 0:
                    break

            return False

        return backTracking(0)        

        