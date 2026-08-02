class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = []
        res = []

        def backTracking(opener, closure):
            if opener == n == closure:
                res.append("".join(curr))
                return
            
            if opener < n:
                curr.append("(")
                backTracking(opener + 1, closure)
                curr.pop()
            
            if closure < opener:
                curr.append(")")
                backTracking(opener, closure + 1)
                curr.pop()
        
        backTracking(0, 0)
        return res
        