class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def backTracking(start):
            if start >= len(s):
                res.append(curr[::])
            
            for end in range(start, len(s)):
                sub = s[start: end + 1]
                if sub == sub[::-1]:
                    curr.append(sub)
                    backTracking(end + 1)
                    curr.pop()
        
        backTracking(0)
        return res

        