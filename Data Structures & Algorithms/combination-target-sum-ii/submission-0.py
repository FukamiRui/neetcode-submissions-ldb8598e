class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def back(i, curr, total):
            if total == target and curr not in res:
                res.append(curr[::])
                return 

  
            if i == len(candidates) or total > target:
                return 

            curr.append(candidates[i])
            back(i + 1, curr, total + candidates[i])
            curr.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            back(i + 1, curr, total)
            
        
        back(0, [], 0)
        return res
            
            
        