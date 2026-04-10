class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        low = 0
        high = (rows * cols) -1
 
        while high >= low:
            mid = low + (high - low) // 2
            row = mid // cols
            col = mid % cols

            val = matrix[row][col]

            if val == target:
                return True
            elif val > target:
                high = mid - 1
            else:
                low = mid + 1
        return False  

        
