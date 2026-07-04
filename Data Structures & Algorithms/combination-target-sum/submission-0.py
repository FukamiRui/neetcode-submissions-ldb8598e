class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if not nums:
            return 0

        def backTracking(i, sum_list, total):
            if total == target:
                res.append(sum_list.copy())
                return
            
            if i >= len(nums) or total > target:
                return
        
            sum_list.append(nums[i])
            backTracking(i, sum_list, total + nums[i])
            sum_list.pop()
            backTracking(i + 1, sum_list, total)
        
        backTracking(0, [], 0)
        return res
    



        

