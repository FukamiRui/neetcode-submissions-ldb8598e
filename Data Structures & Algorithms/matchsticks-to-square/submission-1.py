class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        res = []
        curr = 0
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        target = total // 4

        matchsticks.sort(reverse=True)

        if matchsticks[0] > target:
            return False
        
        sides = [0] * 4

        def backTracking(i):
            if i == len(matchsticks):
                return True
            
            for side in range(4):
                if sides[side] + matchsticks[i] <= target:
                    sides[side] += matchsticks[i]
                
                    if backTracking(i + 1):
                        return True

                    sides[side] -= matchsticks[i]
            
                if sides[side] == 0:
                    break

            return False
        
        return backTracking(0)
