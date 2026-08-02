from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        count = Counter(nums)

        def backTracking(i):
           if len(curr) == len(nums):
               res.append(curr[::])
               return 
        
           for num in count:
               if count[num] > 0:
                   curr.append(num)
                   count[num] -= 1

                   backTracking(i + 1)

                   count[num] += 1
                   curr.pop()
        backTracking(0)
        return res


        