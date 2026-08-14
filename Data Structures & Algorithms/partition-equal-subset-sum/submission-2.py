class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if (total % 2) != 0:
            return False
        
        dp = set([0])

        target = total // 2
    
        for num in nums:
            subset = set()
            for curr in dp:
                if curr + num == target:
                    return True

                subset.add(num + curr)
                subset.add(curr)
            dp = subset

        return True if target in dp else False
                
                
        