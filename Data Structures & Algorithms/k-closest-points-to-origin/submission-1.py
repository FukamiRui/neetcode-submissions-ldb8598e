class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        table = []

        for x, y in points:
            dist = (x ** 2 + y ** 2)
            table.append([dist, x, y])
        
        heapq.heapify(table)
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(table)
            res.append([x, y])
            k -= 1
        
        return res
        