class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            res = numbers[l] + numbers[r]

            if target == res:
                return [l + 1, r + 1]
            
            elif target < res:
                r -= 1
            
            else:
                l += 1
        
        

        