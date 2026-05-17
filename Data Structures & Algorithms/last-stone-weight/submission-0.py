class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            max_heap.append(-stone)
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            max_stone_A = -heapq.heappop(max_heap)
            max_stone_B = -heapq.heappop(max_heap)

            if max_stone_A != max_stone_B:
                new_stone = max_stone_A - max_stone_B
                heapq.heappush(max_heap, -new_stone)

        if len(max_heap) == 1:
            return -max_heap[0]
        
        return 0
        
        