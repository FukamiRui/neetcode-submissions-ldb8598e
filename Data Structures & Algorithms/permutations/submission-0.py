class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def backTrack():
            if len(nums) == len(curr):
                res.append(curr[::])
                return
            
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    backTrack()
                    curr.pop()
        backTrack()
        return res

