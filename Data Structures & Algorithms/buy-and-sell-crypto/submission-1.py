class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = prices[0]
        max_prof = 0

        for price in prices[1:]:
            if price < sell:
                sell = price
            else:
                prof = price - sell
                max_prof = max(max_prof, prof)
        return max_prof
        