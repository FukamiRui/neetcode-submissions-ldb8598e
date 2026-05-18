
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slowest = 1
        fastest = max(piles)
        res = fastest

        while slowest <= fastest:
            mid = slowest + (fastest - slowest) //2
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            
            if total <= h:
                res = mid
                fastest = mid - 1
            else:
                slowest = mid + 1
        return res
                




                

        