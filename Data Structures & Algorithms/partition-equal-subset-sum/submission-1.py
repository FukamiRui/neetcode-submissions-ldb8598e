class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if (total % 2) != 0:
            return False
        
        target = total // 2
        
        dp = set([0])
        
        for num in nums:
            subset = set()
            for n in dp:
                if n + num == target:
                    return True
                subset.add(n + num)
                subset.add(n)
            dp = subset
        
        return True if target in dp else False


        
        
            

               