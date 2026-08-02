class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        
        if not digits:
            return []

        def backTracking(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            for letter in mapping[digits[i]]:
                backTracking(i + 1, curr + letter)
            
        backTracking(0, "")
        return res
        