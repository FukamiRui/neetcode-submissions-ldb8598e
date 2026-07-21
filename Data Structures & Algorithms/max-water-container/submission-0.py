class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        curr_max = 0

        while i < j:
            curr_max = max(curr_max, (j - i) * min(heights[j], heights[i]))
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return curr_max
        