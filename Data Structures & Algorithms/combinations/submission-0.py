class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []

        def backTracking(i):
            if len(curr) == k:
                res.append(curr[::])
                return
            
            for num in range(i, n + 1):
                curr.append(num)
                backTracking(num + 1)
                curr.pop()
        
        backTracking(1)
        return res

        